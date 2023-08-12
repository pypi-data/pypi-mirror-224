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
        'INFO': 'green',
        'WARNING': 'yellow',
        'ERROR': 'red',
    }

    def emit(self, record):
        log_message = self.format(record)
        color = self.COLORS.get(record.levelname, 'white')
        print(colored(log_message, color))

# Create a logger
log = logging.getLogger()

def initialize_logger():
    """Initialize the logger."""
    # Set the logger's level to the lowest level you want to log
    log.setLevel(logging.DEBUG)

    # Create a file handler that logs error messages or higher
    file_handler = logging.FileHandler('stochastic_parrot.log')
    file_handler.setLevel(logging.WARNING)  # Set level for the file handler

    # Create the colored console handler
    console_handler = ColoredConsoleHandler()
    console_handler.setLevel(logging.INFO)  # Set level for the console handler

    # Create a formatter and set it for both handlers
    formatter = logging.Formatter('%(message)s')
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    # Add the handlers to the logger
    log.addHandler(file_handler)
    log.addHandler(console_handler)

def custom_error_handler(exception_type, value, tb):
    # Get the traceback information as a string
    traceback_info = "".join(traceback.format_exception(exception_type, value, tb))

    # Extract the line number and file name from the traceback object
    line_number = tb.tb_lineno
    filename = tb.tb_frame.f_code.co_filename

    # Read the file and get the lines surrounding the error
    with open(filename, 'r') as file:
        lines = file.readlines()
        start_line = max(line_number - 10, 0)
        end_line = min(line_number + 10, len(lines))
        surrounding_code = "".join([f"{i + 1}: {lines[i]}" for i in range(start_line, end_line)])


    logging.error(f"\nError Traceback:\n{traceback_info}\nCode Surrounding Error:\n{surrounding_code}\n")

    # Combine the traceback information and surrounding code
    query = {
        "role": "user",
        "content": f"Error Traceback:\n{traceback_info}\nCode Surrounding Error:\n{surrounding_code}"
    }

    # Send the query to the OpenAI API
    response_content = openai_chat_completion_base_query(query)

    # Print or log the traceback information and response
    logging.info(f"\nStochastic Parrot Code Fix Suggested:\n\n {response_content}\n")

    # Log the traceback information to the error log file
    return

# Your openai_chat_completion_base_query function remains the same
def openai_chat_completion_base_query(query):
    """Returns the response from the OpenAI API given a list of messages."""
    openai_api_key_prompt = "Please enter your OpenAI API Key or type 'skip' to proceed without it: "
    openai_api_key = getpass.getpass(openai_api_key_prompt)

    if openai_api_key.lower().strip() == 'skip':
        logging.warning("Exiting...")
        pass
    else:
        openai.api_key = openai_api_key
    print(colored("\nPlease wait while I troubleshoot your error...", "yellow"))
    messages = []
    messages.append({"role": "system", "content": "You are a busy and terse site reliability engineer and DevOps specialist. Take the following code block and error message and provide updated code that will fix the error. Only respond with your suggested code change inside a code block with line numbers, no other information."})
    messages.append(query)
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=messages,
    )
    content = response.choices[0].message['content']
    cleaned_content = "\n".join([line for line in content.split("\n") if not line.startswith("```")])
    return cleaned_content

def parrot():
    """Initialize the custom error handler with the given OpenAI API Key."""
    sys.excepthook = custom_error_handler