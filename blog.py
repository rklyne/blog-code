#!/usr/bin/python

def usage():
  return """./blog.py command [options]
  Command may be:
   * `regenerate` - regenerate the whole blog.
   * That's all for now :-)
  """

def main(args):
  import getopt
  pgm, args = args[0], args[1:]
  long_opts = [
  ]
  short_opts = ''

  opts, args = getopt.getopt(args, long_opts, short_opts)

  if not args:
    print usage()
    return
  
  command, args = args[0], args[1:]
  if command == 'regenerate':
    import generators
    generator = generators.SiteGenerator(find_path('data'), find_path('htdocs'))
    generator.regenerate()
  elif command == 'spike':
    import spike
    spike.test()
  else:
    print "Unknown command ", command
    return

#  raise RuntimeError(args)

def find_path(path):
  import os
  base = os.path.dirname(__file__)
  return os.path.join(base, path)

if __name__ == '__main__':
  import sys
  main(sys.argv)



