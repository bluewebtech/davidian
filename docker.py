#!/usr/bin/env python

# Import some modules.
import os
import re
import sys
from subprocess

#
# Currently using this module as a scratch pad.
#

_env = '\n'.join([i for i in os.popen("docker-machine env davidian 2>&1").read().split('\n') if len(i) > 0])
_env = re.sub(r'^#.*$', '', _env, flags=re.MULTILINE)  # Remove comments
_env = re.sub(r'^export ', '', _env, flags=re.MULTILINE)  # Remove `export `
_env = re.sub(r'\n', ' ', _env, flags=re.MULTILINE)  # Merge to a single line
#_env = re.sub(r'"', '', _env, flags=re.MULTILINE)  # Merge to a single line
_env_list = _env.split(' ')
_env_list = filter(bool, _env_list) # fastest

subprocess.call(['./davidian.sh'])

#for item in _env_list:
#    item_split = item.split('=')
#    subprocess.call(['./env.sh'])
#    os.putenv(item_split[0], item_split[1])
