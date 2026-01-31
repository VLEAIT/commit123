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
