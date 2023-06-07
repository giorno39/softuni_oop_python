class Person:
    def __init__(self, name: str, surname: str):
        self.name = name
        self.surname = surname

    def __repr__(self):
        return f"{self.name} {self.surname}"

    def __add__(self, other):
        return Person(self.name, other.surname)


class Group:
    def __init__(self, name, people):
        self.name = name
        self.people = people

    def __len__(self):
        return len(self.people)

    def __add__(self, other):
        new_name = f"{self.name} {other.name}"
        new_people = self.people + other.people
        return Group(new_name, new_people)

    def __repr__(self):
        people = ", ".join([repr(p) for p in self.people])
        return f"Group {self.name} with members {people}"

    def __getitem__(self, idx):
        return f"Person {idx}: {repr(self.people[idx])}"

