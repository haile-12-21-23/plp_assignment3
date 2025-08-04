class Car:
    def move(self):
        print("🚗 Driving on the road!")

class Plane:
    def move(self):
        print("✈️ Flying in the sky!")

class Boat:
    def move(self):
        print("🚤 Sailing on the water!")

if __name__=="__main__":

    try:
# List of vehicles
      vehicles = [Car(), Plane(), Boat()]
      vehicles[0].move()
# Loop through and call move()
      for vehicle in vehicles:
            vehicle.move()

    except Exception as e:
        print('An error occurred.')


