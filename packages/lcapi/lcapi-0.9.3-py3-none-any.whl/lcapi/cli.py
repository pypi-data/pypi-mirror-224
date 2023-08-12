#!/bin/env python3

import argparse
import pkg_resources
import sys
import time

import lcapi.commands
from lcapi.config import config

############################################################
## Version Check

if (sys.version_info < (3, 0)):
  sys.stderr.write("[!] Error! Must execute this script with Python3.")
  sys.exit(2)

############################################################
## Parse options

parser = argparse.ArgumentParser(
    description='CLI client for the lc API.')
parser.add_argument('--delay',
                    dest='delay',
                    action='store',
                    type=float,
                    help='delay between uploads')
parser.add_argument('-o',
                    dest='outfile',
                    action='store',
                    default=None,
                    help='append downloads to <OUTFILE>')
parser.add_argument('-d', '--download',
                    dest='download',
                    action='store_true',
                    help='download a list')
parser.add_argument('--lists',
                    dest='lists',
                    action='store_true',
                    help='show all available lists')
parser.add_argument('-t', '--type',
                    dest='type',
                    action='store',
                    nargs='?',
                    default='left',
                    const='default',
                    help='Specify the list type: dict, list, left, found, multi, or log (defaults to left)')
parser.add_argument('-u', '--upload',
                    dest='upload',
                    help='upload plains from <UPLOAD>')
parser.add_argument('--version',
                    dest='version',
                    action='store_true',
                    help='display version and exit.')
parser.add_argument(
                    dest='LIST',
                    action='store',
                    nargs='*',
                    help='lists to target')
args = parser.parse_args()


############################################################
## Main App

def main():
  ## show lists
  if args.lists:
    lcapi.commands.show_lists()
    sys.exit(1)
  
  ## show version
  if args.version:
    print(f"lcapi v{pkg_resources.require('lcapi')[0].version}")
    sys.exit(1)

  ## if we set a delay param, override the config value
  if args.delay:
    config.delay = args.delay
  
  ## init our loop flag
  looped = False
  ## loop through our lists and process actions
  for ls in args.LIST:
    if looped and config.delay:
      ## if we already looped once and have a delay, wait
      time.sleep(float(config.delay))
    if args.download:
      ## download
      lcapi.commands.download(ls, args.type, args.outfile)
    elif args.upload:
      ## upload
      lcapi.commands.upload(ls, args.upload)
    ## set out loop flag
    looped = True
if __name__ == "__main__":
  main()
