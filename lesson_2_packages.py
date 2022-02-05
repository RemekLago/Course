import random
from termcolor import colored

weight_max = 20
number_of_elements_to_pack = 15
# creating list of packages weight, possible are value from 1 to 10 kg
list_of_weight = [i for i in range(0, 11)]
# creating list of random packages with its weight
list_of_packages_to_send = random.choices(list_of_weight, k=number_of_elements_to_pack)
print(colored(f"List of packages to pack with its weight (kg):\n{list_of_packages_to_send}\n", "yellow"))

# function add packages till weight is = weight_max
# function return list of packed packages and id where list was ended
def adding_packages(number):
    list_send = []
    weight_send = 0
    value = list_of_packages_to_send
    for i in range(number, len(value)):
        if value[i] > 0:
            if weight_send + value[i] <= weight_max:
                    weight_package = value[i]
                    weight_send += weight_package
        #           print(weight_send)
                    list_send.append(value[i])
                    round = i
            else:
                break
        else:
            round = len(value)
            break

    print(f"List_send: {list_send} , ID: {round}")
    return list_send, round + 1
#adding_packages(0)

# function takes function (adding_packages) and does a loop till all packages will packed
# function create list of lists
def all_packages(number):
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
    final = all_packages(number)
    number_of_sent_packages = len(final)
    number_of_kilograms_sent = sum([sum(final[i]) for i in range(len(final))])
    number_of_empty_kilos = number_of_sent_packages * 20 - number_of_kilograms_sent
    number_of_package_with_max_empty_weight = 20 - min([sum(final[i]) for i in range(len(final))])
    list_helper = [sum(final[i]) for i in range(len(final))]
    print(list_helper)
#    print(min(list_helper))
    package_with_max_empty_weight = list_helper.index(min(list_helper)) + 1
#    package_with_max_empty_weight = final.count(min(list_helper))


    print(colored(f"Number of packages to send:\n {number_of_sent_packages}", "blue"))
    print(colored(f"Number of kilograms to send:\n {number_of_kilograms_sent}", "blue"))
    print(colored(f"Amount of empty kilograms in all packages:\n {number_of_empty_kilos}", "blue"))
    print(colored(f"Number of package with the biggest amount of empty kilograms:\n"
                  f" {package_with_max_empty_weight} and it was {number_of_package_with_max_empty_weight} kg", "blue"))

final_information(0)