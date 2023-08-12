import configparser
import os
import sys

############################################################
## Load configs

CONFIG_FILE=os.path.abspath(os.path.expanduser('~/.lcapirc'))
cp = configparser.ConfigParser()

## does our file exist?
if not os.path.exists(CONFIG_FILE):
  cp['default'] = { 'apikey': '',
    'url': '',
    'delay': 5 }
  with open(CONFIG_FILE, 'w') as configfile:
    cp.write(configfile)
else:
  cp.read(CONFIG_FILE)

## make sure we have a valid config
if not len(cp.sections()):
  print("Error: Bad config file! Check your .lcapirc")
  sys.exit(2)

## our config class
class Configs():
  key: str
  url: str
  delay: float

  def __init__(self):
    self.key = { 'apikey': cp.get('default', 'apikey') }
    self.url = cp.get('default', 'url')
    self.delay = float(cp.get('default', 'delay', fallback=None))

## init our config object and free the parser
config = Configs()
cp = None
