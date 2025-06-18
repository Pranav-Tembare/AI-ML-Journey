import re
import os

class Students:
    def data(self):
        try:
            name = input("Enter name: ").strip().capitalize()
            score = input("Enter score: ").strip()

            # Check if score is a 2- or 3-digit number
            if re.fullmatch(r"\d{2,3}", score):
                score = int(score)

                # Grade logic as per your rule
                if score >= 90:
                    grade = "A"
                elif score >= 80:
                    grade = "B"
                elif score >= 70:
                    grade = "C"
                else:
                    grade = "D"

                student = f"Name: {name}, Score: {score}, Grade: {grade}\n"
                print(student)

                with open("Students.txt", "a") as f:
                    f.write(student)
            else:
                print("Score must be a 2 or 3-digit number (e.g., 70–999).")

        except ValueError:
            print("Invalid input!")

    def all_students(self):
        if os.path.exists("Students.txt"):
                with open("Students.txt", "r") as f:
                    content = f.read()
                    print("\n--- All Students ---")
                    print(content if content else "No entries yet.")

        else:
            print("No student records found.")

# Run the method
sol = Students()
while True:
    print("\n# --- Menu ---")
    print("1]Add student")
    print("2]View all students list")
    print("3]Exit")

    try:
        user = int(input("Enter your choice here (1/2/3): "))
        if user == 1:
            sol.data()
        elif user == 2:
            sol.all_students()
        elif user == 3:
            exit()
    except ValueError:
        print("Invalid input! Enter number (1/2/3).")