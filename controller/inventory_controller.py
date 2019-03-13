# everything you'll need is imported:
from view import terminal_view
from model.inventory import inventory
from controller import common

def run():
    """
    Starts this module and displays its menu.
     * User can access default special features from here.
     * User can go back to main menu from here.

    Returns:
        None
    """

def run():
    """
    Starts this module and displays its menu.
     * User can access default special features from here.
     * User can go back to main menu from here.

    Returns:
        None
    """
    table = inventory.get_inventory_table_from_file()
    title_list = ["ID", "Name", "Manufacturer", "Year", "Durability"]
    options = ["View records",
               "Add record",
               "Remove record",
               "Update record",
               "Which items have not exceeded their durability yet?",
               "What are the average durability times for each manufacturer?"]

    choice = None
    while choice != "0":
        choice = terminal_view.get_choice_inner_menu(options, "Inventory manager")
        if choice == "1":
            terminal_view.print_table(table, title_list)
        elif choice == "2":
            record = terminal_view.get_inputs(title_list[1::],"Please provide new item data")
            table = inventory.add(table, record)
        elif choice == "3":
            id_to_delete_table = terminal_view.get_inputs(["ID"],"Item to delete")
            id_to_delete = id_to_delete_table[0]
            table = inventory.remove(table, id_to_delete)
        elif choice == "4":
            records = terminal_view.get_inputs(title_list,"Edit item")
            record_id = records[0]
            table = inventory.update(table, record_id, records)
        elif choice == "5":
            available_items = inventory.get_available_items(table)
            terminal_view.print_result(available_items, "Available items")
        elif choice == "6":
            average_durability = inventory.get_average_durability_by_manufacturers(table)
            terminal_view.print_result(average_durability, "Average durability by manufacturer")
        elif choice != "0":
            terminal_view.print_error_message("There is no such choice.")

