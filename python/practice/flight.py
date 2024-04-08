class Flight:
    def __init__(self, capacity):
        self.capacity = capacity
        self.passengers = []
    
    def add_passenger(self, name):
        # if self.has_space():
        if not self.open_seats():
            return False
            # self.passengers.append(name)
            # return True

        self.passengers.append(name)
        return True            
            # return False
    
    # def has_space(self):
        # if self.capacity > len(self.passengers):
        #     return True
        # else:
        #     return False

    def open_seats(self):
        return self.capacity - len(self.passengers)

flightX = Flight(3)
flightX.add_passenger("Naruto")
names = ["Rock Lee", "Sasuke", "Sakura"]
print(flightX.passengers)

for name in names:
    if flightX.add_passenger(name):
        print(f"The passenger {name} was added successfully!")
    else:
        print(f"Unfortunately all seats are reservated and we got no space for {name}, bye!")


print(flightX.passengers)
