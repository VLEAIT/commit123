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
        elif 15 <= self.P <= 40:
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
          self.Deficit_N = self.N-self.reqRice_N
          self.Deficit_P = self.P-self.reqRice_P
          self.Deficit_K = self.K-self.reqRice_K
       elif self.crop == "Tomato":
          self.Deficit_N = self.N-self.reqTomo_N
          self.Deficit_P = self.P-self.reqTomo_P
          self.Deficit_K = self.K-self.reqTomo_K
       elif self.crop == "Potato":
          self.Deficit_N = self.N-self.reqPota_N
          self.Deficit_P = self.P-self.reqPota_P
          self.Deficit_K = self.K-self.reqPota_K

    def need(self):
       self.reqN =self.Deficit_N/10000
       self.reqP =self.Deficit_P/10000
       self.reqK=self.Deficit_K/10000
       self.reqNm = self.reqN *self.area
       self.reqPm=self.reqP*self.area
       self.reqKm=self.reqK*self.area
       self.UreaNeed =self.reqNm / 0.46
       self.MapNeed =self.reqPm /0.46
       self.DapNeed =self.reqKm /0.60

    def soil_sco(self):
         self.soil_quality =(self.Nutrient_P+self.Nutrient_N+self.Nutrient_K)/3

    def display(self):
       print("soil summary")
       print("Soil Score outof 3 is",self.soil_quality)
       print("Required Urea is",self.UreaNeed) 
       print("Required MAP is", self.MapNeed)
       print("Required DAP is ",self.DapNeed)

   
  
soil = Soil_calci()

soil.npk_input()
soil.imp_input()
soil.input()
soil.amount()
soil.calculation()
soil.need() 
soil.soil_sco()
soil.display()  
    

