#!/usr/bin/env python

import platform

'''
Environment Object

The Environment object contains methods to determine the current environment
and operating system.
'''
class Environment(object):

    '''
    The list of Unix based platforms.

    @var list:
    '''
    shell = ['linux', 'linux2', 'darwin']

    '''
    The list of Windows based platforms.

    @var list:
    '''
    cmd = ['win32', 'windows']

    '''
    Class Constructor

    @param self:
    @return void:
    '''
    def __init__(self):
        if self.isUnix():
            print 'yeppers'

    '''
    Get the current operating system.

    @param self:
    @return string:
    '''
    def getOS(self):
        return platform.system()

    '''
    Get the current operating system in lower case

    @param self:
    @return string:
    '''
    def getOSLower(self):
        return self.getOS().lower()

    '''
    Get the current operating system in upper case

    @param self:
    @return string:
    '''
    def getOSUpper(self):
        return self.getOS().upper()

    '''
    Check if the current OS is Unix based.

    @param self:
    @return bool:
    '''
    def isUnix(self):
        if platform.system().lower() in self.shell:
            return True

    '''
    Check if the current OS is Windows based.

    @param self:
    @return bool:
    '''
    def isWindows(self):
        if platform.system().lower() in self.cmd:
            return True
