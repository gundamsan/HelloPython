# coding: utf-8

# for ptvsd debug.
import ptvsd        
import platform


# for ptvsd debug.
ptvsd.enable_attach(secret = 'ptvsd')
os = platform.system()
print 'Waiting for attach...'
if os != 'Windows':
    ptvsd.wait_for_attach()



print 'Hello,World!!'
print 'platform.system: %s' % os
