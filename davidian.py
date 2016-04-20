#!/usr/bin/env python

# Import some modules.
import os, sys

# Set up a few defaults values.
ROOT = os.path.dirname(os.path.realpath(__file__))
PROJECT = os.path.basename(ROOT)

# Set the binary root for all mobules.
sys.path.insert(0, ROOT + '/bin')

# Import the davidian modules.
import modules

# Docker all the things.
modules.Docker(PROJECT)