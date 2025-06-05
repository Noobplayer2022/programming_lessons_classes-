class Student:
    def __init__(self, name, grade, nat_id):
        self.name = name
        self.grade = grade
        self.nat_id = nat_id
        self.courses = []
        self.meal = False

    def book_meal(self, meal):
        if self.meal:
            print(self.name, "already booked a", meal)
        else:
            self.meal = True
            print("Booked", meal, "for", self.name)

    def add_course(self, course, credits):
        if course in [c["name"] for c in self.courses]:
            print(self.name, "is already in", course)
        else:
            self.courses.append({"name": course, "credits": credits})
            print(self.name, "added to", course, "-", credits, "credits")

    def show_info(self):
        print("Name:", self.name)
        print("grade:", self.grade)
        print("ID:", self.nat_id)
        print("Courses:")
        for c in self.courses:
            print(" -", c["name"], "(", c["credits"], "credits )")
        print("Meal Booked:", "Yes" if self.meal else "No")


n = int(input("How many students? "))

students = []

for i in range(n):
    print("\nStudent", i + 1, "details:")
    name = input("Name: ")
    grade = float(input("grade: "))
    nat_id = input("National ID: ")
    
    s = Student(name, grade, nat_id)
    
    meal = input("Meal to book: ")
    s.book_meal(meal)
    
    num = int(input("How many courses? "))
    for j in range(num):
        course = input("Course name: ")
        credits = int(input("Credits: "))
        s.add_course(course, credits)
    
    students.append(s)

print("\nAll Students:")
for i, s in enumerate(students, 1):
    print("\nStudent", i)
    s.show_info()