# pylint: skip-file
import logging

def log():
     logging.basicConfig(filename='util/main.log',
      filemode='a',
      format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
      datefmt='%Y-%m-%d %H:%M:%S',
      level=logging.INFO)
