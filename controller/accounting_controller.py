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
    title_list = ["ID", "Month".upper(), "Day".upper(), "Year".upper(), "Type".upper(),"Amount".upper()]
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
            record_is_not_correct = True
            while record_is_not_correct:
                record = terminal_view.get_inputs(title_list[1::],"Please provide new item data")
                record_is_not_correct = False

                if record[0].isdigit():
                    if int(record[0]) < 1 or int(record[0]) > 12:
                        terminal_view.print_error_message("Incorrect month")
                        record_is_not_correct = True
                else:
                    terminal_view.print_error_message("Month should be natural number")
                    record_is_not_correct = True

                if record[1].isdigit():
                    if int(record[1]) < 1 or int(record[1]) > 31:
                        terminal_view.print_error_message("Incorrect day")
                        record_is_not_correct = True
                else:
                    terminal_view.print_error_message("Day should be natural number")
                    record_is_not_correct = True

                if not record[2].isdigit():
                    terminal_view.print_error_message("Year should be natural number")
                    record_is_not_correct = True

                if not record[4].isdigit():
                    terminal_view.print_error_message("Durability should be natural number")
                    record_is_not_correct = True

                if record_is_not_correct == False:
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
