# everything you'll need is imported:
from model.store import store
from view import terminal_view
from controller import common

""" Store module

Data table structure:
    * id (string): Unique and random generated identifier
        at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letters)
    * title (string): Title of the game
    * manufacturer (string)
    * price (number): Price in dollars
    * in_stock (number)
"""


def run():
    """
    Starts this module and displays its menu.
     * User can access default special features from here.
     * User can go back to main menu from here.

    Returns:
        None
    """

    table = store.get_store_table_from_file()
    title_list = ["ID", "Title", "Manufacturer", "Price [$]", "In stock"]
    options = ["View records",
               "Add record",
               "Remove record",
               "Update record",
               "How many different kinds of game are available of each manufacturer?",
               "What is the average amount of games in stock of a given manufacturer?"]

    choice = None
    while choice != "0":
        choice = terminal_view.get_choice_inner_menu(options, "Store manager")
        if choice == "1":
            terminal_view.print_table(table, title_list)
        elif choice == "2":
            record = terminal_view.get_inputs(
                title_list[1::], "Please provide new item data")
            table = store.add(table, record)
        elif choice == "3":
            id_to_delete_table = terminal_view.get_inputs(
                ["ID"], "Item to delete")
            id_to_delete = id_to_delete_table[0]
            table = store.remove(table, id_to_delete)
        elif choice == "4":
            records = terminal_view.get_inputs(title_list, "Edit item")
            record_id = records[0]
            table = store.update(table, record_id, records)
        elif choice == "5":
            amount_of_games = store.get_counts_by_manufacturers(table)
            list_from_dict = amount_of_games.items()
            manufacturer_count = ["MANUFACTURERS","GAMES"]
            terminal_view.print_table(list_from_dict, manufacturer_count)
        elif choice == "6":
            choose_manufacturer = terminal_view.get_inputs(["Manufacturer"], "For which manufacturer would you like to check the average amount of games in stock?")
            manufacturer = choose_manufacturer[0]
            avg_amount = store.get_average_by_manufacturer(table, manufacturer)
            while avg_amount == False:
                choose_manufacturer = terminal_view.get_inputs(["Put existing manufacturer"], "No such manufacturer in list:")
                manufacturer = choose_manufacturer[0]
                avg_amount = store.get_average_by_manufacturer(table, manufacturer)
            title_two = ["Manufacturer", "Average amount of games in stock"]
            table_two = [[manufacturer,str(avg_amount)]]
            terminal_view.print_table(table_two, title_two)
        elif choice != "0":
            terminal_view.print_error_message("There is no such choice.")
