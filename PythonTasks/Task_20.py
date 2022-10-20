
# Task 20


#Create a class called Human

#Add an attribute leg_count with the value of 4

#Add a method called get_gender() that returns "Unknown" in the Human class

#Create another class called Man that extends Human

class Human:
    leg_count = 4

    def get_gender(self):
        return "Unknown"


human = Human()
print(human.get_gender())


class Man(Human):
    pass


class Woman(Human):
    pass


man1 = Man()
woman1 = Woman()
print(man1.get_gender())
print(woman1.get_gender())