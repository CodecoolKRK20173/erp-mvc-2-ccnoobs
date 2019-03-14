""" Human resources module

Data table structure:
    * id (string): Unique and random generated identifier
        at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letters)
    * name (string)
    * birth_year (number)
"""

# everything you'll need is imported:
from model import data_manager
from model import common


def get_hr_table_from_file():
    return data_manager.get_table_from_file('model/hr/persons.csv')

def add(table, record):
    table = common.add(table,record)
    return table


def update(table, id_, record):
    table = common.update(table, id_, record)
    return table


def remove(table, id_):
    table = common.remove(table, id_)
    return table


# special functions:
# ------------------

def get_oldest_person(table):
    """
    Question: Who is the oldest person?

    Args:
        table (list): data table to work on

    Returns:
        list: A list of strings (name or names if there are two more with the same value)
    """

    # your code

    oldest_year = int(table[0][2])
    oldest_names = []

    for element in table:
        element[2] = int(element[2])
        year_of_person = element[2]
        if year_of_person < oldest_year:
            oldest_year = year_of_person

    for element in table:
        year_of_person = element[2]
        if oldest_year == year_of_person:
            oldest_names.append(element[1])

    return oldest_names



def get_persons_closest_to_average(table):
    """
    Question: Who is the closest to the average age?

    Args:
        table (list): data table to work on

    Returns:
        list: list of strings (name or names if there are two more with the same value)
    """


    list_of_years = []
        
    for element in table:
        element[2] = int(element[2])
        list_of_years.append(element[2])

    numbers_years = int(len(list_of_years))

    suma = 0
    for i in range(numbers_years):
        suma = suma + list_of_years[i]
    
    average = suma/numbers_years
    average = int(average)

    the_closest = min(list_of_years, key=lambda x:abs(x-average))

    the_closest_name = []
    for element in table:
        element[2] = int(element[2])
        the_closest = int(the_closest)
        if element[2] == the_closest:
            the_closest_name.append(element[1])
            
    return the_closest_name
