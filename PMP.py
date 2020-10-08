
"""
Program prompts user for pool size and desired chemical
change, then calculates the necessary chemicals to enact change
"""
from pyfiglet import figlet_format
from datetime import date
from prettytable import PrettyTable
import csv


# daily_tests stores  the chemical readings for that day to be passed to other functions
daily_tests = {}


def get_test_results():
    """
    get_test_results prompts user to enter the results of their daily tests and records them to daily_tests
    """
    print(f"Now, let's enter the results of your chemical tests.")

    daily_tests["total_chlorine"] = float(
        input("What was your total chlorine today? "))
    daily_tests["free_chlorine"] = float(
        input("OK. What was your free chlorine today? "))
    daily_tests["combined_chlorine"] = round(
        daily_tests["total_chlorine"] - daily_tests["free_chlorine"], 2)
    daily_tests["total_alkalinity"] = float(
        input("What was your total alkalinity reading? "))
    daily_tests["calcium_hardness"] = float(
        input("All right. What was your calcium hardness? "))
    daily_tests["pH"] = float(input("OK. What was your pool's pH today? "))
    daily_tests["temperatute"] = float(
        input("What was your pool's temperature? "))
    daily_tests["stabilizer"] = float(
        input("Finally, what was your cyanuric acid reading today?"))


def export_test_results():
    fields = ["Total Chlorine", "Free Chlorine", "Combined Chlorine", "Total Alkalinity", "Calcium Hardness",
        "pH", "Temperature", "Stabilizer"]
    print("\n\nCreating CSV file...\n\n")
    with open ("test_results.csv", 'a') as results_file:
        writer = csv.DictWriter(results_file, fieldnames = fields)
        writer.writeheader(fields)
        writer.writerow(daily_tests)
    print("Finished.")


def increase_chlorine(factor):
    """
    increase_chlorine prompts the user for the desired change
    in chlorine then calculates and prints the ncessary chemical application
    """
    change = 0
    amount_to_add = 0

    change = int(
        input("By how much would you like to increase the chlorine (in PPM)? "))

    while change > 10 or change < 1:
        change = int(input("Please enter a number between 1 and 10: "))

    if change < 5:
        amount_to_add = ((change / 1) * 2 * factor) / 16
        print(f"To increase your chlorine level by {change} PPM, you should add {amount_to_add / 16} pound(s) of calcium hypochlorite")

    elif change < 10:
        amount_to_add = ((change / 5) * 10 * factor) / 16
        print(f"To increase your chlorine level by {change} PPM, you should add {amount_to_add / 16} pound(s) of calcium hypochlorite")

    else:
        print(f"To increase your chlorine level by {change} PPM, you should add {amount_to_add / 16} pound(s) of calcium hypochlorite")


def neutralize_chlorine(factor):
    """
    neutralize_chlorine calculates the the amount of sodium thiosulfate to add to decrease
    chlorine. Results are printed to the console.
    """
    change = 0
    amount_to_add = 0

    change = int(
        input("By how much would you like to decrease the chlorine (in PPM)? "))

    while change > 10 or change < 1:
        change = int(input("Please enter a number between 1 and 10: "))

    if change < 5:
        amount_to_add = change * 2.6 * factor
        print(f"To decrease your chlorine level by {change} PPM, you should add {amount_to_add / 16} pound(s) of sodium thiosulfate")
    elif change < 10:
        amount_to_add = (change / 5) * 13 * factor
        print(f"To decrease your chlorine level by {change} PPM, you should add {amount_to_add / 16} pound(s) of sodium thiosulfate")
    else:
        amount_to_add = change * 26 * factor
        print(f"To decrease your chlorine level by {change} PPM, you should add {amount_to_add / 16} pound(s) of sodium thiosulfate")


def increase_TA(factor):
    """ 
    increase_TA calculates te amount of sodium bicarbonate to add to increase the
    total alkalinity. Results are printed to the console.
    """
    change = 0
    amount_to_add = 0

    change = int(
        input("By how much would you like to increase the total alkalinity (in PPM)? "))

    while change < 10:
        change = int(input("Please enter a number greater than 10: "))

    if change < 30:
        amount_to_add = (change / 10) * 1.4 * factor
        print(f"To increase your total alkalinity by {change} PPM, you should add {amount_to_add} pound(s) of sodium bicarbonate")
    elif change < 50:
        amount_to_add = (change / 30) * 4.2 * factor
        print(f"To increase your total alkalinity by {change} PPM, you should add {amount_to_add} pound(s) of sodium bicarbonate")
    else:
        amount_to_add = (change / 26) * 7.0 * factor
        print(f"To decrease your total alkalinity by {change} PPM, you should add {amount_to_add} pound(s) of sodium bicarbonate")


def decrease_TA(factor):
    """
    decrease_TA calculates how to decrease the total alkalinity
    """
    change = 0
    amount_to_add = 0

    change = int(
        input("By how much would you like to decrease the total alkalinity (in PPM)? "))

    while change < 10:
        change = int(input("Please enter a number greater than 10: "))

    if change < 30:
        amount_to_add = (change / 10) * 26 * factor
        print(f"To decrease your total alkalinity by {change} PPM, you should add {amount_to_add / 128} gallons of muriatic acid")
    elif change < 50:
        amount_to_add = (change / 30) * 76.8 * factor
        print(f"To decrease your total alkalinity by {change} PPM, you should add {amount_to_add / 128} gallons of muriatic acid")
    else:
        amount_to_add = (change / 50) * 1.0 * factor
        print(f"To decrease your total alkalinity by {change} PPM, you should add {amount_to_add / 128} gallons of muriatic acid")




def increase_CH(factor):
    """
    increase_CH calculates how to increase calcium hardness
    """
    change = 0
    amount_to_add = 0

    change = int(
        input("By how much would you like to increase the calcium hardness (in PPM)? "))

    while change < 10:
        change = int(input("Please enter a number greater than 10: "))

    if change < 30:
        amount_to_add = (change / 10) * 1.2 * factor
        print(f"To increase your calcium hardness by {change} PPM, you should add {amount_to_add} pounds of calcium chloride (77%)")
    elif change < 50:
        amount_to_add = (change / 30) * 3.6 * factor
        print(f"To increase your calcium hardness by {change} PPM, you should add {amount_to_add} pounds of calcium chloride (77%)")
    else:
        amount_to_add = (change / 50) * 6.0 * factor
        print(f"To increase your calcium hardness by {change} PPM, you should add {amount_to_add} pounds of calcium chloride (77%)")


def increase_stabilizer(factor):
    """
    increase_stabilizer calculates the amount of cyanuric acid to add
    """
    change = 0
    amount_to_add = 0

    change = int(
        input("By how much would you like to increase the stabilizer(in PPM)? "))

    while change < 10:
        change = int(input("Please enter a number greater than 10: "))

    if change < 30:
        amount_to_add = (change / 10) * 13 * factor
        print(f"To increase your stabilizer by {change} PPM, you should add ")
        if amount > 8:
            print(f"{amount_to_add / 16} pounds of cyanuric acid.")
        else:
            print(f"{amount_to_add} ounces of cyanuric acid.")
    elif change < 50:
        amount_to_add = (change / 30) * 2.5 * factor
        print(f"To increase your stabilizer by {change} PPM, you should add {amount_to_add} pounds of cyanuric acid")
    else:
        amount_to_add = (change / 50) * 4.1 * factor
        print(f"To increase your stabilizer by {change} PPM, you should add {amount_to_add} pounds of cyanuric acid")


def calculate_SI(daily_tests):
    """
    caculate_SI calculates the saturation index of the user's pool
    """
    tds = 12.1

    # determine temperature factor
    if daily_tests["temperature"] < 35:
        tf = 0.0
    elif daily_tests["temperature"] < 42:
        tf = 0.1
    elif daily_tests["temperature"] < 50:
        tf = 0.2
    elif daily_tests["temperature"] < 57:
        tf = 0.3
    elif daily_tests["temperature"] < 64:
        tf = 0.4
    elif daily_tests["temperature"] < 72:
        tf = 0.5
    elif daily_tests["temperature"] < 81:
        tf = 0.6
    elif daily_tests["temperature"] < 90:
        tf = 0.7
    elif daily_tests["temperature"] < 105:
        tf = 0.8
    else:
        tf = 0.9

    # determine calcium hardness factor
    if daily_tests["calcium_hardness"] < 37:
        cf = 0.1
    elif daily_tests["calcium_hardness"] < 64:
        cf = 1.3
    elif daily_tests["calcium_hardness"] < 88:
        cf = 1.5
    elif daily_tests["calcium_hardness"] < 114:
        cf = 1.6
    elif daily_tests["calcium_hardness"] < 139:
        cf = 1.7
    elif daily_tests["calcium_hardness"] < 164:
        cf = 1.8
    elif daily_tests["calcium_hardness"] < 226:
        cf = 1.9
    elif daily_tests["calcium_hardness"] < 276:
        cf = 2.0
    elif daily_tests["calcium_hardness"] < 351:
        cf = 2.1
    elif daily_tests["calcium_hardness"] < 601:
        cf = 2.2
    else:
        cf = 2.5

    # determine total alkalinity factor
    if daily_tests["total_alkalinity"] < 37:
        af = 1.4
    elif daily_tests["alkalinity_factor"] < 64:
        af = 1.7
    elif daily_tests["alkalinity_factor"] < 88:
        af = 1.9
    elif daily_tests["alkalinity_factor"] < 114:
        af = 2.0
    elif daily_tests["alkalinity_factor"] < 139:
        af = 2.1
    elif daily_tests["alkalinity_factor"] < 164:
        af = 2.2
    elif daily_tests["alkalinity_factor"] < 226:
        af = 2.3
    elif daily_tests["alkalinity_factor"] < 276:
        af = 2.4
    elif daily_tests["alkalinity_factor"] < 351:
        af = 2.5
    elif daily_tests["alkalinity_factor"] < 601:
        af = 2.6
    else:
        af = 2.9

    # calculate and print saturation index
    saturation_index = daily_tests["pH"] + tf + cf + af - tds

    print(f"Your saturation index is {saturation_index}")


def print_table():
    """
    Prints a table of the min, max, and optimum value of the different chemicals
    """
    values_table = PrettyTable()

    values_table.field_names = ["Parameter", "Minimum", "Ideal", "Maximum"]
    values_table.add_row = ["Free Chlorine", "1.0", "2.0-4.0", "5.0"]
    values_table.add_row = (["Combined Chlorine", "0", "0", "0.2"])
    values_table.add_row = (["pH", "7.2", "7.4-7.6", "7.8"])
    values_table.add_row = (["Total Alkalinity", "60", "80-100*", "180"])
    values_table.add_row = (["Calcium Hardness", "150", "200-400", "1000"])
    values_table.add_row = (["Heavy Metals", "None", "None", "None"])
    values_table.add_row = (["Visible Algae", "None", "None", "None"])
    values_table.add_row = (["Bacteria", "None", "None", "Local Code"])
    values_table.add_row = (["Cyanuric Acid", "0", "30-50", "Local Code"])
    values_table.add_row = (["Temperature (in degF)", "78", "80.5", "82"])

    print(values_table)
    print("\n\n*For calcium hypochlorite, lithium hypochlorite, or sodium hypochlorite")


def menu():
    """
    menu function welcomes the user, prompts for pool volume, then calls get_test_results to
    to obtain the user's water chemistry tests.  The menu is then printed, from which the user
    can choose which function to execute.
    """

    print(figlet_format("Welcome to the Pool Maintenance Management Program"))

    pool_gallons = int(
        input("Let's start by getting the volume of your pool (in gallons): "))

    pool_factor = pool_gallons / 10000

    get_test_results()

    # prints the menu and prompts user for selection. 
    while True:
        print("\nWhat would you like to do?")
        print("\n\n1. Export Test Results\n"
              "2. Increase Chlorine\n"
              "3. Neutralize Chlorine\n"
              "4. Increase Total Alkalinity\n"
              "5. Decrease Total Alkalinity\n"
              "6. Increase Calcium Hardness\n"
              "7. Increase Stabilizer\n"
              "8. Calculate Saturation Index\n"
              "9. Print Water Chemistry Guidelines\n"
              "10. Export test results to a CSV file\n"
              "11. Exit")
        user_input = input("Please make a selection from the menu.  ")
        try:
            int(user_input)
            # checks user input and calls the correct function
            if user_input == "1":
                export_test_results()
            elif user_input == "2":
                increase_chlorine(pool_factor)
            elif user_input == "3":
                neutralize_chlorine(pool_factor)
            elif user_input == "4":
                increase_TA(pool_factor)
            elif user_input == "5":
                decrease_TA(pool_factor)
            elif user_input == "6":
                increase_CH(pool_factor)
            elif user_input == "7":
                increase_stabilizer(pool_factor)
            elif user_input == "8":
                calculate_SI(daily_tests)
            elif user_input == "9":
                print_table()
            elif user_input == "10":
                print("\n\n****Thank you for using the Pool Maintenance Program!****")
                break
            else:
                print(
                    "\n\nI'm sorry. Your selection was not valid. Please enter a number from the menu below.")
        except:
            print("\n\n****Input must be a number. Please try again****")


menu()
