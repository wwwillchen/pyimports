from pyimports import bar

def shout():
  print('shout ' + bar.get_bar())

def get_baz():
  return 'baz'

shout()