# Question one
for i in range (151):
    print(i)
    

# Question Two
for i in range (5, 1001, 5):
    print (i)


# Question Three
for i in range(1,101):
    if i % 10 !=0 and i % 5 ==0:
            print ("Coding")
    elif i % 10 == 0: 
            print ("Coding Dojo")
    else:
            print(i)


# Question four
    i = 0
for add in range (1, 500001, 2):
    i = i + add
        print(i)



# Question Five
for i in range (2018, 0, -4):
        print(i)


# Question six
lownum= int(input('num_1:'))
highnum = int(input('num_2:'))
mult = int(input('num_3:'))

for i in range (lownum,highnum +1,1):
    if i % mult == 0:
        print(i)