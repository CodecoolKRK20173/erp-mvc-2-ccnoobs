# everything you'll need is imported:
from view import terminal_view
from model.sales import sales
from controller import common

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

def run():
    """
    Starts this module and displays its menu.
     * User can access default special features from here.
     * User can go back to main menu from here.

    Returns:
        None
    """

    table = sales.get_sales_table_from_file()
    title_list = ["ID", "Title","Price", "Month", "Day", "Year"]
    options = ["View records",
               "Add record",
               "Remove record",
               "Update record",
               "What is the id of the item that was sold for the lowest price?",
               "Which items are sold between two given dates?"]

    choice = None
    while choice != "0":
        choice = terminal_view.get_choice_inner_menu(options, "Sales manager")
        if choice == "1":
            terminal_view.print_table(table, title_list)
        elif choice == "2":
            record = terminal_view.get_inputs(title_list[1::],"Please provide new item data")
            table = sales.add(table, record)
        elif choice == "3":
            id_to_delete_table = terminal_view.get_inputs(["ID"],"Item to delete")
            id_to_delete = id_to_delete_table[0]
            table = sales.remove(table, id_to_delete)
        elif choice == "4":
            records = terminal_view.get_inputs(title_list,"Edit item")
            record_id = records[0]
            table = sales.update(table, record_id, records)
        elif choice == "5":
            lowest_price = sales.get_lowest_price_item_id(table)
            description = ["ID of item that was sold for the lowest price:"]
            value = [[lowest_price]]
            terminal_view.print_table(value, description)
        elif choice == "6":
            day_from_input = terminal_view.get_inputs(["Day from"],"")
            while not day_from_input[0].isdigit():
                day_from_input = terminal_view.get_inputs(["Your input is not digit. Choose correct day from range 1-31"],"")
            while day_from_input[0].isdigit():
                while int(day_from_input[0]) > 31 or int(day_from_input[0]) < 1:
                    day_from_input = terminal_view.get_inputs(["Choose correct day from range 1-31"],"")
                    while not day_from_input[0].isdigit():
                        day_from_input = terminal_view.get_inputs(["Your input is not digit. Choose correct day from range 1-31"],"")
                break
            day_from = day_from_input[0]
            
            month_from_input = terminal_view.get_inputs(["Month from"],"")
            while not month_from_input[0].isdigit():
                month_from_input = terminal_view.get_inputs(["Your input is not digit. Choose correct month from range 1-12"],"")
            while month_from_input[0].isdigit():            
                while not int(month_from_input[0]) < 13 or not int(month_from_input[0]) > 0:
                    month_from_input = terminal_view.get_inputs(["Choose correct month from range 1-12"],"")   
                    while not month_from_input[0].isdigit():
                        month_from_input = terminal_view.get_inputs(["Your input is not digit. Choose correct month from range 1-12"],"")
                break 
            month_from = month_from_input[0]
            
            year_from_input = terminal_view.get_inputs(["Year from"],"")
            while not year_from_input[0].isdigit():
                year_from_input = terminal_view.get_inputs(["Your input is not digit. Choose correct year"],"")
            while year_from_input[0].isdigit():
                while not int(year_from_input[0]) > 0:
                    year_from_input = terminal_view.get_inputs(["Choose correct year"],"")
                    while not year_from_input[0].isdigit():
                        year_from_input = terminal_view.get_inputs(["Your input is not digit. Choose correct year"],"")
                break
            year_from = year_from_input[0]
            
            day_to_input = terminal_view.get_inputs(["Day to"],"")
            while not day_to_input[0].isdigit():
                day_to_input = terminal_view.get_inputs(["Your input is not digit. Choose correct day from range 1-31"],"")
            while day_to_input[0].isdigit():
                while not int(day_to_input[0]) < 32 or not int(day_to_input[0]) > 0:
                    day_to_input = terminal_view.get_inputs(["Choose correct day from range 1-31"],"")
                    while not day_to_input[0].isdigit():
                        day_to_input = terminal_view.get_inputs(["Your input is not digit. Choose correct day from range 1-31"],"")
                break
            day_to = day_to_input[0]
            
            month_to_input = terminal_view.get_inputs(["Month to"],"")
            while not month_to_input[0].isdigit():
                month_to_input = terminal_view.get_inputs(["Your input is not digit. Choose correct month from range 1-12"],"") 
            while month_to_input[0].isdigit():
                while not int(month_to_input[0]) < 13 or not int(month_to_input[0]) > 0:
                    month_to_input = terminal_view.get_inputs(["Choose correct month from range 1-12"],"")
                    while not month_to_input[0].isdigit():
                        month_to_input = terminal_view.get_inputs(["Your input is not digit. Choose correct month from range 1-12"],"") 
                break
            month_to = month_to_input[0]
            
            year_to_input = terminal_view.get_inputs(["Year to"],"")
            while not year_to_input[0].isdigit():
                year_to_input = terminal_view.get_inputs(["Your input is not digit. Choose correct year"],"")
            while year_to_input[0].isdigit():
                while not int(year_to_input[0]) > 0 or not int(year_to_input[0]) > int(year_from):
                    year_to_input = terminal_view.get_inputs(["You can't choose year before 'Year from' value. Put correct year"],"")
                    while not year_to_input[0].isdigit():
                        year_to_input = terminal_view.get_inputs(["Your input is not digit. Choose correct year"],"")
                break
            year_to = year_to_input[0]

            items_sold_by_date = sales.get_items_sold_between(table, month_from, day_from, year_from, month_to, day_to, year_to)
            terminal_view.print_table(items_sold_by_date,title_list)
        elif choice != "0":
            terminal_view.print_error_message("There is no such choice.")
