import csv
from collections import defaultdict

class main:
    def __init__(self):
        pass

    def csvName(self):
        with open("idName.csv") as f:
            reader = csv.reader(f)
            header = []
            header = next(reader)
            id_value = {}
            for x, y in reader:
                id_value[x] = y
            print(id_value)
            my_name = list(id_value.values())
            print(my_name)

        ##################################
        with open("idSalary.csv") as f1:
            reader = csv.reader(f1)
            header = []
            header = next(reader)
            id_salary = {}
            for i, j in reader:
                id_salary[i] = j
            print(id_salary)
            my_sal = list(id_salary.values())
            print(my_sal)

        combine = {}
        for a in my_sal:
            combine[a] = my_name
        print(combine)
        f.close()

    def combaine(self):
        name_file = self.csvName()
        salary_file = self.csvSalary()
        print(name_file)
        print(salary_file)
        

obj = main()
obj.csvName()

