# --- Day 8: Object-Oriented Programming (OOP) ---

# --- 1. Class and Object ---
print("\n--- Class and Object ---")
class Person:
    def say_hello(self):
        print("Hello!")

p = Person()
p.say_hello()


# --- 2. Constructor and Instance Variables ---
print("\n--- Constructor and Instance Variables ---")
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f"Name: {self.name}, Age: {self.age}")

p1 = Person("Pranav", 21)
p1.show()


# --- 3. Class Variable vs Instance Variable ---
print("\n--- Class vs Instance Variable ---")
class Student:
    school_name = "AI School"  # class variable

    def __init__(self, name):
        self.name = name  # instance variable

s1 = Student("Raj")
s2 = Student("Neha")

print(s1.name, "-", s1.school_name)
print(s2.name, "-", s2.school_name)


# --- 4. Inheritance ---
print("\n--- Inheritance ---")
class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def bark(self):
        print("Dog barks")

d = Dog()
d.speak()  # inherited method
d.bark()


# --- 🧠 Mini Challenges ---

# Challenge 1: Car Class
print("\n--- Challenge 1: Car Class ---")
class Car:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

    def display_info(self):
        print(f"Brand: {self.brand}, Year: {self.year}")

car1 = Car("Toyota", 2020)
car1.display_info()


# Challenge 2: Employee and Manager
print("\n--- Challenge 2: Inheritance ---")
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def show_info(self):
        print(f"Name: {self.name}, Salary: {self.salary}")

class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department

    def show_info(self):
        super().show_info()
        print(f"Department: {self.department}")

mgr = Manager("Aniket", 50000, "Tech")
mgr.show_info()


# Challenge 3: Bank Account
print("\n--- Challenge 3: BankAccount Class ---")
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"{amount} deposited. New balance: {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance.")
        else:
            self.balance -= amount
            print(f"{amount} withdrawn. New balance: {self.balance}")

acc = BankAccount("Pranav", 1000)
acc.deposit(500)
acc.withdraw(300)
acc.withdraw(1500)
