#Each person has a name, age and city
#application will be able to add a person to a list (in memory)
#after addition, the application will be able to print all the people in the list

person_list = []

while True:

    person_name = input("Enter your name: ")
    person_age = input("Enter your age: ")
    person_city = input("Enter your city: ")

    person = {
        "name": person_name,
        "age": person_age,
        "city": person_city
    }

    person_list.append(person)

    for p in person_list:
        print(f"Name: {p['name']}, Age: {p['age']}, City: {p['city']}")