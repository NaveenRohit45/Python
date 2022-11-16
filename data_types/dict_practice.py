def dict_2():
    # create a dictionary using {}
    person = {"name": "Jessa", "country": "USA", "telephone": 1178}
    print(person)
    # output {'name': 'Jessa', 'country': 'USA', 'telephone': 1178}

    # create a dictionary using dict()
    person = dict({"name": "Jessa", "country": "USA", "telephone": 1178})
    print(person)
    # output {'name': 'Jessa', 'country': 'USA', 'telephone': 1178}

    # create a dictionary from sequence having each item as a pair
    person = dict([("name", "Mark"), ("country", "USA"), ("telephone", 1178)])
    print(person)

    # create dictionary with mixed keys
    # first key is string and second is an integer
    sample_dict = {"name": "Jessa", 10: "Mobile"}
    print(sample_dict)
    # output {'name': 'Jessa', 10: 'Mobile'}

    # create dictionary with value as a list
    person = {"name": "Jessa", "telephones": [1178, 2563, 4569]}
    print(person)
    # output {'name': 'Jessa', 'telephones': [1178, 2563, 4569]}

    ############
    # creating empty dict

    empty_dict = {}
    print(empty_dict)
    print(type(empty_dict))

    #############
    person = {"name": "jessa", "country": "USA", "telephone": 1178}
    print(person['name'])
    print(person.get("telephone"))
    print(person.keys())
    print(person.values())
    print(person.items())

    #  Iterating a dictionary #####

    person = {"name": "jessa", "country": "USA", "telephone": 1178}
    print('key', ':', 'value')

    for key in person:
        print(key, ':', person[key])

    print('key', ':', 'value')
    for key_value in person.items():
        print(key_value[0], key_value[1])

    # ************Adding items to the dictionary***********
    # adding keys in dict
    person = {"name": "jessa", "country": "USA", "telephone": 1178}
    # person['weight'] = "50"
    # person.update({'hight' : 5})
    person.update({"weight": 50, "hight": 5})
    print(person)

    # ******Modify the values of the dictionary keys************
    # updating new value
    person = {"name": "Jessa", "country": "USA"}

    # updating the country name
    person["country"] = "Canada"
    # print the updated country
    print(person['country'])
    # Output 'Canada'

    # updating the country name using update() method
    person.update({"country": "USA"})
    # print the updated country
    print(person['country'])

    # ********** Removing items from the dictionary***********
    person = {'name': 'Jessa', 'country': 'USA', 'telephone': 1178, 'weight': 50, 'height': 6}

    # Remove last inserted item from the dictionary
    deleted_item = person.popitem()
    print(deleted_item)
    # display updated dictionary
    print(person)

    # Remove key 'telephone' from the dictionary
    deleted_item = person.pop('telephone')
    print(deleted_item)
    # display updated dictionary
    print(person)

    # delete key 'weight'
    del person['weight']
    # display updated dictionary
    print(person)

    # remove all item (key-values) from dict
    person.clear()
    # display updated dictionary
    print(person)

    # Delete the entire dictionary
    del person

    # ******** Checking if a key exists *********
    person = {'name': 'Jessa', 'country': 'USA', 'telephone': 1178, 'weight': 50, 'height': 6}

    key_name = "telephone"

    if key_name in person.keys():
        print("telephone number is", person[key_name])

    else:
        print("its not in the dict")

    # ********************** Join two dictionary ********
    dict1 = {'Jessa': 70, 'Arul': 80, 'Emma': 55}
    dict2 = {'Kelly': 68, 'Harry': 50, 'Olivia': 66}
    # we can you two different way to merge the dict
    dict1.update(dict2)
    print(dict1)

    dict3 = {**dict1, **dict2}
    print(dict3)

    # ****************** Join two dictionaries having few items in common ************ Note: One thing to note here
    # is that if both the dictionaries have a common key then the first dictionary value will be overridden with the
    # second dictionary value.
    dict1 = {'Jessa': 70, 'Arul': 80, 'Emma': 55}
    dict2 = {'Kelly': 68, 'Harry': 50, 'Emma': 66}
    # we can you two different way to merge the dict
    dict1.update(dict2)
    print(dict1["Emma"])

    # ************* Copy a Dictionary**************

    dict1 = {'Jessa': 70, 'Emma': 55}

    dict2 = dict1.copy()
    print(dict2)

    dict3 = dict(dict1)
    print(dict3)

    dict4 = dict(dict1.items())
    print(dict4)

    # nested

    # address dictionary to store person address
    address = {"state": "Texas", 'city': 'Houston'}

    # dictionary to store person details with address as a nested dictionary
    person = {'name': 'Jessa', 'company': 'Google', 'address': address}

    # Display dictionary
    print("person:", person)

    # Get nested dictionary key 'city'
    print("City:", person['address']['city'])

    # Iterating outer dictionary
    print("Person details")
    for key, value in person.items():
        if key == 'address':
            # Iterating through nested dictionary
            print("Person Address")
            for nested_key, nested_value in value.items():
                print(nested_key, ':', nested_value)
        else:
            print(key, ':', value)


dict_2()
