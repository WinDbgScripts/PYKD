WinDbgScripts PYKD
=============

The following set of scripts are meant to make your life easier when using WinDbg for tracking and troubleshooting your applications.
In this repository I will be adding any scripts written in Python and meant for use with the PYKD windbg extension.. 

PYKD Scripts
-------

These dependencies are needed to use these scripts in WinDBG.

* [Python](https://www.python.org/) -- I Installed this directly into the Debugger base directory, but you can install where you would like.  Just make sure the python executable is in the search path.
* [PYKD](https://pykd.codeplex.com/) -- Be sure to follow the instructions as stated on the site.
* [SOSEX](http://www.stevestechspot.com/SOSEXV40NowAvailable.aspx) -- This is an extension for the Windbg tools that more effectively and efficiently walks the .net Heaps and Threads

Installation
-----------

    Download the github repository and copy the scripts into the %debuggerbasedirectory%\scripts directory

Usage
-----

    In WinDbg:
		- .load pykd.pyd
		- !py scripts/scriptname.py
		
Script Descriptions
-----------------------
	findroots.py - This script takes a Generation and Object Type Name as inputs.  It will scan the given generation for the type of object you specified and return only the items that are rooted and give you a clickable link back.  You can further specify a specific size also to narrow down the objects your trying to find that may still be rooted.


	
	