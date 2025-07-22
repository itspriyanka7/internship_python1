# Task 1: Decorator Implementation
# Create a decorator that logs function execution details.

# Create a decorator called log_execution that:
# Records the timestamp when the function starts
# Records the timestamp when the function ends
# Logs the function name, execution time, and arguments
# Preserves the original function's return value
# Apply this decorator to at least two different functions and demonstrate its usage


import time
import functools

# Decorator to log function execution details
def log_execution(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        print(f"[START] Function '{func.__name__}' called with args={args}, kwargs={kwargs}")
        
        result = func(*args, **kwargs)
        
        end_time = time.time()
        exec_time = end_time - start_time
        print(f"[END] Function '{func.__name__}' finished in {exec_time:.4f} seconds")
        return result
    return wrapper

# Sample function 1
@log_execution
def add(a, b):
    time.sleep(1)
    return a + b

# Sample function 2
@log_execution
def greet(name):
    time.sleep(0.5)
    return f"Hello, {name}!"

# Demonstrate usage
print(add(5, 10))
print(greet("Priya"))


# Task 2: Class and Object Implementation 

# Create a Student class to manage student information.
# Create a Student class with:
# Attributes: name, student_id, courses (dictionary to store course names and grades)
# Methods:
# enroll(course_name): Adds a course with default grade None
# update_grade(course_name, grade): Updates grade for a course
# calculate_gpa(): Returns average of all grades (ignore None values)
# display_info(): Shows all student information
# Create at least two Student objects and demonstrate all methods

# class Student:
#     def __init__(self, name, student_id):
#         self.name = name
#         self.student_id = student_id
#         self.courses = {}

#     def enroll(self, course_name):
#         if course_name not in self.courses:
#             self.courses[course_name] = None
#             print(f"{self.name} enrolled in {course_name}")
#         else:
#             print(f"{self.name} is already enrolled in {course_name}")

#     def update_grade(self, course_name, grade):
#         if course_name in self.courses:
#             self.courses[course_name] = grade
#             print(f"Grade updated for {course_name}: {grade}")
#         else:
#             print(f"{self.name} is not enrolled in {course_name}")

#     def calculate_gpa(self):
#         grades = [grade for grade in self.courses.values() if grade is not None]
#         if grades:
#             gpa = sum(grades) / len(grades)
#             return round(gpa, 2)
#         else:
#             return 0.0

#     def display_info(self):
#         print(f"\nStudent Name: {self.name}")
#         print(f"Student ID: {self.student_id}")
#         print("Courses and Grades:")
#         for course, grade in self.courses.items():
#             grade_display = grade if grade is not None else "Not Graded"
#             print(f"  - {course}: {grade_display}")
#         print(f"GPA: {self.calculate_gpa()}\n")

# # Create and use Student objects
# student1 = Student("Priyanka", "S101")
# student1.enroll("Math")
# student1.enroll("Science")
# student1.update_grade("Math", 85)
# student1.update_grade("Science", 90)
# student1.display_info()

# student2 = Student("Neha", "S102")
# student2.enroll("History")
# student2.update_grade("History", 78)
# student2.display_info()



# Task 3: Method Implementation
# Objective: Enhance the Student class with additional functionality.

# Add these methods to your Student class:
# - add_credits(course_name, credits): Store credit hours for each course
# - calculate_weighted_gpa(): Calculate GPA weighted by credit hours
# - get_highest_grade(): Returns the course name and highest grade
# - _str_: Returns a string representation of the student

# class Student:
#     def __init__(self, name, student_id):
#         self.name = name
#         self.student_id = student_id
#         self.courses = {}      # format: {course_name: grade}
#         self.credits = {}      # format: {course_name: credit_hours}

#     def enroll(self, course_name):
#         if course_name not in self.courses:
#             self.courses[course_name] = None
#             print(f"{self.name} enrolled in {course_name}")
#         else:
#             print(f"{self.name} is already enrolled in {course_name}")

#     def update_grade(self, course_name, grade):
#         if course_name in self.courses:
#             self.courses[course_name] = grade
#             print(f"Grade updated for {course_name}: {grade}")
#         else:
#             print(f"{self.name} is not enrolled in {course_name}")

#     def add_credits(self, course_name, credits):
#         if course_name in self.courses:
#             self.credits[course_name] = credits
#             print(f"Added {credits} credit(s) to {course_name}")
#         else:
#             print(f"{course_name} is not enrolled, so cannot assign credits")

#     def calculate_gpa(self):
#         grades = [grade for grade in self.courses.values() if grade is not None]
#         if grades:
#             gpa = sum(grades) / len(grades)
#             return round(gpa, 2)
#         return 0.0

#     def calculate_weighted_gpa(self):
#         total_points = 0
#         total_credits = 0
#         for course, grade in self.courses.items():
#             if grade is not None and course in self.credits:
#                 total_points += grade * self.credits[course]
#                 total_credits += self.credits[course]
#         if total_credits == 0:
#             return 0.0
#         weighted_gpa = total_points / total_credits
#         return round(weighted_gpa, 2)

#     def get_highest_grade(self):
#         valid_courses = {c: g for c, g in self.courses.items() if g is not None}
#         if not valid_courses:
#             return "No grades available"
#         highest_course = max(valid_courses, key=valid_courses.get)
#         return f"Highest Grade: {highest_course} - {valid_courses[highest_course]}"

#     def display_info(self):
#         print(f"\n{self}")
#         print("Courses, Grades, and Credits:")
#         for course, grade in self.courses.items():
#             grade_str = grade if grade is not None else "Not Graded"
#             credit_str = self.credits.get(course, "Not Assigned")
#             print(f"  - {course}: Grade = {grade_str}, Credits = {credit_str}")
#         print(f"GPA: {self.calculate_gpa()}")
#         print(f"Weighted GPA: {self.calculate_weighted_gpa()}")
#         print(self.get_highest_grade())

#     def __str__(self):
#         return f"Student(Name: {self.name}, ID: {self.student_id})"
