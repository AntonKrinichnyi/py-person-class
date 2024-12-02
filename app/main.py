class Person:
    people = {}
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    persons_list = [Person(person["name"], person["age"])for person in people]
    for person in people:
        iterable_person = Person.people[person["name"]]
        if "wife" in person and person["wife"] and person["wife"] in persons_list is not None:
            iterable_person.wife = Person.people[person["wife"]]
        elif "husband" in person and person["husband"] and person["husband"] in persons_list is not None:
            iterable_person.husband = Person.people[person["husband"]]    
    return persons_list


people = [
    {"name": "Ross", "age": 30, "wife": "Rachel"},
    {"name": "Joey", "age": 29, "wife": None},
    {"name": "Rachel", "age": 28, "husband": "Ross"}
]

person_list = create_person_list(people) 
isinstance(person_list[0], Person) # True
person_list[0].name == "Ross"
person_list[0].wife is person_list[2] # True
person_list[0].wife.name == "Rachel"

person_list[1].name == "Joey"
person_list[1].wife
# AttributeError

isinstance(person_list[2], Person) # True
person_list[2].name == "Rachel"
person_list[2].husband is person_list[0] # True
# The same as person_list[0]
print(person_list[2].husband.name == "Ross")
print(person_list[2].husband.wife is person_list[2])  # True
