class Soil_calci:
    def npk_input(self):
       self.N =float(input("Enter the value of Nitrogen"))
       self.P = float(input("Enter the value of Potassiun"))
       self.K = float(input("Enter the value of Phosphorous"))
       print("npk value entered")


    def imp_input(self):
       self.area=float(input("Enter the area in m2"))
       self.crop=str(input("Enter the crop of whcih to add"))
       self.stage=str(input("Enter the stage of vegetable")) 
       print("Value entered")

    def input(self):
        if  self.N < 50 :
           self.Nutrient_N = 1
           self.Nutrient_NV = "Low"
           print(" n =",self.N,"Low")
        elif 50 <= self.N <=120:
           self.Nutrient_N = 2
           self.Nutrient_NV = "Medium"
           print(" n =",self.N,"Medium")
        elif self.N>120:
           self.Nutrient_N=3
           self.Nutrient_NV="High"
           print(" n =",self.N,"High")
        else:
           print("enter correct value")
        
        if self.P < 15:
           self.Nutrient_P = 1
           self.Nutrient_PV ="Low"
           print(" p =",self.P,"Low")
        elif 15 <= self.p <= 40:
           self.Nutrient_P = 2
           self.Nutrient_PV ="Medium"
           print(" p =",self.P,"Medium")
        elif self.P > 40:
           self.Nutrient_P =3
           self.Nutrient_PV ="High"
           print(" p =",self.P,"High")
        else:
           print("enter correct value")

        if self.K  < 80:
           self.Nutrient_K = 1
           self.Nutrient_KV ="Low"
           print(" k =",self.K,"low")
        elif 80 <= self.K <=200:
           self.Nutrient_K = 2
           self.Nutrient_KV ="Medium"
           print(" k =",self.K,"Medium")
        elif self.K > 200:
           self.Nutrient_K =3
           self.Nutrient_KV = "High"
           print(" k =",self.K,"High")
        else:
           print( "enter correct value")    