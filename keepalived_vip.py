#!/usr/bin/env python
#coding=utf-8
#date 2016-03-11
#auth :lianghx

import os,commands,sys,time
import json
keepalived_conf_file='/etc/keepalived/keepalived.conf'
if not os.path.exists(keepalived_conf_file):
    sys.exit(4)
status,vips=commands.getstatusoutput('''grep '192.168.' %s|awk '{print $1}' ''' %keepalived_conf_file)

def discovery_vips():
    array = []
    for v in vips.split('\n'):
        vip = {}
        vip['{#IP}'] = v
        array.append(vip)
    jsonStr=json.dumps({'data': array}, indent=4, separators=(',',':'))
    print jsonStr

def monit_lvs(vip):
    status,keepalived_vip_status=commands.getstatusoutput('/sbin/ip addr |grep %s |wc -l' %vip)
    print status,keepalived_vip_status

if __name__=='__main__':
    discovery_vips()
    monit_lvs('192.168.100.188');
    monit_lvs('192.168.100.135');

