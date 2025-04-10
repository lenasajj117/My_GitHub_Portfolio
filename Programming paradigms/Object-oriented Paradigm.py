class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print("Hello, " + self.name + "!")

def main():
    user = Person(input("Enter your name: "))
    user.greet()

if __name__ == "__main__":
    main()
