import configparser
import os
import sys

############################################################
## Load configs

cp = configparser.ConfigParser()
cp.read(os.path.abspath(os.path.expanduser('~/.lcapirc')))
## make sure we have a valid config
if not len(cp.sections()):
  print("Unable to parse .lcapirc")
  sys.exit(2)


class Configs():
  key: str
  url: str
  delay: int

  def __init__(self):
    self.key = { 'apikey': cp.get('default', 'apikey') }
    self.url = cp.get('default', 'url')
    self.delay = cp.get('default', 'delay', fallback=None)

config = Configs()
cp = None
