""" Inventory module

Data table structure:
    * id (string): Unique and random generated identifier
        at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letters)
    * name (string): Name of item
    * manufacturer (string)
    * purchase_year (number): Year of purchase
    * durability (number): Years it can be used
"""

# everything you'll need is imported:
from model import data_manager
from model import common


def get_inventory_table_from_file():
    return data_manager.get_table_from_file('model/inventory/inventory.csv')


def add(table, record):
    """
    Add new record to table

    Args:
        table (list): table to add new record to
        record (list): new record

    Returns:
        list: Table with a new record
    """
    record[3], record[2] = int(record[3]), int(record[2])
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
    record[3], record[2] = int(record[3]), int(record[2])
    table = common.update(table, id_, record)

    return table


# special functions:
# ------------------

def get_available_items(table):
    """
    Question: Which items have not exceeded their durability yet?

    Args:
        table (list): data table to work on

    Returns:
        list: list of lists (the inner list contains the whole row with their actual data types)
    """
    avaiable_items = []
    for entry in table:
        entry[3] = int(entry[3])
        entry[4] = int(entry[4])
        entry_year = entry[3]
        entry_durability = entry[4]
        entry_age = 2017 - entry_year
        if entry_age <= entry_durability:
            avaiable_items.append(entry)
    return avaiable_items


def get_average_durability_by_manufacturers(table):
    """
    Question: What are the average durability times for each manufacturer?

    Args:
        table (list): data table to work on

    Returns:
        dict: a dictionary with this structure: { [manufacturer] : [avg] }
    """
    avg_durability_dict= {}

    for entry in table:
        entry_manufacturer = entry[2]
        entry_durability = int(entry[4])
        if entry_manufacturer in avg_durability_dict:
            avg_durability_dict[entry_manufacturer] += entry_durability
        else:
            avg_durability_dict[entry_manufacturer] = entry_durability

    for key in avg_durability_dict:
        key_count = 0
        for entry in table:
            if key == entry[2]:
                key_count += 1
        if key_count == 0:
            key_count = 1
        avg_durability_dict[key] = int(avg_durability_dict[key]) / key_count

    return avg_durability_dict


