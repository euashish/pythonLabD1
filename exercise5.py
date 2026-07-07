# Problem Type : Student management System


# Problem statement: Create a program that stores student information and displays student details.
# Features : 1. Add student 2. Search Student 3.Display all student


# Okay..........! Now solve the problem.

students = {}

def add_student():
          name = input("Enter student name:")
          roll = input("Enter roll: ")
          marks = float(input("Enter marks: "))
          
          students[roll] = {
               "name": name,
               "marks": marks  
          }
          
          def search_student():
                    roll = input("Enter roll number: ")
                    if roll in students :
                              print(students[roll])
                    else:
                              print("Student not found")
                              
                              
          def display_student() :
                    for roll, info in students.items():
                              print("Roll:", roll)
                              print("Details:", info)
                              
                              
                              while True:
                                        print("\n1. Add Student")
                                        print("2. Search Students")
                                        print("3. Display Students")
                                        print("4. Exit")
                                        
                                        choice = input("Choose option: ")
                                        
                                        if choice == "1":
                                        add_student()
                                        
                                        elif choice == "2":
                                        search_student()
                                        
                                        elif choice == "3"
                                        display_student()
                                        
                                        elif choice == "4"
                                        break
                              
                              else:
                                        print("Invalid Choice")
                                        # problem not yet solved. I have to solve it later. Thank you. 