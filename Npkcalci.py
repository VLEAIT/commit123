class Soil_calci:
    def input(self,N,P,K):
        if  N < 50 :
           self.Nutrient_N = 1
           print(" n =",N,"Low")
        elif N>50 or N<120:
           self.Nutrient_N = 2
           print(" n =",N,"Medium")
        elif N>120:
           self.Nutrient_N=3
           print(" n =",N,"High")
        else:
           print("enter correct value")
        
        if P < 15:
           self.Nutrient_P = 1
           print(" p =",P,"Low")
        elif P > 15 or P <40:
           self.Nutrient_P = 2
           print(" p =",P,"Medium")
        elif P > 40:
           self.Nutrient_P =3
           print(" p =",P,"High")
        else:
           print("enter correct value")

        if K  < 80:
           self.Nutrient_K = 1
           print(" k =",K,"low")
        elif K >80 or K <200:
           self.Nutrient_K = 2
           print(" k =",K,"Medium")
        elif K > 200:
           self.Nutrient_K =3
           print(" k =",K,"High")
        else:
           print( "enter correct value")    