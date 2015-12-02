#!/usr/bin/env python

import string
import random
import getpass
import sys
import os
from passlib.hash import sha512_crypt

try:
  match = False
  while match is False:
    pw = getpass.getpass()
    pw1 = getpass.getpass("Password again: ")
    if len(pw)>0 and pw == pw1:
      match = True
    else:
      print "Passwords do not match or are empty"
  random.seed = (os.urandom(1024))
  salt = ''.join(random.choice(string.ascii_uppercase + string.digits + string.ascii_lowercase + '/' + '.') for _ in range(16))
  print sha512_crypt.encrypt(pw, salt=salt, rounds=5000)
except KeyboardInterrupt:
  print ""
  sys.exit()

