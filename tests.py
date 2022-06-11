import json

json_file = open('Task.json').read()
data = json.loads(json_file)

def clean_data():
    id_list = []
    name_list = []
    age_list = []
    member_list = []
    people_surname_list = []
    familiy_surname_list = []
    parents_list = []
    has_kids_list = []
    temp_kids_list = []
    kids_list = []
    kids_num_list = []
    temp_list = []
    for people in data['people']:
        for info in people:
            names = people[info]['name']
            surnames = people[info]['surname']
            age = people[info]['age']
            member = people[info]['family_member']
            name_list.append(names)
            age_list.append(age)
            member_list.append(member)
            people_surname_list.append(surnames)
    for family in data['families']:
        for info in family:
            id_list.append(info)
            for details in family[info]:
                surnames = family[info]['surname']
                has_kids = family[info]['has_kids']
                parents = family[info]['parents']
                kids = family[info]['kids']
                kids_num = family[info]['kids_num']
            familiy_surname_list.append(surnames)
            temp_list.append(parents)
            has_kids_list.append(has_kids)
            temp_kids_list.append(kids)
            kids_num_list.append(kids_num)
    for i in temp_list:
        for x in i:
            parents_list.append(x)
    for kid in temp_kids_list[0]:
        kids_list.append(kid)

    # This checks if the first 3 digits in the id field of families is indeed 999
    id_status = False
    for id in id_list:
        if '999' in id:
            id_status = True
            print("The number 999 is the beginning of the id in this list")
        else:
            print("The number 999 is not part of the id related to the families list\n")
    print()

    # This check wheter the names have a numerical correspondent as the surnames
    if len(name_list) == len(people_surname_list):
        print("All the people have a corresponding surname to their name ", "\n" " number of names:", len(name_list), "\n" " number of surnames:", len(people_surname_list), "\n")
    else:
        print("The number of names does not correspond to the number of surnames" + " number of names: ", len(name_list), " number of surnames: ", len(people_surname_list), "\n")

    # This checks whetter there are ages that correspond to the age of teenagers and if it equals to the number of children available
    teens = 0
    for i in age_list:
        if i < 18:
            teens+=1
        else:
            continue
    if len(kids_list) == teens:
        print("The number of teens corresponds to the list of children, age wise","\n" " Kids count:", len(kids_list), "\n Ammount of teens by age:", teens, "\n")
    else:
        print("The ages and the ammount of teens do not correspond","\n" " Kids count:", len(kids_list), "\n Ammount of teens by age:", teens, "\n")

    # This checks if the ammount of parents corresponds to the actual number of parents
    grownups = 0
    for i in age_list:
        if i >= 18:
            grownups+=1
        else:
            continue
    if len(parents_list) == grownups:
        print("The number of parents corresponds to the number of grownups by age\n", "The number of parents:", len(parents_list), "\n The ammount of grownups by age:", grownups, "\n")
    else:
        print("The number of parents DOES NOT correspond to the number of grownups by age\n", "The number of parents:", len(parents_list), "\n The ammount of grownups by age:", grownups, "\n")



    # This code checks wheter the ammount of family members corresponds to the number of kids and grownups in the list
    temp_members_kids = 0
    temp_members_parents = 0
    for mem in member_list:
        if mem == 'kid':
            temp_members_kids+=1
        elif mem == 'parent':
            temp_members_parents+=1
        else:
            continue
    if temp_members_kids == teens:
        print("Kid family member corresponds to the ammount of kids in general\n", "The ammount of kids:", teens, "\n The members that are kids:", temp_members_kids, "\n")
    else:
        print("Kid family member DOES NOT correspond to the ammount of kids in general\n", "The ammount of kids:", teens, "\n The members that are kids:", temp_members_kids, "\n")
    if temp_members_parents == grownups:
        print("Grownups family member corresponds to the ammount of parents in general\n", "The ammount of parents:", grownups, "\n The members that are parents:", temp_members_parents, "\n")
    else:
        print("Grownups family member DOES NOT correspond to the ammount of parents in general\n", "The ammount of parents:", grownups, "\n The members that are parents:", temp_members_parents, "\n")

    # This checks wheter the surnames match from people list and families list
    shemesh = 0
    yakir = 0
    for surname in people_surname_list:
        if surname == familiy_surname_list[0]:
            shemesh+=1
        elif surname == familiy_surname_list[1]:
            yakir+=1
        else:
            print("the surnames dont match")
    if shemesh > 0 | yakir > 0:
        print("There are matching surnames between the people dictionary and the families dictionary\n", "The ammount of shemeshes:",shemesh, "\n The ammount of yakirs:",yakir, "\n")

    #This checks if the ammount of people is correct
    if shemesh + yakir == len(name_list) & shemesh + yakir == len(people_surname_list) & shemesh + yakir == len(member_list):
        print("The ammount of people is the correct between multiple lists", "\n")
    else:
        print("The ammount of people is DIFFERENT between surname, member and name lists", "\n")

    # This checks the ammount of children in the list
    if len(kids_list) == kids_num_list[0]:
        print("There is a matching number of kids between lists\n there are:", len(kids_list), "kids ", "\n and the ammount of kids on the kids num list:", kids_num_list[0], "\n")
    else:
        print("The number of kids does not match")

    # This checks if yakir family has indeed 0 children
    if temp_kids_list[1] == None:
        print("Yakir family has 0 children\n the number of kids is:",kids_num_list[1], "\n the value for kids in list is:", temp_kids_list[1], "\n")

    # This checks whetter shemesh family has kids or not and what is the ammount of them
    if len(temp_kids_list[0]) == len(kids_num_list):
        print("Shemesh family has the same ammount of kids between lists\n", "The ammount of kids is:", len(temp_kids_list[0]),"\n The ammount of kids in list:", kids_num_list[0], "\n")
    else:
        print("The ammount of kids is not matching")

clean_data()