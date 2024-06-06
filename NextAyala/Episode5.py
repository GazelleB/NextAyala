import functools


def check_id_valid(id_number):
    id_str = str(id_number)
    id_original = [int(digit) for digit in id_str] # splitting the digits

    id_multiplied = [(digit if j % 2 == 0 else digit * 2) for j, digit in enumerate(id_original)]

    fix_multiplied_digits = [(digit if digit // 10 == 0 else (digit % 10 + digit // 10)) for digit in id_multiplied]

    sum_of_digits = functools.reduce(lambda x, y: x + y, fix_multiplied_digits)

    return sum_of_digits % 10 == 0


class IDIterator:
    def __init__(self, id_num):
        self._id = id_num + 1

    def __iter__(self):
        return self

    def __next__(self):
        while self._id <= 999999999:
            self._id += 1
            if check_id_valid(self._id - 1):
                return self._id - 1
        # in case we are at the end and there no good id's
        raise StopIteration


def gen_id(id_num):
    """
    generates id numbers
    :param id_num: the start id number from it we start generate id's
    :return: the next valid id number
    """
    while id_num <= 999999999:
        id_num += 1
        if check_id_valid(id_num - 1):
            yield id_num - 1


user_id = int(input("enter id number "))
user_choice = input("enter it for iterator or gen for generator")
if user_choice == "it":
    IDIter = IDIterator(user_id)
    for i in range(10):
        print(next(IDIter))
else:
    IDGen = gen_id(user_id)
    for i in range(10):
        print(next(IDGen))
