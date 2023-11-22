# ------------------------------------------------------------------------------------------ #
# Title: Assignment06_Starter
# Desc: This assignment demonstrates using functions
# with structured error handling
# Change Log: (Who, When, What)
#   KWard,11/18/2023,Created Script
#
# ------------------------------------------------------------------------------------------ #
import json
import io as _io
# Define the Data Constants
MENU: str = '''
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course.
    2. Show current data.  
    3. Save data to a file.
    4. Exit the program.
----------------------------------------- 
'''
# Define the Data Constants
# FILE_NAME: str = "Enrollments.csv"
FILE_NAME: str = "Enrollments.json"

# Define the Data Variables and constants
students: list = []  # a table of student data
menu_choice: str  # Hold the choice made by the user.
file = _io.TextIOWrapper
# When the program starts, read the file data into a list of lists (table)
# Extract the data from the file


#processes data
class FileProcessor:
    '''
    Contains methods to read data from file, and save data to file
    
    Kward, 11/20/23, created class
    '''
    @staticmethod
    def read_data_from_file(file_name: str, student_data: list):
        '''
        Reads data from json file into list of students
        returns student_data
        '''
    
        try:
            file = open(FILE_NAME, "r")
            student_data = json.load(file)
            file.close()
            
        except Exception as e:
            IO.output_error_messages('Problem opening file',e)
        finally:
            if file.closed == False:
                file.close()
        return student_data

    @staticmethod
    def write_data_to_file(file_name: str, student_data: list):
        '''
        writes all the sets of student data inot json file
        '''
        try:
            file = open(file_name, 'w')
            json.dump(student_data, file)
            file.close()
            IO.output_student_courses(student_data=student_data)
            print("The data has been saved")
                  
        except Exception as e:
            IO.output_error_messages('Problem writing to file', e)
        finally:
            if file.closed == False:
                file.close()
                
                
            

#inputs and outputs
class IO:
    '''
    Contains methods to get user input, and output info
    
    Kward, 11/20/23, created class
    '''
    global menu_choice
    
    @staticmethod
    def output_menu(menu: str):
        print(MENU)

    @staticmethod
    def input_menu_choice():
            menu_choice = input('What would you like to do: ')
            return menu_choice
        
    @staticmethod
    def output_student_courses(student_data: list):
        '''
        prints out all students data sets
        '''
        print("-" * 50)
        for student in student_data:
            print(f'{student["firstName"]} '
                  f'{student["lastName"]} is enrolled in {student["courseName"]}')
        print("-" * 50)   
        
    @staticmethod
    def input_student_data(student_data: list):
        '''
        Gets data from user, and saves it to students
        '''
        try:
            student_first_name = input("Enter the student's first name: ")
            if not student_first_name.isalpha():
                raise ValueError("The last name should not contain numbers.")
            student_last_name = input("Enter the student's last name: ")
            if not student_last_name.isalpha():
                raise ValueError("The last name should not contain numbers.")
            course_name = input("Please enter the name of the course: ")
            student = {"firstName": student_first_name,
                                "lastName": student_last_name,
                                "courseName": course_name}
            student_data.append(student)
            print(f"You have registered {student_first_name} {student_last_name} for {course_name}.")
        except ValueError as e:
            IO.output_error_messages('Wrong value type entered', e)
        except Exception as e:
            IO.output_error_messages('There was a problem with your entered data.', e)
                
        return student_data
                
    @staticmethod
    def output_error_messages(message: str, error: Exception = None):
        '''
        Outputs error message when called
        '''
        print(message)
        if error is not None:
            print('---Error Message---')
            print(error, error.__doc__, type(error), sep='\n')



students = FileProcessor.read_data_from_file(FILE_NAME, student_data=students)

# Present and Process the data
while (True):

    # Present the menu of choices
    IO.output_menu(menu=MENU)
    menu_choice = IO.input_menu_choice()

    # Input user data
    if menu_choice == "1":  # This will not work if it is an integer!
        students = IO.input_student_data(student_data=students)
        continue

    # Present the current data
    elif menu_choice == "2":

        # Process the data to create and display a custom message
        IO.output_student_courses(students)
        continue

    # Save the data to a file
    elif menu_choice == "3":

        FileProcessor.write_data_to_file(FILE_NAME, student_data=students)
        continue

    # Stop the loop
    elif menu_choice == "4":
        break  # out of the loop
    else:
        print("Please only choose option 1, 2, or 3")
        
print("Program Ended")
