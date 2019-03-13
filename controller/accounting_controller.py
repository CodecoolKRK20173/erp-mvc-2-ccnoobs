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
    table = accounting.get_accounting_table_from_file()
    title_list = ["ID", "Month", "Day", "Year", "Type","Amount"]
    options = ["View records",
               "Add record",
               "Remove record",
               "Update record",
               "Which year has the highest profit?",
               "What is the average (per item) profit in a given year?"]

    choice = None
    while choice != "0":
        choice = terminal_view.get_choice_inner_menu(options, "Accounting manager")
        if choice == "1":
            terminal_view.print_table(table, title_list)
        elif choice == "2":
            record = terminal_view.get_inputs(title_list[1::],"Please provide new item data")
            table = accounting.add(table, record)
        elif choice == "3":
            id_to_delete_table = terminal_view.get_inputs(["ID"],"Item to delete")
            id_to_delete = id_to_delete_table[0]
            table = accounting.remove(table, id_to_delete)
        elif choice == "4":
            records = terminal_view.get_inputs(title_list,"Edit item")
            record_id = records[0]
            table = accounting.update(table, record_id, records)
        elif choice == "5":
            max_year = accounting.which_year_max(table)
            terminal_view.print_result(max_year, "Year of the highest profit")
        elif choice == "6":
            year_input = terminal_view.get_inputs(["Year"],"Average (per item) profit in a given year")
            year = year_input[0]
            avg_amount = accounting.avg_amount(table, year)
            terminal_view.print_result(avg_amount,"Avarage profit in {}".format(year))
        elif choice != "0":
            terminal_view.print_error_message("There is no such choice.")
