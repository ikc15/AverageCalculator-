"""Computation of weighted average of squares."""
from argparse import ArgumentParser
import numpy as np
import pandas as pd
import json

def read_csv(file):
    """
    Convert a csv into numpy array.
    """
    return np.genfromtxt(file, delimiter=',')

def extract_values_from_json(file):

    return
    
def average_of_columns(data):
    """
    Return the average of columns of numbers.
    
    Example:
    -------
    >>> average_of_columns(np.array([[2,10,200,2],[0, 20, -200, 5]]))
    np.array([1, 15, 0, 3.5])
    """
    means = np.mean(data, axis=0)
    print(means.reshape(1,len(means)))
    return means.reshape(1,len(means))

def write_to_file(data):
    """
    Write results to csv file
    """
    np.savetxt('results.csv',data,delimiter=',')


if __name__ == "__main__":
    parser = ArgumentParser(description="Filename")
    parser.add_argument('file')
    arguments = parser.parse_args()
    data = read_csv(arguments.file)
    write_to_file(average_of_columns(data))