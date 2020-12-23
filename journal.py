"""
This is a journal module
"""

import os


def get_full_filename(name):
    full_name = os.path.abspath(os.path.join('.', 'journals', name)+'.jrl')
    return full_name


def load(file_name):
    '''
    This method load a journal from a file
    :param file_name: the file name to load the journal
    :return: the journal loaded
    '''
    name = get_full_filename(file_name)
    journal = []
    with open(name,'r') as fin:
        journal.append(fin.read())
    return journal


def save(journal_data, file_name):
    full_name = get_full_filename(file_name)
    print(".....Saving data to {} ".format(full_name))
    with open(full_name, 'a') as fout:
        for entry in journal_data:
            fout.write(entry + '\n')


def add_entry(text, journal):
    journal.append(text)