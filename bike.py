class RoyalEnfield:
    def __init__(self,model_name,color,mileage):
        self.model_name=model_name
        self.color=color
        self.mileage=mileage

bike1=RoyalEnfield("abc","white","40")
bike2=RoyalEnfield("edf","black","30")
bike3=RoyalEnfield("wed","brown","45")
print(bike1.model_name,bike1.color,bike1.mileage)

print(bike2.model_name,bike2.color,bike2.mileage)

print(bike3.model_name,bike3.color,bike3.mileage)