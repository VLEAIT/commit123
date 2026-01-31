N =input("value of nitrogen ")
P =input("value of potassium")
K =input("value of phosphorous")

if N < 50 :
    Nutrient_N = 1
elif N>50 or N<120:
    Nutrient_N = 2
elif N>120:
    Nutrient_N=3
else:
    print("enter correct value")

if P < 15:
    Nutrient_P = 1
elif P > 15 or P <40:
    Nutrient_P = 2
elif P > 40:
    Nutrient_P =3
else:
    print("enter correct value")

if K  < 80:
    Nutrient_K = 1
elif K >80 or K <200:
    Nutrient_K = 2
elif K > 200:
    Nutrient_K =3
else:
    print( "enter correct value")


