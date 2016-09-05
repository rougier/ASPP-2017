# -----------------------------------------------------------------------------
# Copyright (c) 2016, Nicolas P. Rougier. All Rights Reserved.
# Distributed under the (new) BSD License. See LICENSE.txt for more info.
# -----------------------------------------------------------------------------
# Scientific visualization course (https://github.com/rougier/ASPP-2016)
# Advanced Scientific Python Programming course
# University of Reading, 2016, https://python.g-node.org/wiki/ 
# -----------------------------------------------------------------------------
import matplotlib.pyplot as plt

dpi = 300
fig = plt.figure(figsize = (3.15,3.15))

plt.subplot(111)
plt.savefig("exercise-4.png", dpi=dpi)
plt.show()

