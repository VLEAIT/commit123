asd = "hello world "
try:
    asd1 = int(asd)
except:
    asd1 = -1    
print(asd1)

print(10>5>2)
# try and except is used to like if else and each time peoplo use it is run program and see if it crashes and if then use another one
# if even one line of a block in try doesnot run then other statement also doesnot run
# ctrl + shift  + p and then type toggle suggest and click


# funtion chapter 4

def vision():
    print("helkko")
    print("reuse")

vision()
print('hello')
vision()

# def as in used to declare a function and vision is user defined name given to that function and it can be used to reuse code miltiple times 
big = max('abcdABCD')#max function is used to like find the alphabet that is in last of series in alphabet and a>A 
print(big)

small =min("abcd")#min is opposite of max
print(small)


def name(your):# your is parameter that user can have as well as the function name
    if your == "hero":
       print('i donot know')
    elif your == "gun":
        print('fuck you')
name("hero")
name('gun')

# return value 
def greet():
    return "hello"

print(greet(),"vision")


def new(A):
    if A == "hero":
        return A + "is hero"
    
print(new("hero"))    

# loops and iteration chapter 5

v =5 
while v>0:
    print(v)
    v=v-1
print('blastoff')


# loops 
for i in [5,4,3,2,1]:
    print(i)
print("blastoff")    

friends =["vision","suresh", "akash", "nepal" ]
for friend in friends:
    print('happy day', friend)
print('done!')    

# loop idioms

largest_number=-1
for the_num in [9,41,12,3,74,15]:
    if(the_num>largest_number):
        largest_number=the_num
print(largest_number)   

# more loop patterns
num =0
for thing in [1,2,3,4,62,231,231,54,12,3123,13]:
    num =num +1
    print(thing)
print("number is",num)    