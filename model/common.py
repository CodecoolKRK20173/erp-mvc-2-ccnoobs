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
    table.append(record)
    return table


def update(table, id_, record):
    table[int(id_)] = record

    return table
    # your code


def remove(table, id_):
    del table[int(id_)]

    return table


def swap_position(list_to_sort, first_element_index, second_element_index): #swap position od two elements, first_element_index with second_element_index
    temporary_list = list_to_sort[second_element_index]
    list_to_sort[second_element_index] = list_to_sort[first_element_index]
    list_to_sort[first_element_index] = temporary_list
    return list_to_sort


def bubble_sort(list_to_sort, reverse=False, index_of_element_in_list_of_lists_by_which_you_want_to_sort=1, sort_by_lenght_of_element=False):
    for element in range(0,len(list_to_sort)):
        for iterate in range(0, len(list_to_sort)-1):
            if sort_by_lenght_of_element == False:
                first_element = list_to_sort[iterate][index_of_element_in_list_of_lists_by_which_you_want_to_sort]
                second_element = list_to_sort[iterate+1][index_of_element_in_list_of_lists_by_which_you_want_to_sort]
            elif sort_by_lenght_of_element == True:
                first_element = len(list_to_sort[iterate][index_of_element_in_list_of_lists_by_which_you_want_to_sort])
                second_element = len(list_to_sort[iterate+1][index_of_element_in_list_of_lists_by_which_you_want_to_sort])
                if reverse == False:
                    if first_element > second_element:
                        list_to_sort = swap_position(list_to_sort, iterate, iterate+1)
                if reverse == True:
                    if first_element < second_element:
                        list_to_sort = swap_position(list_to_sort, iterate, iterate+1)
    return list_to_sort