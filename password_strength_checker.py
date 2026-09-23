password = input("Enter the password : ")
#Uppercase
uppercase = False
for char in password:
    if char.isupper():
        uppercase = True
if uppercase:
            print("Uppercase : Yes")
else:
    print("Uppercase: No")


#lowercase
lowercase = False
for char in password:
    if char.islower():
        lowercase = True

if lowercase:
    print("Lowercase : Yes")
else:
    print("Lowercase: No")


#digit
digit = False
for char in password:
     if char.isdigit():
          digit = True
if digit:
     print ("Digit : Yes")
else:
    print("Digit : No")


#special
special = False
for char in password:
    if not char.isdigit() and not char.isalpha() and char!=" ":
         special = True

if special:
    print("Special : Yes") 
else:
    print("Special: No")


#length
length = False
if len(password) >= 8:
    length = True
if length:
    print("Length: Yes")
else:
    print("Length: No")


#score calculate
score = 0
if uppercase:
    score +=1
if lowercase:
    score +=1
if digit:
    score +=1
if special: 
    score +=1
if length:
    score +=1

#pswrd strength
if score == 5:
    print("Strong")
elif score >= 3:
    print("Medium")
else:
    print("Weak")