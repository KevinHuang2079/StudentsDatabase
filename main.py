import sqlite3
import csv

db_file = '/Users/kevinhuang/Documents/StudentDB.db'

class StudentDatabase:
    def __init__(self, db_file):
        self.conn = sqlite3.connect(db_file)
        self.mycursor = self.conn.cursor()
        # Create the 'Student' table if it doesn't exist
        self.mycursor.execute("CREATE TABLE IF NOT EXISTS Student(StudentId INTEGER PRIMARY KEY, FirstName TEXT, LastName TEXT, GPA REAL, Major TEXT, FacultyAdvisor TEXT, Address TEXT, City TEXT, State TEXT, ZipCode TEXT, MobilePhoneNumber TEXT, isDeleted INTEGER)")
        self.conn.commit()


    def importData(self,csv_file):
        with open(csv_file, newline='') as f:
            reader = csv.DictReader(f)
            for line in reader:
                # Extract data from the CSV and create a tuple of values
                values = (
                    line.get('FirstName'),
                    line.get('LastName'),
                    line.get('GPA'),
                    line.get('Major'),
                    "Schulyer",      # FacultyAdvisor
                    line.get('Address'),
                    line.get('City'),
                    line.get('State'),
                    line.get('ZipCode'),
                    line.get('MobilePhoneNumber'),
                    0,   #isDeleted
                )
                self.mycursor.execute("INSERT INTO Student(FirstName, LastName, GPA, Major, FacultyAdvisor, Address, City, State, ZipCode, MobilePhoneNumber, isDeleted) VALUES(?,?,?,?,?,?,?,?,?,?,?)", values)

        self.conn.commit()
    def printData(self):
        self.mycursor.execute("SELECT* FROM Student WHERE isDeleted = 0")
        students = self.mycursor.fetchall()
        # Iterate through the selected rows and print each student's data
        for student in students:
            print(student)
    def updateStudent(self):
        while True:
            student_id = input("Enter Student ID for update, enter 'exit' to quit: ")
            if (student_id == "exit"):
                break

            # Check if the student ID exists in the database
            self.mycursor.execute("SELECT StudentId FROM Student WHERE StudentId = ?", (student_id,))
            studentId_input = self.mycursor.fetchone()

            # Choose the field
            if (studentId_input):
                field_to_update = input("Enter the field to update: (Major, FacultyAdvisor, MobilePhoneNumber) ")

                # Update field
                if field_to_update not in ['Major', 'FacultyAdvisor', 'MobilePhoneNumber']:
                    print("Invalid field. Please enter: ('Major', 'FacultyAdvisor', or 'MobilePhoneNumber') ")
                else:
                    new_value = input(f"Enter the new value for {field_to_update}: ")
                    #all values work if not empty
                    if new_value.strip() != "":
                        self.mycursor.execute((f"UPDATE Student SET {field_to_update} = ? WHERE StudentId = ?"), (new_value, student_id))
                        break
                    else:
                        print("Invalid Input, enter non-empty TEXT")
            else:
                print("Invalid StudentId")

        self.conn.commit()
    def softDeleteStudent(self):
        while True:
            student_id = input("Enter Student ID for delete, enter 'exit' to quit: ").strip().lower()
            if (student_id == "exit"):
                 break

            # Check if the student ID exists in the database
            self.mycursor.execute("SELECT StudentId FROM Student WHERE StudentId = ?", (student_id,))
            studentId_input = self.mycursor.fetchone()

            # Delete student query
            if (studentId_input):
                self.mycursor.execute(f"UPDATE Student SET isDeleted = ? WHERE StudentId = ?", (1,student_id))

            else:
                print("Invalid StudentId")
                continue

        self.conn.commit()
    def searchStudents(self):
        while True:
            user_input = input("Search by Major, GPA, City, State, or Advisor (or 'exit' to quit): ").strip().lower()
            if user_input == 'exit':
                break

            elif user_input == "major":
                while True:
                    major = input("Enter Major, enter 'exit' to quit: ")
                    if (major == "exit"):
                        break
                    # Check if value exists
                    self.mycursor.execute("SELECT * FROM Student WHERE Major = ?", (major,))
                    students = self.mycursor.fetchall()
                    if students:
                        for student in students:
                            print(student)
                    else:
                        print("Not valid entry")

            elif user_input == "gpa":
                while True:
                    GPA = input("Enter GPA, enter 'exit' to quit: ")
                    if (GPA == "exit"):
                        break
                    # Check if value exists
                    self.mycursor.execute("SELECT * FROM Student WHERE GPA = ?", (GPA,))
                    students = self.mycursor.fetchall()
                    if students:
                        for student in students:
                            print(student)
                    else:
                        print("Not valid entry")

            elif user_input == "city":
                while True:
                    city = input("Enter City, enter 'exit' to quit: ")
                    if (city == "exit"):
                        break
                    # Check if value exists
                    self.mycursor.execute("SELECT * FROM Student WHERE City = ?", (city,))
                    students = self.mycursor.fetchall()
                    if students:
                        for student in students:
                            print(student)
                    else:
                        print("Not valid entry")

            elif user_input == "state":
                while True:
                    state = input("Enter State, enter 'exit' to quit: ")
                    if (state == "exit"):
                        break
                    # Check if value exists
                    self.mycursor.execute("SELECT * FROM Student WHERE State = ?", (state,))
                    students = self.mycursor.fetchall()
                    if students:
                        for student in students:
                            print(student)
                    else:
                        print("Not valid entry")

            elif user_input == "advisor":
                while True:
                    advisor = input("Enter Advisor, enter 'exit' to quit: ")
                    if (advisor == "exit"):
                        break
                    # Check if value exists
                    self.mycursor.execute("SELECT * FROM Student WHERE FacultyAdvisor = ?", (advisor,))
                    students = self.mycursor.fetchall()
                    if students:
                        for student in students:
                            print(student)
                    else:
                        print("Not valid entry")
            else:
                print("Invalid field.")
                continue
    def mainMenu(self):
        validInputs = [1,2,3,4,5,6]
        mainInput = ""
        while True:
            mainInput = input("Enter 1: importData()"
                              "\nEnter 2: printData()"
                              "\nEnter 3: updateStudent()"
                              "\nEnter 4: deleteStudent()"
                              "\nEnter 5: searchStudents()"
                              "\nEnter 6: QUIT\n")
            try:
                if (int(mainInput) == 1):
                    db.importData()
                elif (int(mainInput) == 2):
                    db.printData()
                elif (int(mainInput) == 3):
                    db.updateStudent()
                elif (int(mainInput) == 4):
                    db.softDeleteStudent()
                elif (int(mainInput) == 5):
                    db.searchStudents()
                elif (int(mainInput) == 6):
                    break
            except:
                print("Enter in valid option")
                continue

        self.mycursor.close()
        self.conn.close() 


db = StudentDatabase(db_file)
db.mainMenu()
