"""
In this modules we defined the logger object, using which the logging can be done
"""
import logging

# Create and configure logger
logging.basicConfig(filename="logfile.log", format='[%(asctime)s] - %(levelname)s - %(message)s', filemode='w')

# Creating an object
logger = logging.getLogger()

# Setting the threshold of logger to DEBUG
logger.setLevel(logging.INFO)
