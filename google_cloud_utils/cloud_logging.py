import logging
from google.cloud import logging as cloud_logging

def init():
  logging.basicConfig(level=logging.INFO)
  log_client = cloud_logging.Client()
  log_client.setup_logging()
