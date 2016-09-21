import sys
import pyimports.bar
import pyimports.baz.sub_baz
# import pyimports.baz

def main():
  # print("sys.path {}".format(sys.path))
  print("foo")
  print(pyimports.bar.get_bar())
  # print(pyimports.baz.get_baz())
  print(pyimports.baz.sub_baz.get_baz())


if __name__ == '__main__':
  sys.exit(main())