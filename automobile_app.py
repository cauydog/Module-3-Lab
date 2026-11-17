# Name: Cauy Whaley
# File: automobile_app.py
# Description: Collects automobile information using a Vehicle superclass
# and an Automobile subclass, then displays the details.


class Vehicle:
    def __init__(self, vehicle_type):
        self.vehicle_type = vehicle_type


class Automobile(Vehicle):
    def __init__(self, year, make, model, doors, roof):
        super().__init__("car")
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof

    def display_information(self):
        print("\nAutomobile Information")
        print("----------------------")
        print(f"Vehicle type: {self.vehicle_type}")
        print(f"Year: {self.year}")
        print(f"Make: {self.make}")
        print(f"Model: {self.model}")
        print(f"Number of doors: {self.doors}")
        print(f"Type of roof: {self.roof}")


def main():
    print("Enter your automobile information:")
    year = input("Year: ")
    make = input("Make: ")
    model = input("Model: ")

    doors = input("Number of doors (2 or 4): ").strip()
    while doors not in ("2", "4"):
        doors = input("Please enter 2 or 4 doors: ").strip()

    roof = input("Type of roof (solid or sun roof): ").strip().lower()
    while roof not in ("solid", "sun roof"):
        roof = input("Please enter solid or sun roof: ").strip().lower()

    car = Automobile(year, make, model, int(doors), roof)
    car.display_information()


if __name__ == "__main__":
    main()
