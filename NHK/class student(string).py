class student():
    def __init__(self,name,grade):
        self.name = name
        self.grade = grade
    @property
    def name(self):
        return self.name
    @property
    def grade(self):
        return self.grade
    @name.setter
    def name(self,value):
        self.name = value
    @grade.setter
    def grade(self,value):
        self.grade = value
    def __str__(self):
        return f'{self.name} {self.grade}'
    s1 = ("NHK",9)
    print(s1)
