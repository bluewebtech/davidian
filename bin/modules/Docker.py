#!/usr/bin/env python

import inspect
import modules
import os
import Prompt
import re
from subprocess import call

'''
Docker Object

The Docker object contains methods and processes for managing 
all Docker related tasks. It checks if a Docker machine exists,
has been started, stopped or needs to be created.
'''
class Docker(object):

    '''
    Class Constructor

    @param self:
    @param string project:
    @return void:
    '''
    def __init__(self, project):
        self.docker = 'docker'
        self.compose = 'docker-compose'
        self.machine = 'docker-machine'
        self.project = project
        self.event(self.status())

    def build(self):
        self.message('build')
        os.system('docker build -t ' + self.project + ' .')
        return self

    def up(self):
        os.system('docker-compose up')
        return self

    '''
    Regenerate machine certificates.

    @param self:
    @return self:
    '''
    def certs(self):
        self.message('certs')
        os.system(self.machine + ' regenerate-certs ' + self.project)
        return self

    '''
    Run the Docker create up process.

    @param self:
    @return self:
    '''
    def create(self):
        self.message('create').process('create').env()

    def getEnv(self):
        return '\n'.join([i for i in os.popen(self.machine + ' env ' + self.project + " 2>&1").read().split('\n') if len(i) > 0])

    '''
    Handle the Docker events based on the current container status.

    @param self:
    @param string status:
    @return string:
    '''
    def event(self, status):
        if (status == 'Running'):
            self.stop()
        else:
            self.run()

    '''
    Get the flag command string.

    @param self:
    @param string flag:
    @return self:
    '''
    def flag(self, flag):
        return 'create --driver virtualbox' if flag == 'create' else flag

    '''
    Display the defined message.

    @param self:
    @param message:
    @return string:
    '''
    def message(self, message):
        print self.messages()[message]
        return self

    '''
    Return dictionary of messages.

    @param self:
    @return dict:
    '''
    def messages(self):
        return {
            'build':   'Building the (' + self.project + ') docker image.',
            'certs':   'Generating certificates for docker machine (' + self.project + ').',
            'create':  'Creating docker machine (' + self.project + ') since it was not found.',
            'env':     'Setting the (' + self.project + ') environment variables.',
            'ignore':  'Ok! As you were soldier.',
            'prepare': 'Preparing environment: ' + self.project + ' : ' + self.status(),
            'start':   'The docker machine (' + self.project + ') already exists.',
            'stop':    'The docker machine (' + self.project + ') is now stopping,'
        }

    '''
    Handle the specific process based on flag.

    @param self:
    @param string flag:
    @return self:
    '''
    def process(self, flag):
        #print self.machine + ' ' + self.flag(flag) + ' ' + self.project
        os.system(self.machine + ' ' + self.flag(flag) + ' ' + self.project)
        return self

    '''
    Create the Docker machine based off the name of the project root directory.

    @param self:
    @return string:
    '''
    def run(self):
        if 'not' in self.status():
            self.create()
        else:
            self.start()

    '''
    Run the Docker start up process.

    @param self:
    @return self:
    '''
    def start(self):
        self.message('start').process('start').env()
        return self

    '''
    Get the status of the current Docker machine.

    @param self:
    @return string:
    '''
    def status(self):
        return '\n'.join([i for i in os.popen(self.machine + ' status ' + self.project + " 2>&1").read().split('\n') if len(i) > 0])

    '''
    Run the Docker stop up process.

    @param self:
    @return self:
    '''
    def stop(self):
        if (modules.Prompt().ask('Would you like to stop the ('  + self.project + ') Docker container?')):
            self.message('stop').process('stop')
        else:
            self.message('ignore')
