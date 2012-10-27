#!/usr/bin/env python

import sys
sys.path.insert(0, '.')

from funnel import *

class MyFunnel(Funnel):
    pass


if __name__ == '__main__':
    myfunnel = MyFunnel()
    myfunnel.run()
