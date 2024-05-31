#!/Library/Frameworks/Python.framework/Versions/3.11/bin/python3.11
# -*- coding: utf-8 -*-
from bullcode.cmp import Compiler
import sys

comp = Compiler(config=sys.argv[sys.argv.index("--config") + 1])
comp.run(open(sys.argv[1]).read())