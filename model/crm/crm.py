""" Customer Relationship Management (CRM) module

Data table structure:
    * id (string): Unique and random generated identifier
        at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letters)
    * name (string)
    * email (string)
    * subscribed (int): Is she/he subscribed to the newsletter? 1/0 = yes/no
"""

# everything you'll need is imported:
from model import data_manager
from model import common

def add(table, record):
    table.append(record)
    return table


def update(table, id_, record):
    table[int(id_)] = record
    return table


def remove(table, id_):
    del table[int(id_)]
    return table


# special functions:
# ------------------

def get_longest_name_id(table):
    """
        Question: What is the id of the customer with the longest name?

        Args:
            table (list): data table to work on

        Returns:
            string: id of the longest name (if there are more than one, return
                the last by alphabetical order of the names)
        """


    max_lengh = len(table[0][1])
    max_id = table[0][0]
    max_name = table[0][1]
    for element in table:
        element_lengh_name = len(element[1])
        if  element_lengh_name > max_lengh:
            max_lengh = element_lengh_name
            max_id = element[0]
            max_name = element[1]
        elif element_lengh_name == max_lengh:
            if max_name < element[1]:
                max_lengh = element_lengh_name
                max_id = element[0]
                max_name = element[1]
    return max_id




# the question: Which customers has subscribed to the newsletter?
# return type: list of strings (where string is like email+separator+name, separator=";")
def get_subscribed_emails(table):
    """
        Question: Which customers has subscribed to the newsletter?

        Args:
            table (list): data table to work on

        Returns:
            list: list of strings (where a string is like "email;name")
        """


    list_of_users = []
    subscription = table[3]

    for element in table:
        if subscription == 1:
            list_of_users.append(element)
            list_of_emails = list_of_users[2]
    return list_of_emails 


