def dictionary():
    # ********* sorted dictionary *******
    dict1 = {'c': 45, 'b': 95, 'a': 35}

    dict2 = (sorted(dict1.items()))
    print(dict2)

    print(sorted(dict1))

    dict3 = (sorted(dict1.values()))
    print(dict3)

    # ******** Dictionary comprehension *****
    numbers = [1, 3, 5, 2, 8]

    emptydict = {x: x ** 2 for x in numbers if x % 2 == 0}
    print(emptydict)

    # two list merging with dictionary
    telephone_book = [1178, 4020, 5786]
    persons = ['Jessa', 'Emma', 'Kelly']

    match = {x: y for x, y in zip(persons, telephone_book)}
    print(match)

    # ******* max() and min() ********
    dict5 = {1: 'aaa', 2: 'bbb', 3: 'AAA'}

    print("Maximum Key:", max(dict5))
    print("Minimum Key:", min(dict5))


dictionary()
