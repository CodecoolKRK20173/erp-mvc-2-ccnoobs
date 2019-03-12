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
    table_sorted_by_price = table[:]
    table_sorted_by_price = common.bubble_sort(table_sorted_by_price, False, 2, False)
    if table_sorted_by_price[0][2] == table_sorted_by_price[1][2]:
        table = common.bubble_sort(table,False,1,False)
        return table[-1][0]
    return table_sorted_by_price[0][0]

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

    years_range = list(range((int(year_from)+1), int(year_to)))
    months_range = list(range((int(month_from)+1), int(month_to)))
    days_range = list(range(int(day_from), int(day_to)+1))
    days_in_range_by_year = len(years_range)*365
    
    year = 365
    month = 31



    filtered_table = []
    filtered_by_years_and_months = []
    for item in range(len(table)):
        if table[item][5] in years_range:
            if table[item][3] in months_range:
                filtered_by_years_and_months.append(table[item])



                if table[item][4] in days_range:
                    filtered_table.append(table[item])
    return filtered_table
 