# ------------------------------------------------------------------------------------------------------------------------------ #
# Title: Assignment07
# Desc: This assignment demonstrates using data classes
# with structured error handling
# Change Log: (Who, When, What)
#   <Rucha Nimbalkar>, <11/21/2024>,<Created Script>
#   <Rucha Nimbalkar>, <11/21/2024>,<Re-organize the code and create Classes>
#   <Rucha Nimbalkar>, <11/23/2024>,<Added classes ()>
#   <Rucha Nimbalkar>, <11/24/2024>,<Added attributes to the student class>
#   <Rucha Nimbalkar>, <11/25/2024>,<Added properties and methods for classes>
#   <Rucha Nimbalkar>, <11/27/2024>,<Added constructor and deleted the duplicate classes>
#   <Rucha Nimbalkar>, <11/27/2024>,<Added getter and setter methods and __str__ overiding method for Student and Person>
#   <Rucha Nimbalkar>, <11/27/2024>,<Updated the methods for FileProcessor class>
#   <Rucha Nimbalkar>, <11/27/2024>,<Updated the methods for IO class>
#   <Your Name Here>,<Date>,<Activity>
# ----------------------------------------------------------------------------------------------------------------------------- #
import json


#Data----------------------------------------------------------------------------------------------------#
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
FILE_NAME: str = "Enrollments.json"

# Define the Data Variables
students: list = []  # a table of student data
menu_choice: str  # Hold the choice made by the user.
#--------------------------------------------------------------------------------------------------------#

class Person:
    '''
       A collection data about persons

      ChangeLog: (Who, When, What)
      Rucha Nimbalkar, 11/26/2024,Created Class

    '''

    # Add first_name and last_name properties to the constructor
    def __init__(self, first_name:str = "", last_name : str =""): #parameters default to empty
        self.first_name = first_name
        self.last_name = last_name

    # Create a getter and setter for the first_name property
    @property #Getter or accessor
    def first_name(self):
        return self.__first_name.title() #formatting code

    @first_name.setter
    def first_name(self, value : str):
        if value.isalpha() or value == " ": #first_name value is a character or empty string
            self.__first_name = value
        else:
            raise ValueError("First name cannot have numbers!")

    #Create a getter and setter for the last_name property
    @property #Getter or accessor
    def last_name(self):
        return self.__last_name.title() #formatting code

    @last_name.setter
    def last_name(self, value : str):
        if value.isalpha() or value == " ": #last_name value is a character or empty string
            self.__last_name = value
        else:
            raise ValueError("Last name cannot have numbers!")

    # Override the __str__() method to return Person data
    def __str__(self):
        return f'{self.first_name},{self.last_name}'

#Create a Student class the inherits from the Person class (Done)
class Student(Person):
    '''
        A collection data about students

        ChangeLog: (Who, When, What)
        Rucha Nimbalkar, 11/26/2024,Created Class

    '''

    # Add first_name, last_name and course_name properties to the constructor
    def __init__(self, first_name:str = " ", last_name : str = " ", course_name : str = " "): #parameters default to empty
        #Call to the Person constructor and pass it the first_name and last_name data
        super().__init__(first_name=first_name, last_name=last_name)
        self.course_name = course_name # Add an assignment to the course_name property using the course_name parameter

    # Add the getter for course_name
    @property
    def course_name(self):
        return self.__course_name.capitalize()

    # Add the setter for course_name
    @course_name.setter
    def course_name(self, value:str):
        if value.isalpha() or value == " ": #course_name value is a character or empty string
            self.__course_name = value
        else:
            raise  ValueError("The course name should not contain numbers") #Assuming Course name does not contain numbers

    # Override the __str__() method to return the Student data
    def __str__(self):
         return f'{self.first_name},{self.last_name},{self.course_name}'



#Processing----------------------------------------------------------------------------------------------#
class FileProcessor:
    """
    A collection of processing layer functions that work with Json files

    ChangeLog: (Who, When, What)
    Rucha Nimbalkar, 11/27/2024, Created class
    """
    @staticmethod
    def read_data_from_file(file_name: str, student_data: list):
        """ This function reads data from a json file and loads it into a list of dictionary rows

        ChangeLog: (Who, When, What)
        Rucha Nimbalkar,11/27/2024,Created function
        Rucha Nimbalkar,11/27/2024,Updated the function to read JSON data and create Student objects list
        :param file_name: string data with name of file to read from
        :param student_data: list of Object(Student) rows to be filled with  the JSON file data

        :return: list of Student Objects
        """

        try:
            file = open(file_name, "r")
            #student_data = json.load(file)
            list_of_dictionary_data = json.load(file)  # the load function returns a list of dictionary rows.
            for student in list_of_dictionary_data:
                student_object: Student = Student(first_name=student["FirstName"],
                                                  last_name=student["LastName"],
                                                  course_name=student["CourseName"])
                student_data.append(student_object)
            file.close()
        except Exception as e:
            IO.output_error_messages(message="Error: There was a problem with reading the file.", error=e)

        finally:
            if file.closed == False:
                file.close()
        return student_data

    @staticmethod
    def write_data_to_file(file_name: str, student_data: list):
        """ This function writes data to a json file with data from a list of dictionary rows

        ChangeLog: (Who, When, What)
        Rucha Nimbalkar,11/27/2024,Created function
        Rucha Nimbalkar,11/27/2024,Updated the function to write JSON data from the Student objects list

        :param file_name: string data with name of file to write to
        :param student_data: list of dictionary rows to be writen to the file

        :return: None
        """
        try:
            list_of_dictionary_data: list = []
            for student in student_data:  # Convert List of Student objects to list of dictionary rows.
                student_json: dict \
                    = {"FirstName": student.first_name,
                       "LastName": student.last_name,
                       "CourseName": student.course_name}
                list_of_dictionary_data.append(student_json)

            file = open(file_name, "w")
            json.dump(list_of_dictionary_data, file)
            file.close()
            print("The following data is saved to the file:")
            IO.output_student_and_course_names(student_data=student_data) # Call function to display data
        except Exception as e:
            message = "Error: There was a problem with writing to the file.\n"
            message += "Please check that the file is not open by another program."
            IO.output_error_messages(message=message,error=e)
        finally:
            if file.closed == False:
                file.close()


# Presentation --------------------------------------- #
class IO:
    """
    A collection of presentation layer functions that manage user input and output

    ChangeLog: (Who, When, What)
    RRoot,1.1.2030,Created Class
    RRoot,1.2.2030,Added menu output and input functions
    RRoot,1.3.2030,Added a function to display the data
    RRoot,1.4.2030,Added a function to display custom error messages
    """

    @staticmethod
    def output_error_messages(message: str, error: Exception = None):
        """ This function displays the a custom error messages to the user

        ChangeLog: (Who, When, What)
        Rucha Nimbalkar, 11/27/2024, Created method

        :param message: string with message data to display
        :param error: Exception object with technical message to display

        :return: None
        """
        print(message, end="\n\n")
        if error is not None:
            print("-- Technical Error Message -- ")
            print(error, error.__doc__, type(error), sep='\n')

    @staticmethod
    def output_menu(menu: str):
        """ This function displays the menu of choices to the user

        ChangeLog: (Who, When, What)
        RRoot,1.1.2030,Created function


        :return: None
        """
        print()  # Adding extra space to make it look nicer.
        print(menu)
        print()  # Adding extra space to make it look nicer.

    @staticmethod
    def input_menu_choice():
        """ This function gets a menu choice from the user

        ChangeLog: (Who, When, What)
        RRoot,1.1.2030,Created function

        :return: string with the users choice
        """
        choice = "0"
        try:
            choice = input("Enter your menu choice number: ")
            if choice not in ("1","2","3","4"):  # Note these are strings
                raise Exception("Please, choose only 1, 2, 3, or 4")
        except Exception as e:
            IO.output_error_messages(e.__str__())  # Not passing e to avoid the technical message

        return choice

    @staticmethod
    def output_student_and_course_names(student_data: list):
        """ This function displays the student and course names to the user

        ChangeLog: (Who, When, What)
        Rucha Nimbalkar, 11/27/2024, Created method

        :param student_data: list of dictionary rows to be displayed

        :return: None
        """

        print("-" * 50)
        for student in student_data:
            #print(f'Student {student["FirstName"]} '
                  #f'{student["LastName"]} is enrolled in {student["CourseName"]}')
            #message = "Student {} {} has registered for {}"
            print(student)
        print("-" * 50)

    @staticmethod
    def input_student_data(student_data: list):
        """ This function gets the student's first name and last name, with a course name from the user

        ChangeLog: (Who, When, What)
        Rucha Nimbalkar, 11/27/2024, Created method

        :param student_data: list of dictionary rows to be filled with input data

        :return: list
        """

        try:
            # Input the data
            student = Student()
            student.first_name = input("What is the student's first name? ")
            student.last_name = input("What is the student's last name? ")
            student.course_name = input("What is the course name? ")
            student_data.append(student)
            print()
            #print(f"You have registered {student_first_name} {student_last_name} for {course_name}.")
        except ValueError as e:
            IO.output_error_messages(message="One of the values was the correct type of data!", error=e)
        except Exception as e:
            IO.output_error_messages(message="Error: There was a problem with your entered data.", error=e)
        return student_data


# Start of main body

# When the program starts, read the file data into a list of lists (table)
# Extract the data from the file
students = FileProcessor.read_data_from_file(file_name=FILE_NAME, student_data=students)

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
        IO.output_student_and_course_names(students)
        continue

    # Save the data to a file
    elif menu_choice == "3":
        FileProcessor.write_data_to_file(file_name=FILE_NAME, student_data=students)
        continue

    # End the loop
    elif menu_choice == "4":
        break  # out of the loop

    #Invalid menu choice
    else:
        print("Invalid choice!")

print("Program Ended")
