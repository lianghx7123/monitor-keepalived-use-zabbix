#!/usr/bin/env python
#coding=utf-8
#date 2016-03-11
#auth :lianghx
  
import os,commands,sys,time
keepalived_conf_file='/etc/keepalived/keepalived.conf'
if not os.path.exists(keepalived_conf_file):
    sys.exit(4)

vips=commands.getstatusoutput('''grep '192.168.' %s ''' %keepalived_conf_file)[1].strip()
print  vips
