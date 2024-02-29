def display_person (**person):
    for key,value in person.items():
        print(f"{key} : {value}")

display_person(name="John",age=25)


numbers =[7,6,5,5,3,2,1]
print(numbers[-4])


numbers =[22,19,19,14,33]
numbers.sort()
print(numbers)