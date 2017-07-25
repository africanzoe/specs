# specs
A python script that can be sourced at login to display useful info about the node.

Here is an output sample:

```
--------------------------------------------------------------------

     .--.      Node     : hostname.domain.tld
    |o_o |     System   : Linux
    |:_/ |     Distrib  : Red Hat Enterprise Linux Server 7.3 Maipo
   //   \ \    Release  : 3.10.0-514.el7.x86_64
  (|     | )   Machine  : x86_64
 /'\_   _/'\   Uptime   : 10 days
 \___)=(___/   CPU(s)   : 2
   ~LOGNAME    Memory   : 4096 MiB

--------------------------------------------------------------------
```

All you need to do is:
1. Update your ~/.bash_profile (or the equivalent one dependy on your shell login) with the following line:
  ```
  ~/specs.py
  ```
2. chmod u+x specs.py

If you want to, you can move it to ".specs": a hidden file with no extension. In that case use this line instead:
  ```
  ~/.specs
  ```

## The supported OSs:
- Linux.
- Solaris.
- AIX.
