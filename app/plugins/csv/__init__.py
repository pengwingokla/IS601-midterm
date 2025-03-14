"""
csv_command.py

This module defines the `CsvCommand` class, which demonstrates the process of:
- Ensuring a directory exists for storing CSV files.
- Converting a dictionary to a pandas DataFrame and saving it as a CSV file.
- Reading the CSV back into a DataFrame and logging its content.

Classes:
    - CsvCommand: Implements CSV-related operations including saving and reading state abbreviations.

Usage:
    This command is designed to be used within a command execution system.
    When executed, it logs and processes state data using CSV files.
"""

import logging
import os
import pandas as pd
from commands import Command


class CsvCommand(Command):
    """A command that demonstrates handling CSV files using pandas.

    This class ensures a target directory exists, creates a DataFrame from 
    a dictionary, saves it as a CSV file, and then reads and logs the contents.
    """
    def execute(self):
        """Executes the CSV file creation and reading process.

        This function:
        - Ensures the 'data' directory exists and is writable.
        - Converts a dictionary of state abbreviations into a pandas DataFrame.
        - Saves the DataFrame to a CSV file.
        - Reads the CSV file back into a DataFrame and logs the content.

        Raises:
            OSError: If the 'data' directory is not writable.
        """
        # Ensure the 'data' directory exists and is writable
        data_dir = './data'
        if not os.path.exists(data_dir):
            os.makedirs(data_dir)
            logging.info("The directory '%s' is created", data_dir)
        elif not os.access(data_dir, os.W_OK):
            logging.error("The directory '%s' is not writable.", data_dir)
            return

        # Convert dictionary to DataFrame and save to CSV
        states_abbreviations = {
            'CA': 'California',
            'NJ': 'New Jersey',
            'TX': 'Texas',
            'FL': 'Florida',
            'IL': 'Illinois',
            'NY': 'New York'  # Newly added state
        }
        df_states = pd.DataFrame(list(states_abbreviations.items()), columns=[
                                 'Abbreviation', 'State'])
        csv_file_path = os.path.join(data_dir, 'states.csv')
        df_states.to_csv(csv_file_path, index=False)

        logging.info("States saved to CSV at '%s'.", csv_file_path)

        # This is creating the path for saving the file.
        csv_file_path = os.path.join(data_dir, 'gpt_states.csv')
        logging.info("The relative path to save my file is %s", csv_file_path)

        # Read the CSV file back into a DataFrame
        absolute_path = os.path.abspath(csv_file_path)
        logging.info("The absolute path to save my file is %s", absolute_path)

        try:
            df_read_states = pd.read_csv(csv_file_path)
        except FileNotFoundError:
            logging.error(
                "File '%s' not found. Please check if it was created correctly.", csv_file_path)
            return

        # Print and log each state nicely
        print("States from CSV:")
        for index, row in df_read_states.iterrows():
            # First, print and log the complete record for the state
            state_info = "%s: %s" % (row['Abbreviation'], row['State'])
            print("Record %d: %s" % (index, state_info))
            logging.info("Record %d: %s", index, state_info)

            # Then, iterate through each field in the row to print and log
            for field in row.index:
                field_info = "    %s: %s" % (field, row[field])
                print(field_info)
                logging.info("Index: %d, %s", index, field_info)
