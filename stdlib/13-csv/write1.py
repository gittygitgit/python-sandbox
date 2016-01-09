#!/usr/bin/env python
import csv

with open('foo.csv', 'wb') as f:
  writer=csv.writer(f)
  writer.writerow(('one', 'two', 'three'))


