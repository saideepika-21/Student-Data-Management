#studentDB Features
#1. Add student (ID,Name,Age,Course,Marks)
#2.Display all students
#3.Search student by ID
#4.Update student details
#5.Delete student by ID
#6.Save/load data from file
#7.Menu-based navigation

import json
filename="students.json"

def load_students():
    try:
        with open(filename,'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []
    

def add_student(students):
    sid = input("Enter student ID:")
    name = input("Enter name:")
    age = input("Enter age:")
    course = input("Enter course name:")
    marks = input("Enter marks:")
    students.append({
        "id":sid,
        "name":name,
        "age":age,
        "course":course,
        "marks":marks
    })
    print("student added successfully")

def display_students(students):
    if not students:
        print("No Students records found.")
        return 
    print("\n ----- STUDENTS RECORDS -----")
    for s in students:
        print(f"ID:{s['id']}, Name: {s['name']}, Age: {s['age']}, course: {s['course']}, marks: {s['marks']}")


def search_student(students):
    sid=input('Enter student ID to search:')
    for s in students:
        if s['id'] == sid:
            print(f'Found -> {s}')
            return
    print('Student Record Not Found')

def update_student(students):
    sid=input('enter student ID to update:')
    for s in students:
        if s['id'] == sid:
            print("\n-----Update Options-----")
            print("1.Update individual fields")
            print("2.Update all fields")
            
            options=input("Enter your option:")
            #---individual fields update-----
            if options == "1":
                print("Which field do you want to update?")
                print("1.Name")
                print("2.Age")
                print("3.Course")
                print("4. Course")
                choice=input("Enter your choice:")
                if choice=="1":
                    s['name']=input("Enter new name:")
                    print('Student updated successfully!')
                elif choice=="2":
                    s['age'] = input('Enter new Age:')
                    print('Student updated successfully!')
                elif choice=="3":
                    s['course'] = input('Enter new Course:')
                    print('Student updated successfully!')
                elif choice=="4":
                    s['marks'] = input('Enter new marks:')
                    print('Student updated successfully!')
                else:
                    print("Invalid field choice.")
                    return
                #all fields update
            elif options=="2":
                s['name'] = input('Enter new name:')
                s['age'] = input('Enter new Age:')
                s['course'] = input('Enter new Course:')
                s['marks'] = input('Enter new marks:')
                print('Student updated successfully!')
                return
            else:
                print("Invalid update option")
                return
            return
        print('Student not Found')


def delete_student(students):
    sid=input('Enter Student ID to search:')
    for s in students:
        if s['id'] == sid:
            students.remove(s)
            print(f'Student deleted Successfully')
            return
        print("Student Record Not Found.")

def save_student(students):
    with open(filename,'w') as f:
        json.dump(students,f,indent=4)


def main():

    students = load_students()
    
    while True:
        print("\n===== StudentDB Menu =====")
        print("1. Add Student")
        print("2. Display Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Save & Exit")

        choice=input("Enter your choice:")
        if choice == "1":
            add_student(students)
        elif choice == "2":
            display_students(students)
        elif choice == "3":
            search_student(students)
        elif choice == "4":
            update_student(students)
        elif choice == "5":
            delete_student(students)
        elif choice == "6":
            save_student(students)
            print("Data Saved. Exiting program.")
            break
        else:
            print("Invalid choice! Try again.")
main()