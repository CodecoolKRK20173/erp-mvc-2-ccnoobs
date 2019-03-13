# everything you'll need is imported:
from view import terminal_view
from model.hr import hr
from controller import common

def run():
    """
    Starts this module and displays its menu.
     * User can access default special features from here.
     * User can go back to main menu from here.

    Returns:
        None
    """
    table = hr.get_hr_table_from_file()
    title_list = ["ID", "Name", "BirthYear", "Year"]
    options = ["View records",
               "Add record",
               "Remove record",
               "Update record",
               "Which person is the oldest?",
               "Which person is the closet to average age?"]


    choice = None
    while choice != "0":
        choice = terminal_view.get_choice_inner_menu(options, "HR manager")
        if choice == "1":
            terminal_view.print_table(table, title_list)
        elif choice == "2":
            record = terminal_view.get_inputs(title_list[1::],"Please provide new item data")
            table = hr.add(table, record)
        elif choice == "3":
            id_to_delete_table = terminal_view.get_inputs(["ID"],"Item to delete")
            id_to_delete = id_to_delete_table[0]
            table = hr.remove(table, id_to_delete)
        elif choice == "4":
            records = terminal_view.get_inputs(title_list,"Edit item")
            record_id = records[0]
            table = hr.update(table, record_id, records)
        elif choice == "5":
            oldest_person = hr.get_oldest_person(table)
            terminal_view.print_result(oldest_person, "The oldest person: ")
        elif choice == "6":
            closest_to_average = hr.get_persons_closest_to_average(table)
            terminal_view.print_result(closest_to_average,"The closest to average is: ")
        elif choice != "0":
            terminal_view.print_error_message("There is no such choice.")


