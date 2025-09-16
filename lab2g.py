#!/usr/bin/env python3
# Author: Mikal Dixon
# Author ID: mdixon21
# Date Created: 2025/09/16
import sys
timer = 3
if len(sys.argv) > 1:
    timer = int(sys.argv[1])
while timer != 0:
    print(timer)
    timer = timer - 1
print('blast off!')