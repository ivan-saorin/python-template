import argparse
import logging
import colorlog

# Create a logger object
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# Create a colored console handler
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
formatter = colorlog.ColoredFormatter(
    '%(log_color)s%(levelname)s:%(message)s%(reset)s'
)
ch.setFormatter(formatter)
logger.addHandler(ch)

def testLogging():
  # Log some messages with different levels
  logger.debug('This is a debug message')
  logger.info('This is an info message')
  logger.warning('This is a warning message')
  logger.error('This is an error message')
  logger.critical('This is a critical message')

def main():
  logger.info("Hello, World!")

  #  parser = argparse.ArgumentParser(description='Py Project CLI')
  #  parser.add_argument('--run-api', action='store_true', help='Run the API')
  #  args = parser.parse_args()
    
  # if args.run_api:
  #  start_api()

if name == "main":
  main()
