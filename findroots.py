import pykd
import sys
import argparse
import re
parser = argparse.ArgumentParser(description='Search a given generation and output rooted items for a specific type and optionally its size')
parser.add_argument('gen', metavar='generation', type=int, help='GC generation to scan')
parser.add_argument('type', metavar='typename',  help='The typename you are scanning for roots for')
parser.add_argument('--size', help="size of the object we are searching for root on")
parser.add_argument("--verbose", help="increase output verbosity",action="store_true")

args=parser.parse_args()


pykd.dprintln ("Scanning for rooted objects in Gen={0} for type={1}".format(args.gen, args.type))

s = pykd.dbgCommand("!chain")
out = ""
if not("sos.dll" in s):
	pykd.dprintln("sos not found ...... loading sos")
	out = pykd.dbgCommand("!loadby sos clr")
	print out
if not("sosex.dll" in s):
	pykd.dprintln("sosex not found ...... loading sosex please wait")
	out = pykd.dbgCommand("!load sosex")
	print out
	pykd.dprintln("Building heap index this may take a few minutes....")
	out = pykd.dbgCommand("!bhi")
	pykd.dprintln(out)


command = "!dumpgen {0} -type {1}".format(args.gen, args.type)
prog = re.compile('^([^\W]*)\W+([^\W]*)\W+([^\W]*)')

for i in pykd.dbgCommand(command).split("\n"):
	out = ""
	if(args.type in i):
		m = prog.match(i)
		if args.verbose:
			print "Checking for root for address:{0} ".format(m.group(1))
		if(args.size and m.group(3) == args.size):
			out = pykd.dbgCommand('!mroot {0}'.format(m.group(1)))
		elif not(args.size):
			out = pykd.dbgCommand('!mroot {0}'.format(m.group(1)))
		if out and not('No root' in out):
			pykd.dprintln("Root found at: <link cmd=\"!mdt {0}\">{0}</link> having size of {1}".format(m.group(1),m.group(3)), True)
			print out
	