Use a dictionary to store people’s favorite numbers. Think of five names, and use them as keys in your dictionary. Think of a favorite number for each person, and store each as a value in your dictionary. Print each person’s name and their favorite number. For even more fun, poll a few friends and get some actual data for your program.

favorite_numbers = {
    'rahul': 42,
    'raj': 23,
    'raani': 7,
    'rejin': 1000_000,
    'nilima': 0,
    }

num = favorite_numbers['mandy']
print(f"rahul's favorite number is {num}.")

num = favorite_numbers['micah']
print(f"raj's favorite number is {num}.")

num = favorite_numbers['gus']
print(f"raani's favorite number is {num}.")

num = favorite_numbers['hank']
print(f"rejin's favorite number is {num}.")

num = favorite_numbers['maggie']
print(f"nilima's favorite number is {num}.")