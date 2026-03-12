import sys

def foo(**kwargs):
  print(kwargs)
  print(type(kwargs))

if __name__ == "__main__":
  sys.argv.append("test")
  print(sys.argv)
  foo(a=1, b=2)