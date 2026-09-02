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
        print("Enter a valid number ")
        return None




def add_student(students_list):
    name = input("enter full name : ")

    grades = input("enter grades use space to splite them ").split(" ")

    students_list.append({name : grades})



    


def show_classment(students_list):
    pass
    


def main():
    students_list = []
    while True :
        menu()
        choice = manage_choices()

        match choice:
            case 1:
                add_student(students_list)
                print(students_list)
            case 2:
                show_classment(students_list)
            case 3:
                print("goodbye")
                break
            case None:
                print("you entered invalid input")
            case _:
                print("invalid choice")


main()