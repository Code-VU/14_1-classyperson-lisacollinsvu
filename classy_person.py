'''
Starter code!
don't forget the use of 'self' and to have the methods:
1. __init__
2. increase_age
3. say_greeting
4. count_to_age
'''

class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age
        

    def increase_age(self):
        self.age = self.age +1

    def say_greeting(self):
        print(f"Hello world! My name is {self.name}!")

    def count_to_age(self):
        for number in range(1, self.age+1):
            print(number)



# You won't need to call anything here.