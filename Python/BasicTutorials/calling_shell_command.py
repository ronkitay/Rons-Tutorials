#!/usr/bin/python
import subprocess

# pshListOut=subprocess.Popen(["ls", "-la"], stdout=subprocess.PIPE)
# out=subprocess.Popen(["grep", "r"], stdin=pshListOut.stdout, stdout=subprocess.PIPE)
# pshListOut.stdout.close()
# pshListOut.communicate()
# out.communicate()

mycmd=subprocess.getoutput('psh list | g P')
print mycmd

