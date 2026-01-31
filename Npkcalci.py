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
    
    def amount(self):
           self.reqRice_N = 120
           self.reqRice_P = 40
           self.reqRice_K = 40

           self.reqTomo_N = 200
           self.reqTomo_P = 150
           self.reqTomo_K =100

           self.reqPota_N =150
           self.reqPota_P =150
           self.reqPota_K =90

    def calculation(self):
       self.soil_score = (self.Nutrient_N+self.Nutrient_P+self.Nutrient_K)/3
       if self.crop == "Rice":
          self.Deficit_N = self.Nutrient_N-self.reqRice_N
          self.Deficit_P = self.Nutrient_P-self.reqRice_P
          self.Deficit_K = self.Nutrient_K-self.reqRice_K
       elif self.crop == "Tomato":
          self.Deficit_N = self.Nutrient_N-self.reqTomo_N
          self.Deficit_P = self.Nutrient_P-self.reqTomo_P
          self.Deficit_K = self.Nutrient_K-self.reqTomo_K
       elif self.crop == "Potato":
          self.Deficit_N = self.Nutrient_N-self.reqPota_N
          self.Deficit_P = self.Nutrient_P-self.reqPota_P
          self.Deficit_K = self.Nutrient_K-self.reqPota_K
             
          
    

