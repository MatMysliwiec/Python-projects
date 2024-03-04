class Person:
    def __init__(self, name, birth_year, death_year=None):
        self.name = name
        self.birth_year = birth_year
        self.death_year = death_year
        self.children = []

    def add_child(self, child):
        self.children.append(child)


class FamilyTree:
    def __init__(self, root_person):
        self.root = root_person

    def display_tree(self, person, generation=0):
        indent = "  " * generation
        print(f"{indent}{person.name} ({person.birth_year}-{person.death_year or 'Present'})")

        for child in person.children:
            self.display_tree(child, generation + 1)


john = Person("John", 1980)
jane = Person("Jane", 1985)
bob = Person("Bob", 2000)
alice = Person("Alice", 2005)

john.add_child(jane)
john.add_child(bob)
jane.add_child(alice)

family_tree = FamilyTree(john)

family_tree.display_tree(john)
