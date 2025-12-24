class FitnessTracker:
    def __init__(self, name, age, height, weight):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight

    def calculate_bmi(self):
        bmi = self.weight / (self.height ** 2)
        return round(bmi, 2)

    def track_activity(self):
        self.steps = int(input("Enter steps walked today: "))
        self.water = float(input("Enter water intake (liters): "))
        self.exercise_time = int(input("Enter exercise time (minutes): "))
        self.calories = self.steps * 0.04

    def save_data(self):
        with open("fitness_data.txt", "a") as file:
            file.write(f"Name: {self.name}\n")
            file.write(f"Age: {self.age}\n")
            file.write(f"BMI: {self.calculate_bmi()}\n")
            file.write(f"Steps: {self.steps}\n")
            file.write(f"Water Intake: {self.water} liters\n")
            file.write(f"Exercise Time: {self.exercise_time} minutes\n")
            file.write(f"Calories Burned: {self.calories}\n")
            file.write("-" * 30 + "\n")
        print("Data saved successfully!")

    def view_history(self):
        try:
            with open("fitness_data.txt", "r") as file:
                print("\n--- Fitness History ---")
                print(file.read())
        except FileNotFoundError:
            print("No fitness data found.")

print("==== Personal Fitness Tracker ====")

name = input("Enter your name: ")
age = int(input("Enter your age: "))
height = float(input("Enter height in meters: "))
weight = float(input("Enter weight in kg: "))
user = FitnessTracker(name, age, height, weight)

while True:
    print("\n1. Calculate BMI")
    print("2. Track Daily Activity")
    print("3. Save Fitness Data")
    print("4. View Fitness History")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        print("Your BMI is:", user.calculate_bmi())

    elif choice == 2:
        user.track_activity( )
        print("Activity recorded successfully!")

    elif choice == 3:
        user.save_data( )

    elif choice == 4:
        user.view_history( )

    elif choice == 5:
        print("Thank you for using Fitness Tracker!")
        break

    else:
        print("Invalid choice! Try again.")