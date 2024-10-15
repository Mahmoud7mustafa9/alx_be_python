from book_class import Book
from polymorphism_demo import Shape, Rectangle, Circle
import math
from class_static_methods_demo import Calculator

# def main():
#     # Creating an instance of Book
#     my_book = Book("1984", "George Orwell", 1949)

#     # Demonstrating the __str__ method
#     print(my_book)  # Expected to use __str__

#     # Demonstrating the __repr__ method
#     print(repr(my_book))  # Expected to use __repr__

#     # Deleting a book instance to trigger __del__
#     del my_book



def main():
    shapes = [
        Rectangle(10, 5),
        Circle(7)
    ]

    for shape in shapes:
        print(f"The area of the {shape.__class__.__name__} is: {shape.area()}")    


# Expected Output:
# 1984 by George Orwell, published in 1949
# Book('1984', 'George Orwell', 1949)
# Deleting 1984


def main():
    # Using the static method
    sum_result = Calculator.add(10, 5)
    print(f"The sum is: {sum_result}")

    # Using the class method
    product_result = Calculator.multiply(10, 5)
    print(f"The product is: {product_result}")

if __name__ == "__main__":
    main()