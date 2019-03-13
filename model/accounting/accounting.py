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


def get_accounting_table_from_file():
    return data_manager.get_table_from_file('model/accounting/items.csv')


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
    record[0], record[1], record[2] = int(record[0]), int(record[1]), int(record[2])
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
    record[0], record[1], record[2] = int(record[0]), int(record[1]), int(record[2])
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
    years_profit = {}
    for entry in table:
        entry[1], entry[2], entry[3], entry[5] = int(entry[1]), int(entry[2]), int(entry[3]), int(entry[5])
        entry_year = entry[3]
        entry_type = entry[4]
        entry_ammount = entry[5]
        if entry_year in years_profit:
            if entry_type == "out":
                years_profit[entry_year] -= entry_ammount
            elif entry_type == "in":
                years_profit[entry_year] += entry_ammount
        else:
            if entry_type == "out":
                years_profit[entry_year] = -1 * entry_ammount
            elif entry_type == "in":
                years_profit[entry_year] = entry_ammount
    max_income_year = max(years_profit, key=years_profit.get)

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
    year = int(year)
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
    if item_count == 0:
        item_count = 1
    avg_profit = total_profit / item_count

    return avg_profit

