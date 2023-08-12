#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
import traceback
import logging
import getpass
import openai
from termcolor import colored

class ColoredConsoleHandler(logging.StreamHandler):
    COLORS = {
        'DEBUG': 'blue',
        'INFO': 'green',
        'WARNING': 'yellow',
        'ERROR': 'red',
        'CRITICAL': 'magenta',
    }

    def emit(self, record):
        log_message = self.format(record)
        color = self.COLORS.get(record.levelname, 'white')
        print(colored(log_message, color))

# Create a logger
logger = logging.getLogger()

# Set the logger's level to the lowest level you want to log
logger.setLevel(logging.DEBUG)

# Create a file handler that logs error messages or higher
file_handler = logging.FileHandler('automated_error_handling.log')
file_handler.setLevel(logging.ERROR)  # Set level for the file handler

# Create the colored console handler
console_handler = ColoredConsoleHandler()
console_handler.setLevel(logging.INFO)  # Set level for the console handler

# Create a formatter and set it for both handlers
formatter = logging.Formatter('%(message)s')
file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)

# Add the handlers to the logger
logger.addHandler(file_handler)
logger.addHandler(console_handler)


def custom_error_handler(exception_type, value, tb):
    # Get the traceback information as a string
    traceback_info = "".join(traceback.format_exception(exception_type, value, tb))

    # Extract the line number and file name from the traceback object
    line_number = tb.tb_lineno
    filename = tb.tb_frame.f_code.co_filename

    # Read the file and get the lines surrounding the error
    with open(filename, 'r') as file:
        lines = file.readlines()
        start_line = max(line_number - 5, 0)
        end_line = min(line_number + 5, len(lines))
        surrounding_code = "".join(lines[start_line:end_line])
    logging.error(f"\nError Traceback:\n{traceback_info}\nCode Surrounding Error:\n{surrounding_code}\n")
    # Combine the traceback information and surrounding code
    query = {
        "role": "user",
        "content": f"Error Traceback:\n{traceback_info}\nCode Surrounding Error:\n{surrounding_code}"
    }

    # Send the query to the OpenAI API
    response_content = openai_chat_completion_base_query(query)

    # Print or log the traceback information and response
    logging.info(f"\nSuggested Fix:\n {response_content}")

    # Log the traceback information to the error log file
    return

openai.api_key = getpass.getpass("Please enter your OpenAI API Key: ")

# Your openai_chat_completion_base_query function remains the same
def openai_chat_completion_base_query(query):
    """Returns the response from the OpenAI API given a list of messages."""
    print(colored("Troubleshooting your error...", "yellow"))
    messages = []
    messages.append({"role": "system", "content": "You are a busy and terse site reliability engineer and DevOps specialist. Take the following code block and error message and provide updated code that will fix the error. Only respond with your suggested code change inside a code block, no other information."})
    messages.append(query)
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=messages,
    )
    return response.choices[0].message['content']

def initialize():
    """Initialize the custom error handler with the given OpenAI API Key."""
    openai.api_key = getpass.getpass("Please enter your OpenAI API Key: ")
    sys.excepthook = custom_error_handler