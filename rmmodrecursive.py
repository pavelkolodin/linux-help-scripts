#!/usr/bin/python
# 2022-02-21
import subprocess

def rmmod(name):
    err = "is in use by:"
    result = subprocess.run(['rmmod', name], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    s = result.stderr.decode('utf-8')
    a = -1
    try:
        a = s.index(err)
    except:
        a = -1

    #print(s)
    #print(a)

    if a > -1:
        modules = s[a + len(err):].strip().split(" ")
        for m in modules:
            print("Removing dependency: {}".format(m))
            rmmod(m)

        # retry removing module:
        rmmod(name)
        

rmmod("snd_soc_core")

