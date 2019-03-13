# everything you'll need is imported:
from view import terminal_view
from model.accounting import accounting
from controller import common

def run():
    """
    Starts this module and displays its menu.
     * User can access default special features from here.
     * User can go back to main menu from here.

    Returns:
        None
    """

    options = ["Add record",
               "Remove record",
               "Update record",
               "Which year has the highest profit?",
               "What is the average (per item) profit in a given year?"]

    choice = None
    while choice != "0":
        choice = terminal_view.get_choice_inner_menu(options, "Accounting manager")
        if choice == "1":
            store_controller.run()
        elif choice == "2":
            hr_controller.run()
        elif choice == "3":
            inventory_controller.run()
        elif choice == "4":
            accounting_controller.run()
        elif choice == "5":
            sales_controller.run()
        elif choice == "6":
            crm_controller.run()
        elif choice != "0":
            terminal_view.print_error_message("There is no such choice.")
