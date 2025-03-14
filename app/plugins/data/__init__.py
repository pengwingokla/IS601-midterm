"""
data_command.py

This module defines the `DataCommand` class, which demonstrates the usage 
of various Python data structures, including lists, tuples, sets, and 
dictionaries. It logs information about their properties, usage, and 
modifications.

Classes:
    - DataCommand: Implements the execution of logging and showcasing
      different data structures.

Usage:
    This class is designed to be used within a command execution system.
    When executed, it logs and prints details about different data structures.
"""

import logging
from commands import Command


class DataCommand(Command):
    """A command that demonstrates Python data structures.

    This class showcases the usage of lists, tuples, sets, and dictionaries.
    It logs their properties, modifications, and iterations.

    Methods:
        execute(): Demonstrates various data structures and logs the output.
    """

    def execute(self):
        """Executes various data structure demonstrations and logs outputs."""
        # Demonstrating Lists
        my_list = ['apple', 'banana', 'cherry']
        logging.info('List example: %s', my_list)
        # Lists are ordered and mutable, making them ideal for storing a
        # collection of items that may change over time.
        logging.info('I pick an %s', my_list[0])
        my_list.append('date')  # Adding an item to the list
        logging.info('List after adding an item: %s', my_list)

        # Demonstrating Tuples
        my_tuple = (1, 2, 3, 4)
        logging.info('Tuple example: %s', my_tuple)
        # Tuples are ordered and immutable, suitable for storing a collection
        # of items that should not change.
        logging.debug('My Tuple is %s', my_tuple[0])

        # Demonstrating Sets
        my_set = {1, 2, 3, 4}
        my_set2 = {2, 3, 4, 5}
        logging.info('Set example: %s', my_set)
        logging.info('Whats different: %s', my_set.difference(my_set2))
        # Sets are unordered, mutable, and do not allow duplicate values,
        # ideal for unique collections without specific order.

        my_set.add(5)  # Adding an item to the set
        logging.info('Set after adding an item: %s', my_set)

        # Demonstrating Dictionaries
        states_abbreviations = {
            'CA': 'California',
            'NJ': 'New Jersey',
            'TX': 'Texas',
            'FL': 'Florida',
            'IL': 'Illinois'
        }

        logging.info('Dictionary example: %s', states_abbreviations)
        # Dictionaries store data in key-value pairs. They are mutable and
        # unordered, ideal for fast lookups where each value is associated
        # with a unique key.

        states_abbreviations['NY'] = 'New York'  # Adding a new key-value pair
        logging.info(
            'Dictionary after adding a state: %s', states_abbreviations
        )

        # Demonstrating dictionary iteration
        for abbreviation, full_name in states_abbreviations.items():
            logging.info(
                'State Abbreviation: %s for: %s', abbreviation, full_name
            )

        # Advanced use case: Nested Dictionaries
        states_info = {
            'CA': {
                'capital': 'Sacramento',
                'population': 39538223,  # As of the latest estimates
                'great': 'No'
            },
            'TX': {
                'capital': 'Austin',
                'population': 29145505,  # As of the latest estimates
                'great': 'Yes'
            },
            'NJ': {
                'capital': 'Trenton',
                'population': 50,  # As of the latest estimates
                'great': 'Yes',
                'good hot dogs': 'yes',
                'where': 'Rutts hutt'
            }
        }

        for state, info in states_info.items():
            # Log the state abbreviation
            logging.info('State: %s', state)
            print(f"State: {state}")

            # Iterate through each property of the state and print/log it
            for property_name, property_value in info.items():
                property_info = (
                    f"{property_name.capitalize()}: {property_value}"
                )
                print(property_info)
                logging.info('%s', property_info)
