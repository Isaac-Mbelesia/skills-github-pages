import math

def calculate_square():
    side = float(input("Enter the length of the side of the square: "))
    area = side ** 2
    perimeter = 4 * side
    print(f"Area of the square: {area}")
    print(f"Perimeter of the square: {perimeter}")

def calculate_rectangle():
    length = float(input("Enter the length of the rectangle: "))
    width = float(input("Enter the width of the rectangle: "))
    area = length * width
    perimeter = 2 * (length + width)
    print(f"Area of the rectangle: {area}")
    print(f"Perimeter of the rectangle: {perimeter}")

def calculate_circle():
    radius = float(input("Enter the radius of the circle: "))
    area = math.pi * (radius ** 2)
    circumference = 2 * math.pi * radius
    print(f"Area of the circle: {area}")
    print(f"Circumference of the circle: {circumference}")

def calculate_triangle():
    base = float(input("Enter the base of the triangle: "))
    height = float(input("Enter the height of the triangle: "))
    side1 = float(input("Enter the length of the first side: "))
    side2 = float(input("Enter the length of the second side: "))
    side3 = float(input("Enter the length of the third side: "))
    area = 0.5 * base * height
    perimeter = side1 + side2 + side3
    print(f"Area of the triangle: {area}")
    print(f"Perimeter of the triangle: {perimeter}")

def main():
    while True:
        print("\nChoose a figure to calculate area and perimeter:")
        print("1. Square")
        print("2. Rectangle")
        print("3. Circle")
        print("4. Triangle")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            calculate_square()
        elif choice == "2":
            calculate_rectangle()
        elif choice == "3":
            calculate_circle()
        elif choice == "4":
            calculate_triangle()
        elif choice == "5":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
