class Parent():
    def __init__(self, last_name, eye_color):
        print ("Parent Constructor is called")
        self.last_name = last_name
        self.eye_color = eye_color


class Child(Parent):
    def __init__(self, last_name, eye_color, number_of_toys):
        print("Child Constructor is called")
        Parent.__init__(self, last_name, eye_color)
        self.number_of_toys = number_of_toys

#billy_cosby = Parent("Billy", "red")
#print (billy_cosby.eye_color)

miley_cosby = Child("Miley", "blue", 5)
print(miley_cosby.last_name)
print(miley_cosby.number_of_toys)


