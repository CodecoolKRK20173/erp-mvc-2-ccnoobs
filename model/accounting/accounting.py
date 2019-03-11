""" Accounting module

Data table structure:
    * id (string): Unique and random generated identifier
        at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letters)
    * month (number): Month of the transaction
    * day (number): Day of the transaction
    * year (number): Year of the transaction
    * type (string): in = income, out = outflow
    * amount (int): amount of transaction in USD
"""

# everything you'll need is imported:
from model import data_manager
from model import common



def add(table, record):
    """
    Add new record to table

    Args:
        table (list): table to add new record to
        record (list): new record

    Returns:
        list: Table with a new record
    """
    # your code
    table = common.add(table,record)

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
    # your code

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
    # your code

    return table


# special functions:
# ------------------

def which_year_max(table):
    """
    Question: Which year has the highest profit? (profit = in - out)

    Args:
        table (list): data table to work on

    Returns:
        number
    """
    max_income_year = int(table[0][3])
    max_income = float(table[0][5])

    for entry in table:
        entry_income = float(entry[5])
        if entry_income > max_income:
            entry_year = int(entry[3])
            max_income_year = entry_year
            max_income = entry_income

    return max_income_year


def avg_amount(table, year):
    """
    Question: What is the average (per item) profit in a given year? [(profit)/(items count)]

    Args:
        table (list): data table to work on
        year (number)

    Returns:
        number
    """
    item_count = 0
    total_profit = 0
    for entry in table:
        entry_year = int(entry[3])
        if entry_year == year:
            item_count += 1
            entry_type = entry[4]
            entry_profit = int(entry[5])
            if entry_type == "in":
                total_profit += entry_profit
            elif entry_type == "out":
                total_profit -= entry_profit

    avg_profit = total_profit / item_count

    return avg_profit

