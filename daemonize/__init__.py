"""
jonesy-daemon daemonization library
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

jonesy-daemon is a Python daemonization library. To use it, do something 
like this: 

from jonesy-daemon import daemonize
def main():
    ...some setup stuff here...

    if not args.run_in_foreground:
        daemonize(user='www-data', pidfile='/var/run/myapp.pid')

    myapp = make_app()
    myapp.loop_and_listen(port=80)


By default, stderr/stdout are set to /dev/stderr and /dev/stdout. You can 
override those arguments to daemonize if you want to send all output to the 
same device or break it up differently.

"""
__title__ = 'jonesy-daemon'
__version__ = '0.1.0'
__author__ = 'Brian K. Jones'
__license__ = 'MIT'
__copyright__ = 'Copyright 2012 Brian K. Jones'

from .daemonize import daemonize
