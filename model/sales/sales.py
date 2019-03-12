""" Sales module

Data table structure:
    * id (string): Unique and random generated identifier
        at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letters)
    * title (string): Title of the game sold
    * price (number): The actual sale price in USD
    * month (number): Month of the sale
    * day (number): Day of the sale
    * year (number): Year of the sale
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

def get_lowest_price_item_id(table):
    """
    Question: What is the id of the item that was sold for the lowest price?
    if there are more than one item at the lowest price, return the last item by alphabetical order of the title

    Args:
        table (list): data table to work on

    Returns:
         string: id
    """
    lowest_price = int(table[0][2])
    lowest_price_title = table[0][1]
    lowest_price_id = table[0][0]

    for element in table:
        element[2] = int(element[2])
        element_price = element[2]
        if element_price < lowest_price:
            lowest_price = element_price
            lowest_price_title = element[1]
            lowest_price_id = element[0]

    for element in table:
        element_price = element[2]
        element_title = element[1]
        element_id = element[0]
        if lowest_price == element_price:
            if element_title > lowest_price_title:
                lowest_price = element_price
                lowest_price_title = element[1]
                lowest_price_id = element[0]
    
    return lowest_price_id

def get_items_sold_between(table, month_from, day_from, year_from, month_to, day_to, year_to):
    """
    Question: Which items are sold between two given dates? (from_date < sale_date < to_date)

    Args:
        table (list): data table to work on
        month_from (int)
        day_from (int)
        year_from (int)
        month_to (int)
        day_to (int)
        year_to (int)

    Returns:
        list: list of lists (the filtered table)
    """

    time_range_from = (int(year_from) * 365) + (int(month_from) * 31) + int(day_from)
    time_range_to = (int(year_to) * 365) + (int(month_to) * 31) + int(day_to)
    time_range = list(range(time_range_from + 1, time_range_to))

    filtered_table = []
    for item in range(len(table)):
        if ((int(table[item][5]) * 365) + (int(table[item][3]) * 31) + int(table[item][4])) in time_range:
            filtered_table.append(table[item])
    for entry in filtered_table:
        entry[2] = int(entry[2])
        entry[5] = int(entry[5])
        entry[3] = int(entry[3])
        entry[4] = int(entry[4])
    return filtered_table
 