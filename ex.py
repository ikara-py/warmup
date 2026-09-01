#!/usr/bin/env python3


# first_name = input("enter your first name : ")
# last_name = input("enter your last name : ")

# grades = []

# MAX_NUM = 3
# num= 1

# while num <= MAX_NUM:


#     note = input(f"enter grade number {num} : ")
#     grades.append(note)
#     num += 1

# for g in grades:
#     try:
#         float(g)
#         print(f"Note acceptee : {g}")
#     except:
#         print("it is not a number try again.")

        
# summ = 0

# try:

#     for grade in grades:
#         summ += float(grade)
#     print(f" : {summ/ len(grades):.2f}")
# except ValueError as err:
#     print(f"there is err {err}")

# # print(f"{first_name} {last_name} : {sum(grades)/ len(grades):.2f}")

# print(grades)


grades = [12, 13.22, 15]



def calculer_moyenne(grades):
    summ = 0

    try:
        for grade in grades:
            summ += float(grade)
        
        return round(summ / len(grades), 2)
    except ValueError as err:
        return err


valeurs_test = [9.9, 10.0, 11.9, 12.0, 15.9, 16.0, 20.0]

def appreciation(grades_list):
    for i in grades_list:
        if i >= 16 and i <= 20:
            print(f"{i} -> Tres bien")
        elif i >= 12 :
            print(f"{i} -> bien")
        elif i >= 10:
            print(f"{i} -> Passable")
        elif i < 10:
            print(f"{i} -> Insuffisant")

# appreciation(valeurs_test)

# print(calculer_moyenne(grades))

etudiants = [
    {"nom": "Karim", "notes": [12, 15, 9]},
    {"nom": "Sara", "notes": [18, 17, 16]},
    {"nom": "Lina", "notes": [6, 8, 5]},
]

def moyenne_groupe(etudiants):
    pass
