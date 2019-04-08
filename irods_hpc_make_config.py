#!/usr/bin/env python3

from __future__ import print_function
import os,readline
from subprocess import *
import re,pprint
import json
import sys

#---------#---------#---------#---------#---------#---------#---------#--------

class DefaultCommandTransmuter (object):

    def __init__(self,**kw): 
        self.cmd_map = kw.pop('cmd_map',None)

    def transmute_argv(self, Args):
        if self.cmd_map is not None:
            Args [0] = self.cmd_map [Args[0]]

class SingularityCommandTransmuter(DefaultCommandTransmuter):

    def __init__(self, **kw):
        self.user_home = kw.pop('user_home',None)
        super(SingularityCommandTransmuter,self).__init__(**kw)

    def transmute_argv(self, Args ):
        assert Args[0].endswith('/singularity') or Args[0] == 'singularity', \
            'Singularity commandline check used with wrong binary'
        if Args[1] in ('exec','run','shell'):
            Args [2:2] = ['-H',self.user_home] if self.user_home else []
        super(SingularityCommandTransmuter,self).transmute_argv( Args )

#---------#---------#---------#---------#---------#---------#---------#--------

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

#---------#---------#---------#---------#---------#---------#---------#--------

if __name__ == '__main__':

    icommand_regex = re.compile (b'^/usr/bin/i')
    icommand_binaries_filter   = lambda x: icommand_regex.match(x)

    d = {}

    add_allowed_commands( d, ('dpkg' , '-L', 'irods-icommands'), icommand_binaries_filter)

    singularity_binary_filter = lambda x : x.endswith(b'bin/singularity')

    add_allowed_commands( d, ('dpkg' , '-L', 'singularity-container'), singularity_binary_filter)

    sct = SingularityCommandTransmuter(#user_home = '/tmp/irods_users/daniel',
                                       cmd_map = d)

    #sct.transmute_argv( L )
    print(sct.__dict__)
    print('---------')
    L = ['singularity','exec','my.img'] 
    sct.transmute_argv(L)
    print('L =',L)

    #print(json.dumps( d, indent=4, sort_keys=True ))
    #pprint.pprint(d)


