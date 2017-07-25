#!/usr/bin/env python

from subprocess import Popen, PIPE
import platform
import multiprocessing
import socket
import os

def main():
    node    = socket.getfqdn()
    system  = platform.system()
    dist    = ' '.join(platform.linux_distribution())
    distrib = "NA" if dist.isspace() or dist is None else dist
    release = platform.release()
    machine = platform.machine()
    # Get the uptime from the cmdline and reformat it according
    p = Popen('uptime', stdin=PIPE, stdout=PIPE, stderr=PIPE)
    output = p.communicate()[0]
    if 'day' in output:
        uptime = ' '.join(output.split('\n')[0].split()[2:4]).replace(',', '')
    else:
        uptime = ' '.join(output.split('\n')[0].split()[2:3]).replace(',', '') + " h"
    cpus    = str(multiprocessing.cpu_count())
    logname = os.environ['LOGNAME']

    display_size = max(
                       len(node),
                       len(system),
                       len(distrib),
                       len(release),
                       len(machine),
                       len(uptime),
                       len(cpus)
                   )

    print((display_size + 27) * "-" + '\n')
    print('     .--.      Node     : {0}'.format(node))
    print('    |o_o |     System   : {0}'.format(system))
    print('    |:_/ |     Distrib  : {0}'.format(distrib))
    print('   //   \ \    Release  : {0}'.format(release))
    print('  (|     | )   Machine  : {0}'.format(machine))
    print(" /'\_   _/'\   Uptime   : {0}".format(uptime))
    print(' \___)=(___/   CPU(s)   : {0}'.format(cpus))
    
    if system == "Linux":
        f = Popen('free', stdin=PIPE, stdout=PIPE, stderr=PIPE)
        mem = int(f.communicate()[0].split('\n')[1].split()[1]) / 1024
        print('   ~' + '{0:<10}'.format(logname)[:10] + ' Memory   : ' + str(mem) + " MiB")
    # Use of the prtconf connamd on Solaris OS
    elif system == "SunOS":
        try:
            mem = Popen(
                        '/usr/sbin/prtconf',
                         stderr=PIPE,
                         stdout=PIPE,
                         shell=False
                  ).communicate()[0].split('\n')[1].split()[2]
            print('   ~' + '{0:<10}'.format(logname)[:10] + ' Memory   : ' + str(mem) + " MiB")
        except:
            print('   ~' + '{0:<10}'.format(logname)[:10] + ' Memory   : ' + 'Error occured during memory fetch')
    # Use of the svmon connamd on AIX OS
    elif system == 'AIX':
        try:
            mem = Popen(
                        ['/usr/bin/svmon', '-G'],
                         stderr=PIPE,
                         stdout=PIPE,
                         shell=False
                  ).communicate()[0].split('\n')[1].split()[2]
            print('   ~' + '{0:<10}'.format(logname)[:10] + ' Memory   : ' + str(mem) + " MiB")
        except:
            print('   ~' + '{0:<10}'.format(logname)[:10] + ' Memory   : ' + 'Error occured during memory fetch')
    # The non yet supported OS
    else:
        print('   ~' + '{0:<10}'.format(logname)[:10] + ' Memory   : ' + '< Not implemented yet for the OS: {0} >'.format(system))
    print('\n' + (display_size + 27) * "-")

if __name__ == '__main__':
    main()
