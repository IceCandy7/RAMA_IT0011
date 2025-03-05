import json

class StudentRecordManager:
    def __init__(self):
        self.records = []
        self.filename = None
    
    def open_file(self, filename):
        try:
            with open(filename, 'r') as file:
                self.records = json.load(file)
            self.filename = filename
            print("File opened successfully.")
        except FileNotFoundError:
            print("File not found.")
    
    def save_file(self):
        if self.filename:
            with open(self.filename, 'w') as file:
                json.dump(self.records, file, indent=4)
            print("File saved successfully.")
        else:
            print("No file currently opened. Use 'Save As' option.")
    
    def save_as_file(self, filename):
        with open(filename, 'w') as file:
            json.dump(self.records, file, indent=4)
        self.filename = filename
        print("File saved as", filename)
    
    def show_all_records(self):
        if not self.records:
            print("No records available.")
        else:
            for record in self.records:
                print(record)
    
    def order_by_lastname(self):
        self.records.sort(key=lambda x: x[1][1])
        self.show_all_records()
    
    def order_by_grade(self):
        self.records.sort(key=lambda x: (0.6 * x[2] + 0.4 * x[3]), reverse=True)
        self.show_all_records()
    
    def show_student_record(self, student_id):
        for record in self.records:
            if record[0] == student_id:
                print(record)
                return
        print("Student not found.")
    
    def add_record(self, student_id, fullname, class_standing, major_exam):
        self.records.append((student_id, fullname, class_standing, major_exam))
        print("Record added successfully.")
    
    def edit_record(self, student_id, new_fullname=None, new_class_standing=None, new_major_exam=None):
        for i, record in enumerate(self.records):
            if record[0] == student_id:
                new_record = (
                    student_id,
                    new_fullname if new_fullname else record[1],
                    new_class_standing if new_class_standing else record[2],
                    new_major_exam if new_major_exam else record[3]
                )
                self.records[i] = new_record
                print("Record updated successfully.")
                return
        print("Student not found.")
    
    def delete_record(self, student_id):
        for i, record in enumerate(self.records):
            if record[0] == student_id:
                del self.records[i]
                print("Record deleted successfully.")
                return
        print("Student not found.")


if __name__ == "__main__":
    manager = StudentRecordManager()
    while True:
        print("\n\t  Menu")
        print("--------------------------")
        print("1.  Open File")
        print("2.  Save File")
        print("3.  Save As File")
        print("4.  Show All Students Record")
        print("5.  Order by Last Name")
        print("6.  Order by Grade")
        print("7.  Show Student Record")
        print("8.  Add Record")
        print("9.  Edit Record")
        print("10. Delete Record")
        print("11. Exit\n--------------------------")
        
        choice = input("Enter choice: ")
        if choice == "1":
            filename = input("Enter filename: ")
            manager.open_file(filename)
        elif choice == "2":
            manager.save_file()
        elif choice == "3":
            filename = input("Enter filename to save as: ")
            manager.save_as_file(filename)
        elif choice == "4":
            manager.show_all_records()
        elif choice == "5":
            manager.order_by_lastname()
        elif choice == "6":
            manager.order_by_grade()
        elif choice == "7":
            student_id = input("Enter Student ID: ")
            manager.show_student_record(student_id)
        elif choice == "8":
            student_id = input("Enter Student ID: ")
            first_name = input("Enter First Name: ")
            last_name = input("Enter Last Name: ")
            class_standing = float(input("Enter Class Standing: "))
            major_exam = float(input("Enter Major Exam Grade: "))
            manager.add_record(student_id, (first_name, last_name), class_standing, major_exam)
        elif choice == "9":
            student_id = input("Enter Student ID to edit: ")
            first_name = input("Enter New First Name (leave blank to keep current): ")
            last_name = input("Enter New Last Name (leave blank to keep current): ")
            class_standing = input("Enter New Class Standing (leave blank to keep current): ")
            major_exam = input("Enter New Major Exam Grade (leave blank to keep current): ")
            
            new_fullname = (first_name, last_name) if first_name and last_name else None
            new_class_standing = float(class_standing) if class_standing else None
            new_major_exam = float(major_exam) if major_exam else None
            
            manager.edit_record(student_id, new_fullname, new_class_standing, new_major_exam)
        elif choice == "10":
            student_id = input("Enter Student ID to delete: ")
            manager.delete_record(student_id)
        elif choice == "11":
            break
        else:
            print("Invalid choice. Please try again.")
