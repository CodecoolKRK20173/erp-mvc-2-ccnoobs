""" Store module

Data table structure:
    * id (string): Unique and random generated identifier
        at least 2 special characters (except: ';'), 2 number, 2 casefold and 2 upper case letters)
    * title (string): Title of the game
    * manufacturer (string)
    * price (number): Price in dollars
    * in_stock (number)
"""

# everything you'll need is imported:
from model import data_manager
from model import common

def get_store_table_from_file():
    return data_manager.get_table_from_file('model/store/games.csv')

def add(table, record):
    """
    Add new record to table

    Args:
        table (list): table to add new record to
        record (list): new record

    Returns:
        list: Table with a new record
    """
    table = common.add(table, record)

    return table


def remove(table, id_):
    """
    Remove a record with a given id from the table.

    Args:
        table (list): table to remove a record from
        id_ (str): id of a record to be removed

    Returns:
        list: Table without specified record.
    """

    table = common.remove(table, id_)
    return table


def update(table, id_, record):
    """
    Updates specified record in the table.

    Args:
        table: list in which record should be updated
        id_ (str): id of a record to update
        record (list): updated record

    Returns:
        list: table with updated record
    """

    table = common.update(table, id_, record)

    return table


# special functions:
# ------------------

def get_counts_by_manufacturers(table):
    """
    Question: How many different kinds of game are available of each manufacturer?

    Args:
        table (list): data table to work on

    Returns:
         dict: A dictionary with this structure: { [manufacturer] : [count] }
    """
    dictionary = {}
    for element in table:
        if element[2] in dictionary.keys():
            dictionary[element[2]] += 1
        if element[2] not in dictionary.keys():
            dictionary[element[2]] = 1
    return dictionary
 

def get_average_by_manufacturer(table, manufacturer):
    """
    Question: What is the average amount of games in stock of a given manufacturer?

    Args:
        table (list): data table to work on
        manufacturer (str): Name of manufacturer

    Returns:
         number
    """

    dictionary = {}
    for element in table:
        if element[2].casefold() in dictionary.keys():
            dictionary[element[2].casefold()] += 1
        if element[2].casefold() not in dictionary.keys():
            dictionary[element[2].casefold()] = 1
    
    dictionary_average = {}
    for element in table:
        if element[2].casefold() in dictionary_average.keys():
            dictionary_average[element[2].casefold()] += int(element[4])
        if element[2].casefold() not in dictionary_average.keys():
            dictionary_average[element[2].casefold()] = int(element[4])

    manufacturer = manufacturer.casefold()
    if manufacturer not in dictionary.keys():
        return False

    average = dictionary_average[manufacturer] / dictionary[manufacturer]

    return average