
class Device:
    def __init__(self, brand, model, battery_percent=80):
        self.brand=brand
        self.model=model
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

    def charge(self,percent):
        if percent<=0:
            print("Charge amount must be positive.")
            return
        self.battery_percent+=percent
        if self.battery_percent>100:
            self.battery_percent=100
        print(f"Charged phone to {self.battery_percent}%.")

    def __str__(self):
        return f"{self.brand} {self.model} {self.storage_in_gb}GB - Battery: {self.battery_percent}%."

class Smartphone(Device):
    def __init__(self, brand, model, storage_in_gb, color, battery_percent=100):
        super().__init__(brand, model, battery_percent)
        self.storage_gb = storage_in_gb
        self.color = color

    def use_phone(self, hours):
        if self.is_on:
            battery_drain = hours * 10
            if battery_drain > self.battery_percent:
                print("Battery too low to use that long!")
            else:
                self.battery_percent -= battery_drain
                print(f"Used phone for {hours} hours. Battery at {self.battery_percent}%.")
        else:
            print("Can't use phone. It is OFF.")

    def __str__(self):
        return f"{self.brand} {self.model} ({self.color}, {self.storage_gb}GB) - Battery: {self.battery_percent}%"

class Tablet(Device):
    def __init__(self, brand, model, screen_size_inches, battery_percent=100):
        super().__init__(brand, model, battery_percent)
        self.screen_size_inches = screen_size_inches

    def watch_video(self, hours):
        if self.is_on:
            battery_drain = hours * 8
            if battery_drain > self.battery_percent:
                print("Battery too low to watch that long!")
            else:
                self.battery_percent -= battery_drain
                print(f"Watched videos for {hours} hours. Battery at {self.battery_percent}%.")
        else:
            print("Can't watch videos. The device is OFF.")

    def __str__(self):
        return f"{self.brand} {self.model} ({self.screen_size_inches}\" screen) - Battery: {self.battery_percent}%"



# Example of creating and using smartphone.
if __name__=="__main__":
    phone = Smartphone("Apple", "iPhone 14", 128, "Silver")
    tablet = Tablet("Samsung", "Galaxy Tab S9", 11)
    print(phone)

    phone.power_on()
    phone.use_phone(4)
    phone.charge(16)
    phone.power_off()

    print(tablet)
    tablet.power_on()
    tablet.watch_video(5)
    tablet.charge(13)
    tablet.power_off()




