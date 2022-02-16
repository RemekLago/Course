from termcolor import colored

weight_max = 20


def creating_list_of_packages():
    """ function takes weights from input, clear spaces and
    split by commas to list"""
    list_of_packages_to_send = []
    package = input(f"Please enter weight of packages(with commas): ")
    package1 = package.replace(" ", "")
    package2 = package1.split(",")
    for idx, number in enumerate(package2):
        if number != " " and number != ",":
            list_of_packages_to_send.append(number)
    print(colored(f"List of packages to pack with its weight (kg):\n"
                  f"{list_of_packages_to_send}\n", "yellow"))
    return list_of_packages_to_send


list_of_packages_to_send = creating_list_of_packages()


def adding_packages(number):
    """ function add packages till weight is = weight_max
    function return list of packed packages and id where list was ended"""
    list_send = []
    weight_send = 0
    value = list_of_packages_to_send
    for i in range(number, len(value)):
        if 0 < int(value[i]) <= 10:
            if weight_send + int(value[i]) <= weight_max:
                weight_package = int(value[i])
                weight_send += weight_package
                list_send.append(int(value[i]))
                round_number = i
        elif int(value[i]) == 0:
            round_number = i
            break
        else:
            round_number = i
            print(colored("ERROR, ERROR, ERROR, ERROR", "red"))
            break
    print(f"List_send: {list_send} , ID: {round_number}")
    return list_send, round_number + 1


def all_packages(number):
    """ function takes function (adding_packages) and does a loop till
    all packages will packed function create list of lists"""
    final_list = []
    y = number
    while y < (len(list_of_packages_to_send)):
        all = adding_packages(y)
        x = all[0]
        final_list.append(x)
        print(f"Final list: {final_list}")
        y = int(all[1])
    return final_list


def final_information(number):
    """Printing final results"""
    final = all_packages(number)
    number_of_sent_packages = len(final)
    number_of_kilograms_sent = sum([sum(final[i]) for i in range(len(final))])
    number_of_empty_kilos = number_of_sent_packages * 20 - number_of_kilograms_sent
    number_of_package_with_max_empty_weight = \
        20 - min([sum(final[i]) for i in range(len(final))])
    list_helper = [sum(final[i]) for i in range(len(final))]
    print(f"Sum in each package: {list_helper}")

    package_with_max_empty_weight = list_helper.index(min(list_helper)) + 1
    print(colored(
        f"Number of packages to send:\n {number_of_sent_packages}", "blue"))
    print(colored(
        f"Number of kilograms to send:\n {number_of_kilograms_sent}", "blue"))
    print(colored(
        f"Amount of empty kilograms in all packages:\n {number_of_empty_kilos}", "blue"))
    print(colored(
        f"Number of package with the biggest amount of empty kilograms:\n"
        f"{package_with_max_empty_weight} and it was "
        f"{number_of_package_with_max_empty_weight} kg", "blue"))


final_information(0)