# everything you'll need is imported:
from view import terminal_view
from model.crm import crm
from controller import common

def run():
    """
    Starts this module and displays its menu.
     * User can access default special features from here.
     * User can go back to main menu from here.

    Returns:
        None
    """

    table = crm.get_crm_table_from_file()
    title_list = ["ID", "Name", "E-mail", "Subscribed"]
    options = ["View records",
               "Add record",
               "Remove record",
               "Update record",
               "ID releated with the longest name",
               "The emails with subscription"]


    choice = None
    while choice != "0":
        choice = terminal_view.get_choice_inner_menu(options, "Customer Relationship Management manager")
        if choice == "1":
            terminal_view.print_table(table, title_list)
        elif choice == "2":
            record = terminal_view.get_inputs(title_list[1::],"Please provide new item data")
            table = crm.add(table, record)
        elif choice == "3":
            id_to_delete_table = terminal_view.get_inputs(["ID"],"Item to delete")
            id_to_delete = id_to_delete_table[0]
            table = crm.remove(table, id_to_delete)
        elif choice == "4":
            records = terminal_view.get_inputs(title_list,"Edit item")
            record_id = records[0]
            table = crm.update(table, record_id, records)
        elif choice == "5":
            longest_name_id = crm.get_longest_name_id(table)
            terminal_view.print_result(longest_name_id, "The longest name ID: ")
        elif choice == "6":
            subscribed_emails = crm.get_subscribed_emails(table)
            terminal_view.print_result(subscribed_emails,"The subscribed emails: ")
        elif choice != "0":
            terminal_view.print_error_message("There is no such choice.")

