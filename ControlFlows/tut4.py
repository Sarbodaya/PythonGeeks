# Different Looping Techniques

# Using enumerate():  enumerate() is used to loop through the containers printing
# the index number along with the value present in that particular index.

for key, value in enumerate(['The', 'Big', 'Bang', 'Theory']):
    print(key, value)

for key, value in enumerate(['Geeks', 'for', 'Geeks', 'is', 'the', 'Best', 'coding', 'platform']):
    print(value, end=" ")

# Using zip(): zip() is used to combine 2 similar containers(list-list or dict-dict)
# printing the values sequentially. The loop exists only till the smaller container
# ends. A detailed explanation of zip() and enumerate() can be found here.
print()
question = ['name', 'colour', 'shape']
answers = ['apple', 'red', 'circle']

for question, answers in zip(question, answers):
    print(f"What is your {question} ? I am {answers}.")

# Using iteritem(): iteritems() is used to loop through the dictionary printing the
# dictionary key-value pair sequentially.
# Using items(): items() performs the similar task on dictionary as iteritems() but
# have certain disadvantages when compared with iteritems().

# Disadvantages
# It is very time-consuming. Calling it on large dictionaries consumes quite
# a lot of time.
# It takes a lot of memory. Sometimes takes double the memory when called
# on a dictionary.


d = {"geeks": "for", "only": "geeks"}
# print("The key value pair item using iteritems : ")
# for i, j in d.iteritem():
#     print(i, j)

print("The key value pair item using items : ")
for i, j in d.items():
    print(i, j)







