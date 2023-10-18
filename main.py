import random
class FoodOrder():
  def __init__(self, ArrivalTime, AmOrPm, Distance, Price, Main_dish, Side_dish):
    self.AmOrPm = AmOrPm
    self.ArrivalTime = ArrivalTime
    self.Distance = Distance
    self.Price = Price  
    self.Main_dish = Main_dish
    self.Side_dish = Side_dish
  def __str__(self):
    return f'{self.ArrivalTime} {self.Distance} {self.Price}'
  

Main_dish = ['Pizza', 'Pasta', 'Burger', 'Sandwiches',]
Side_dish = ['Fries', 'Salad', 'Soup', 'Wings', 'Chips']
AMandPM = ('am' , 'pm')
time = random.choice(AMandPM)

order = FoodOrder(random.randint(1, 12), time, random.randint(3, 5), random.randint(10, 30), random.choice(Main_dish), random.choice(Side_dish))

name = input('what is your name ')

def help():
  print('')
  print('Hi, I am food delivery bot. I can help you with all concerns from the lis tbelow.')
  print(f'Hello {name} please select one of the option below')
  print('')
  print('1: Cancel the order')
  print('2: Reorder the food')
  print('3: Track how far your delivery driver is')
  print('4: Refund')
  print('5: Get General order information')
  print('6: Exit')
  print('')

def Cancel():
  print('')
  print(f'hello {name} Your order has been cancelled')
  print('Good day')
  help()
  print('')
  
def ReorderFood():
  print('')
  print(f'hello {name} Your order has been reordered')
  print(f'That will cost you ${order.Price}')
  help()
  print('')
  
def Trakcing():
  print('')
  print(f'hello {name} Your delivery driver is {order.Distance} miles away and was supposed to arrive at {order.ArrivalTime}{order.AmOrPm}')
  help()
  print('')

def Refund():
  print('')
  print(f'hello {name} Your order has been refunded')
  print(f'Amount: ${order.Price}')
  help()
  print('')
  
def genInfo():
  print('')
  print(f'hello {name} Your order costs ${order.Price}')
  print(f'Main: {order.Main_dish} Sides: {order.Side_dish}')
  print(f'Arrival time: {order.ArrivalTime}{order.AmOrPm}')
  print(f'distance from driver location: {order.Distance} miles away')
  help()
  print('')
  
def Exit(exit):
  print('')
  print('Hopefully we were able to help')
  print('Good Day')
  exit = True
  return exit
  print('')

def main():
  exit = False
  help()
  while  exit == False:
    choice = input('What would you like to do ')
    if choice == '1':
      Cancel()
    elif choice == '2':
      ReorderFood()
    elif choice == '3':
      Trakcing()
    elif choice == '4':
      Refund()
    elif choice == '5':
      genInfo()
    elif choice == '6':
      exit = Exit(exit)
    else:
      print('')
      print('Please enter a valid option')
      print('')
      
main()