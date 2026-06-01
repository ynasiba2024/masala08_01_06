#8-masala
class Teacher:
    def __init__(self, name, experience):
        self.name = name
        self.__experience = experience

    @property
    def experience(self):
        return self.__experience

    @experience.setter
    def experience(self, years):
        self.__experience = years

t1 = Teacher("Aziz", 5)

print(t1.experience)

t1.experience = 10
print(t1.experience)
