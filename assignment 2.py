# Write a Python program that accepts a word from the user and reverse it.

# Input : Edyoda

# output: adoydE



# word=input("Enter word for reverse --> ")
# print(word[::-1])


word=input("Enter word for reverse --> ")
str=" "
for i in word:
    str=i+str
print("Reverse string is -->",word,"==>",str,end=" ")  


# Output -->
# Enter word for reverse --> Edyoda
# Reverse string is --> Edyoda ==> adoydE
 











     