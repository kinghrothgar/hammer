#!/usr/bin/python
from __future__ import print_function
import subprocess

def ip_a():
    stdout = subprocess.Popen('ip a', stdout=subprocess.PIPE, shell=True).stdout.read()

    
