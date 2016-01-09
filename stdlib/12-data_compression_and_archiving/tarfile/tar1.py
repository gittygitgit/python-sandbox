#!/usr/bin/env python

import tarfile

tar=tarfile.open("f.tar.gz", "w:gz")

for name in ["f1.txt", "f2.txt"]:
  tar.add(name)

tar.close()


