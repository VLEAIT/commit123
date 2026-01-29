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


sum =0 
for sumation in [1,3,4,1,23,123,123,231]:
    sum =sum +sumation
    print(sum , sumation)
print(sum)    

count = 0
add =0
average =0
for number in [1,32,4345,123,54,23]:
    count=count +1
    add=add +number
    average = add / count

print(average)
   
print('before')

for ok in [1,23,412,41251,12314,1231]:
    if ok >50:
        print("the value ", ok)
print('after')    


# just want to new repo


smalls =[1,3,4,12,4,123,123,123,123123,123]
no = 100
for small in smalls:
    if small < 100:
        no == small
print(no)


for i in range(1,10,1):
    print(i)


# searching using a boolean variable
found = False
for check in [1,4,3,6,1,2,6,31,6,123,213]:
    if check == 1:
        found =True

print(found, check)
    
print("the vlaue of 1 is", found)

# use of is and is not operators
sv = None
for small in [1,2,3,4,5,6,7,8,9]:
    if sv is None:
        sv = small
    elif small < sv:
        sv = small 
    print(small ,sv)

print('after', sv)

# string data type

# fruits = input('what is your fvb')
fruits ="banana"
index = 0
while index <len(fruits):
    letter =  fruits[index]
    print(letter,index)
    index =index +1

# word = input("Enter a word")
word = "aeiou"
gu = ["a","e","i","o","u"]
co = 0

for leter in word:
    if leter in gu:
        co =co+1
print(co)

# slicing string 

s ="nishant python"
print(s[0:4])
print(s[6:7])
print(s[6:20])
print(s[:4])
print(s[8:])
print(s[:])

# string concatenation

a = "vision"
b = a + "thapa"
print("b")
c = a+' '+ b[6:]
print(c)

if "a" in c :
    print("found it")

# string comaparision 
# word = input("write a word")
word ="hello"
 # so when word are comapre aka string they are lexographincally
if word == "banana":
    print('all right ,bannas')

if word < 'banana': 
       print('your word,'+ word + ',comes before banana')
elif word > 'banana':
    print('your word' + word + 'comes after banana')
else:
    print("all done")           


# string library 

greet  ="hello bob"
zap = greet.lower()
print(zap)
print(greet)

print('hello and go ther'.upper())

stuff ="hello world"
type(stuff)
dir(stuff)