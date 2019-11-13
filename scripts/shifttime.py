#!/usr/bin/env python3

import sys
import re

def totimestamp(epoch):
  ms = epoch % 1000
  epoch = epoch // 1000
  s = epoch % 60
  epoch = epoch // 60
  m = epoch % 60
  epoch = epoch // 60
  h = epoch

  return "{h:1}:{m:02}:{s:02}.{ms:03}".format(h=h, m=m, s=s, ms=ms)

def shiftline(line, delta): # delta is in milliseconds, rounded to 0.01s
  m = re.match("(\d+):(\d+):(\d+)\.(\d+),(\d+):(\d+):(\d+)\.(\d+)", line)
  if not m:
    return line

  h1 = int(m.group(1))
  m1 = int(m.group(2))
  s1 = int(m.group(3))
  ms1 = int(m.group(4))
  epoch1 = ((h1 * 60 + m1) * 60 + s1) * 1000 + ms1

  h2 = int(m.group(5))
  m2 = int(m.group(6))
  s2 = int(m.group(7))
  ms2 = int(m.group(8))
  epoch2 = ((h2 * 60 + m2) * 60 + s2) * 1000 + ms2

  epoch1 += delta
  epoch2 += delta
  return totimestamp(epoch1) + "," + totimestamp(epoch2)

delta = int(sys.argv[1])

for line in sys.stdin.readlines():
  print(shiftline(line.strip(), delta))
