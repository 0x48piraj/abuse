__all__ = ('list_abuses_from', 'random_abuse_from', 'list_all_abuses', 'random_abuse')

import random
import csv
import os

_DATASET = []


def load_dataset():
    """ Loads the dataset from the csv and puts it into the global variable _DATASET"""
    current_file = os.path.abspath(os.path.dirname(__file__))
    csv_filename = os.path.join(current_file, 'abuse_en.csv')

    with open(csv_filename) as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            _DATASET.append(row[0])


def list_abuses_from(first_letter):
    """ Returns list of abuses starting from a specific letter provided in argument of the function. """
    if not (isinstance(first_letter, str) and first_letter.isalpha() and len(first_letter) == 1):
        raise ValueError("argument must be a letter")
    first_letter = first_letter.lower()

    return [w for w in _DATASET if w.lower().startswith(first_letter)]


def random_abuse_from(first_letter):
    """ Returns a random abuse starting from a specific letter provided in argument of the function. """
    words = list_abuses_from(first_letter)
    return random.choice(words) if words is not None else None


def random_abuse():
    """ Returns any random abuse from it's built-in dataset. """
    return random.choice(_DATASET)


def list_all_abuses():
    """ Just returns all the abusive words present in the dataset. """
    return _DATASET.copy()


load_dataset()
