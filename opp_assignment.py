
class Smartphone:
    def __init__(self, brand, model, storage_in_gb, battery_percent=80):
        self.brand=brand
        self.model=model
        self.storage_in_gb=storage_in_gb
        self.battery_percent=battery_percent
        self.is_on=False

    def  power_on(self):
        if not self.is_on:
            self.is_on=True
            print(f"{self.brand} {self.model} is now ON.")
        else:
            print(f"{self.brand} {self.model} is already ON.")

    def power_off(self):
        if self.is_on:
            self.is_on=False
            print(f"{self.brand} {self.model} is now OFF.")
        else:
         print(f"{self.brand} {self.model} is now ON.")
    def use_phone(self,hours):
        if self.is_on:
            battery_darin=hours*10  #Assume 10% of battery used per hour
            if battery_darin>self.battery_percent:
                print("Battery too low use that long! Please charge your phone.")

            else:
                self.battery_percent-=battery_darin
                print(f"Used phone for {hours} hours. Battery as {self.battery_percent}%.")
        else:
            print("Can't use phone. It is OFF.")
    def charge(self,percent):
        if percent<=0:
            print("Charge amout must be positive.")
            return
        self.battery_percent+=percent
        if self.battery_percent>100:
            self.battery_percent=100
        print(f"Charged phone to {self.battery_percent}%.")

    def __str__(self):
        return f"{self.brand} {self.model} {self.storage_in_gb}GB - Battery: {self.battery_percent}%."

# Example of creating and using smartphone.
if __name__=="__main__":
    apple=Smartphone("Apple",'iPhone 14', 128,)
    samsung=Smartphone("samsung",'Galaxy S23', 256, battery_percent=75)
    print(apple)

    apple.power_on()
    apple.use_phone(4)
    apple.charge(16)
    apple.power_off()

print(samsung)
samsung.power_on()
samsung.use_phone(5)
samsung.charge(13)
samsung.power_off()




