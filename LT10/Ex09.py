class Person:
    count = 0

    def __init__(self, name, age):
        if age < 0:
            raise ValueError("Tuổi không hợp lệ")
        self._name = name
        self._age = age
        Person.count += 1

    # getter setter
    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if value < 0:
            raise ValueError("Tuổi phải >= 0")
        self._age = value

    def __str__(self):
        return f"{self._name} - {self._age}"

    def info(self):
        return f"Tên: {self._name}"

    @classmethod
    def get_count(cls):
        return cls.count

    @staticmethod
    def hello():
        return "Hello"

    def __eq__(self, other):
        return self._age == other._age


class Student(Person):
    def __init__(self, name, age, score):
        super().__init__(name, age)
        if score < 0:
            raise ValueError("Điểm không hợp lệ")
        self.score = score

    def __str__(self):
        return f"{self._name} - {self._age} - {self.score}"


# test
p1 = Person("Nam", 20)
p2 = Person("An", 20)

s1 = Student("Khang", 18, 9)

print(p1)
print(s1)
print(p1 == p2)
print(Person.get_count())
print(Person.hello())