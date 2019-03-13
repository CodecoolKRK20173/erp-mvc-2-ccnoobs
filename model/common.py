""" Common functions for models
implement commonly used functions here
"""
import random


def generate_random(table):
    """
    Generates random and unique string. Used for id/key generation:
         - at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letter
         - it must be unique in the table (first value in every row is the id)

    Args:
        table (list): Data table to work on. First columns containing the keys.

    Returns:
        string: Random and unique string
    """

    generated = ''
    generated_not_on_list = True
    while generated_not_on_list:
        generated = random.choice("abcdefghijklmnopqrstuvwxyz") + \
            random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ") + \
            str(random.randrange(9)) + \
            str(random.randrange(9)) + \
            random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ") + \
            random.choice("abcdefghijklmnopqrstuvwxyz") + \
            str(random.choice("!$%&()*+,-./:<=>?@[\]^_`{|}~")) + \
            str(random.choice("!$%&()*+,-./:<=>?@[\]^_`{|}~"))
        generated_not_on_list = False
        for element in table:
            if element[0] == generated:
                generated_not_on_list = True




    return generated


def add(table, record):
    record.insert(0, generate_random(table))
    table.append(record)
    return table


def update(table, id_, record):
    entry_index = 0
    for entry in table:
        entry_id_ = entry[0]
        if entry_id_ == id_:
            searched_entry_index = entry_index
        entry_index += 1

    entry_index = 0
    for entry in table[searched_entry_index]:
        if record[entry_index] != "":
            table[searched_entry_index][entry_index] = record[entry_index]
        entry_index += 1

    return table
    # your code


def remove(table, id_):
    current_entry_index = 0
    for entry in table:
        entry_id_ = entry[0]
        if entry_id_ == id_:
            del table[current_entry_index]
        current_entry_index += 1

    return table
