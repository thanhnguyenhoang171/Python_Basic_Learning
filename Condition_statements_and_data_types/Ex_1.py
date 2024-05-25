now_year = 2024
print ("What's is your firstname: ")
firstname = input()

print ("What's is your lastname: ")
lastname = input()

# connecting 2 strings together
print ("Your name is " +firstname + " " + lastname)

print ("When you were born: ")
year_born = int(input())

age = now_year-year_born
print ("You are "+ str(age) +" years old in "+ str(now_year))

sex = input("Are you male or female?: ")
height = int(input ("How tall are you?:  "))

if age >=18 and height>= 160:
    print ("You are mature!")
else:
    print ("You are still a child")