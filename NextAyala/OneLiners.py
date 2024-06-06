import functools

with open("names.txt", 'r') as names_file:
    names_text = names_file.read().splitlines()
    print(names_text)

    # getting the longest name in the file
    longest_name = max(names_text, key=len)
    print(longest_name)
    print('\n')

    # getting the sum of lengths of the names
    sum_of_lengths = sum(len(name) for name in names_text)
    print(sum_of_lengths)
    print('\n')

    # getting the names with the shortest length
    shortest_length = len(min(names_text, key=len))
    shortest_names = [name for name in names_text if len(name) == shortest_length]
    print('\n'.join(map(str, shortest_names)))

    # getting the length of each name
    length_of_each_name = [len(name) for name in names_text]
    print('\n'.join(map(str, length_of_each_name)))

    # getting the names with the same length the user entered
    length_from_user = int(input("enter length of name: "))
    names_with_the_length_from_user = [name for name in names_text if len(name) == length_from_user]
    print('\n'.join(map(str, names_with_the_length_from_user)))
