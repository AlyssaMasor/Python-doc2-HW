class Garage():

    
    def __init__(self, current_ticket, tickets, spots):
        self.tickets = tickets
        self.spots = spots
        self.current_ticket = current_ticket
        
    def takeTicket(self):
        print("Here is your ticket.")
        del(self.tickets[0])
        del(self.spots[0])
        
    def showSpots(self):
        print(f'There are {len(self.spots)} spots left')
        
    def payForParking(self):
        hours = (input('How many hours would you like to pay for? (Please enter a number)'))
        price = int(hours) * 15
        print("You owe:", (price), "dollars")
        paymentStatus = input("When you are done paying, type 'done'")
        while True:
            if paymentStatus.lower() == ('done'):
                self.current_ticket["paid"] = True
                print("Thank you for your business (You have 15 minutes to leave.)")
                self.tickets.insert(0,1)
                self.spots.insert(0,1)
                print(f'There are {len(self.spots)} spots left')
                break
            else:
                print("You owe:", (price), "dollars")
                paymentStatus = input("When you are done paying, type 'done'")

ParKing = Garage({"paid": False}, [1,2,3,4,5], [1,2,3,4,5])

def runGarage():
    ParKing.takeTicket()
    ParKing.showSpots()
    ParKing.payForParking()
    
runGarage()