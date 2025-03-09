#!/bin/python3
import sys
import os
from git import Repo
from b.xmlengine import *

def printDescription():
    print(">> This is just B.")
    print(">> The Buildsystem")
    print(">> Made by Nakada Tokumei")

def printDebug(string):
    print("[Debug] " + string)

if __name__ == "__main__":
    printDebug("argv : " + sys.argv[1])
    xmlengine = XMLEngine(sys.argv[1])
    xmlengine.do_parse()
    pass