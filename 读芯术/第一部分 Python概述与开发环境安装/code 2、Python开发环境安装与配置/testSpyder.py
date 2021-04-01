# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import sys
import os.path

dir = os.path.dirname(sys.executable)
with open(dir+'\\num.txt', encoding = 'utf-8') as fp:
    content = fp.readlines()
    
print(len(content))