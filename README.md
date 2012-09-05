jonesy-daemon
--------------

jonesy-daemon is a really simple 'quick-n-dirty' daemonization library for use
in Python apps.

The basic usage looks something like this: 

```python
from jonesy_daemon import daemonize
def main():
    ...some setup stuff here...

    if not args.run_in_foreground:
        daemonize(user='www-data', pidfile='/var/run/myapp.pid')

    myapp = make_app()
    myapp.loop_and_listen(port=80)

```

By default, stderr/stdout are set to /dev/stderr and /dev/stdout. You can
override those arguments to daemonize if you want to send all output to the
same device or break it up differently.

