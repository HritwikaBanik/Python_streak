from random import randint

class Train:
    def __init__(self, trainNo):
        self.trainNo = trainNo
    
    def book_tickets(self, to, fro):
        print("Tickets booked for train number {} from {} to {}".format(self.trainNo, fro, to))
    
    def get_status(self, seats):
        print("Status for number of seats {} for train number {}".format(seats, self.trainNo))
    
    def get_fareInformation(self):
        print("Fare for AC is {} , and for Non-AC is {} - train number {}".format(
            randint(2000, 5000), randint(1500, 2000), self.trainNo))

# Example usage:
train = Train(12345)
train.book_tickets("Delhi", "Mumbai")
train.get_status(50)
train.get_fareInformation()
