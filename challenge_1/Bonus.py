#!/usr/bin/env python3


def menu():
    print("1. Ajouter etudiant")
    print("2. Afficher classement")
    print("3. Quitter")

def manage_choices():
    try:
        choice = int(input("enter a choice : "))
        return choice
    except ValueError :
        return None




def add_student(students_list):
    name = input("enter the name : ")
    check = False
    grades = list(map(float, filter(lambda x: x!= "", input("enter grades use space to splite them ").split(" "))))
    
    


    if(len(grades) > 3):
        print("only 3 notes are allowed")
    else:
        for grade in grades:
            if 0 < float(grade) <= 20:
                check = True
            else:
                check = False
                break
            
    if check :
        students_list.append({"name" : name , "grades" : grades})


# grades = list(filter(lambda x: x!= "", "5    12 17     18 24 32".split(" ")))

# print(grades)
def mentions_check(grade):
    if grade == None:
        return None
    elif 16 <= grade <=20:
        return "Très bien"
    elif 12 <= grade < 16:
        return "Bien"
    elif 10 <= grade < 12:
        return "Passable"
    elif 0 <= grade < 10:
        return "Insuffisant"
    elif grade < 0:
        return "invalid grade input (valide : between 0 and 20)"
    else:
        print("invalid input")
        return None



def calc_avg(grades):
    try:
        return round(sum(grades) / len(grades), 1)
    except ZeroDivisionError:
        # print("list is empty")
        return None
# print(calc_avg([1, 2.00021, 3.123, 4, 1.3, 4, 1]))


def show_classment(students_list):
    tracing = []
    for index, student in enumerate(students_list):
        avg = calc_avg(student["grades"])
        if student["name"] not in tracing:
            tracing.append(student["name"])
            safe_mentions_check = mentions_check(avg)
            if safe_mentions_check == None:
                print(f"{index + 1} {student["name"]} -- empty list")    
            else:
                print(f"{index + 1} {student["name"]} {avg} {mentions_check(avg)}")
        elif student["name"] in tracing:
            print(f"{index + 1} {student["name"]} Doublon de nom à détecter")
        # elif avg == None:
        #     print("empty list")
    

# show_classment([
# {"name": "Karim", "grades": [12, 8, 16]},
# {"name": "Sara", "grades": [18, 17, 19]},
# {"name": "Lina", "grades": [5, 6, 4]},
# {"name": "Youssef","grades": [10, 10, 10]},
# {"name": "Nadia", "grades": [16, 16, 16]},
# {"name": "Karim", "grades": [11, 12, 13]},
# {"name": "Hicham", "grades": []},
# ])



def main():
    students_list = []
    try:
        while True :
                menu()
                choice = manage_choices()
        
                match choice:
                    case 1:
                        add_student(students_list)
                        # print(students_list)
                    case 2:
                        show_classment(students_list)
                    case 3:
                        print("goodbye")
                        break
                    case None:
                        print("you entered invalid input")
                    case _:
                        print("invalid choice")
        
    except KeyboardInterrupt:
        print("\n --- stopped by the user ---")


main()