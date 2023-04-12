#!/usr/bin/python3
"""Adds all arguments to a Python list and saves them to a JSON file."""

import sys
import json
from os import path

from save_to_json_file import save_to_json_file
from load_from_json_file import load_from_json_file


if __name__ == "__main__":
    # Define the name of the file to use
    filename = "add_item.json"

    # If the file doesn't exist, create an empty list
    if not path.isfile(filename):
        data = []
    else:
        # Otherwise, load the existing data from the file
        data = load_from_json_file(filename)

    # Add all the arguments to the list
    for arg in sys.argv[1:]:
        data.append(arg)

    # Save the updated data to the file
    save_to_json_file(data, filename)
