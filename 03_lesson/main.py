# Task 1


def len_string(string):
    return len(string)


def concatenation(firs_str, second_str):
    return firs_str + " " + second_str


# Task 2


def square_of_number(num):
    return num**2


def add_number(num1, num2):
    return num1 + num2


def division_number(num1, num2):
    if num2 == 0:
        raise ZeroDivisionError("zero division by zero")

    return num1 // num2, num1 % num2


# Task 3


def average_number_of_list(input_list):
    return sum(input_list) / len(input_list)


def identical_numbers_of_list(firs_list, second_list):
    # new_list = []
    # for i in firs_list:
    #     for j in second_list:
    #         if i == j:
    #             new_list.append(i)
    # temp_set = set(new_list)
    # new_list = list(new_list)
    # return new_list

    return list({i for i in firs_list for j in second_list if i == j})


# Task 4


def info_dict(input_dict):
    for key in input_dict.keys():
        print(key)


def merge_dicts(dict1, dict2):
    return dict1 | dict2


# Task 5


def merge_sets(set1, set2):
    return set1 | set2


def is_subsets(set1, set2):
    return set1.issubset(set2)


# Task 6


def even_odd_number(number):
    if number % 2 == 0:
        print("even")
        return

    print("odd")


def even_numbers_list(input_list):
    return [number for number in input_list if number % 2 == 0]


# Task 7

fn = lambda number: "even" if number % 2 == 0 else "odd"
