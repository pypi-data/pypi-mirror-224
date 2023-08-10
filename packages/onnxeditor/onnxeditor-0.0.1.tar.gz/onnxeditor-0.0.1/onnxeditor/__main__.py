import sys
from .gui import entry

if __name__ == '__main__':
  if len(sys.argv) == 1:
    entry()
  elif len(sys.argv) == 2:
    entry(path=sys.argv[1])