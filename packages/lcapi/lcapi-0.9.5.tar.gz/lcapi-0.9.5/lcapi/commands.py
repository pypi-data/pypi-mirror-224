import json
import os
import requests
import time

from lcapi.config import config

def show_lists():
  print ("Retreiving available lists ...")
  ## make our request
  req = requests.post(f"{config.url}&api2&get=lists_list", data=config.key)
  
  if req.status_code == 200:
    ## if we are successful, loop through the results
    lsts = json.loads(req.text)
    for ls in lsts['result']:
      print(f"{ls['name']}\t{ls['type']}")
  else:
    ## if we fail, show the error
    msg = json.loads(req.text)
    print (f"Error: {msg['error']}")

def download(ls, typ, outfile):
  print(f"Downloading {ls}.{typ}.txt ...")
  req = requests.post(f"{config.url}&download={typ}&file={ls}", data=config.key)
   
  #if req.status_code == 200:
  ## lc doesn't support error codes yet, let's work around this
  try:
    err = json.loads(req.text)
  except json.decoder.JSONDecodeError as e:
    err = None
  if not err:
    ## if successful, save our files
    if outfile:
      open(outfile, 'ab').write(req.content)
    else:
      open(f"{ls}.{typ}.txt", 'wb').write(req.content)
  else:
    ## if we fail, show the error
    msg = json.loads(req.text)
    print (f"Error: {msg['error']}")

def upload(ls, infile, watch):
  ## expand out path before processing
  infile = os.path.abspath(os.path.expanduser(infile))

  last_mtime=0
  while True:
    ## when looping, only upload if the infile has been modified since last check
    mtime = os.path.getmtime(infile)
    if mtime == last_mtime:
      continue
    last_time = mtime
    
    print(f"Uploading to {ls} ...")
    ## select our file to upload
    files = {'file': open(infile, 'rb')}
    ## upload!
    req = requests.post(f"{config.url}&uploadlistname={ls}", data=config.key, files=files)
    ## dump our response
    msg = json.loads(req.text)
    if msg['message']:
      print(msg['message'])
    else:
      print(f"Error: {msg['error']}")
    if not watch:
      break
    time.sleep(float(config.delay))
