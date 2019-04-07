#!/usr/bin/env python3

from __future__ import print_function
import os,readline
from subprocess import *
import re,pprint
import json
import sys
from abc import (ABCMeta,abstractmethod)

#---------#---------#---------#---------#---------#---------#---------#--------

class CommandTransmuter (object):
    __metaclass__ = ABCMeta
    @abstractmethod
    def __init__(self,*x): 
        raise NotImplementedError('abstract class "{}" cannot be instantiated'.format(self.__class__.__name__))
    @abstractmethod
    def transmute_argv(self, cmdline_elements ):
        pass

class SingularityCommandTransmuter(CommandTransmuter):
    # Note, we need Singularity >= 2.5 for this to work properly
    def __init__(self, userHome): self.user_home = userHome
    def transmute_argv(self, cmd_tuple ):
        assert cmd_tuple[0].endswith('/singularity') or cmd_tuple[0] == 'singularity', \
            'Singularity commandline check used with wrong binary'
        if cmd_tuple[1] in ('exec','run','shell'):
            cmd_tuple [2:2] = ['-H',self.user_home]

sct = SingularityCommandTransmuter('/tmp/irods_users/daniel')


def bytes_to_string( bytes_obj ):
    if sys.version_info >= (3,):
        return bytes_obj.decode()
    return bytes_obj

def add_allowed_commands( targetDict, use_cmd = (), filter_fn=None ):

    stdout_lines = []

    if use_cmd:
        stdout_buf, _ = Popen( use_cmd, stdin=None, stdout=PIPE, stderr=PIPE).communicate()
        stdout_lines = stdout_buf.split(b'\n')

    for f in map(bytes_to_string, filter (filter_fn, stdout_lines)):
        targetDict[os.path.basename(f)] = f
        targetDict[f] = f

if __name__ == '__main__':

    icommand_regex = re.compile (b'^/usr/bin/i')
    icommand_binaries_filter   = lambda x: icommand_regex.match(x)

    d = {}

    add_allowed_commands( d, ('dpkg' , '-L', 'irods-icommands'), icommand_binaries_filter)

    singularity_binary_filter = lambda x : x.endswith(b'bin/singularity')
    add_allowed_commands( d, ('dpkg' , '-L', 'singularity-container'), singularity_binary_filter)
    #print(json.dumps( d, indent=4, sort_keys=True ))
    #pprint.pprint(d)

