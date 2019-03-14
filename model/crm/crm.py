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


def get_crm_table_from_file():
    return data_manager.get_table_from_file('model/crm/customers.csv')


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


    list_of_emails = []
    
    for element in table:
        element[3] = int(element[3])
        subscription = int(element[3])
        if subscription == 1:
            list_of_emails.append(element[2] + ";" + element[1])
    

    return list_of_emails 


def proposition_subscription(table):

    list_of_names = []
    
    for element in table:
        element[3] = int(element[3])
        subscription = int(element[3])
        if subscription == 0:
            list_of_names.append(element[1])

    offer = str(list_of_names) + "\n" + "If You are interested our subscription, please contact with us via e-mail."

    return offer