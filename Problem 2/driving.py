
def driving_cost(miles_per_gallon, dollars_per_gallon, miles_driven):
   miles_per_gallon= input('Enter miles per gallon: ')
   dollars_per_gallon= input('Enter dollars per gallon: ')
   miles_driven= input('Enter miles driven: ')
   
   cost = (miles_driven/miles_per_gallon)*dollars_per_gallon
   
   return cost

if __name__ == '__main__':
    miles_per_gallon = float(input('Enter miles per gallon: '))
    dollars_per_gallon = float(input("Enter dollars per gallon: "))

print(f'10 miles: {driving_cost(miles_per_gallon, dollars_per_gallon, 100):.2f}')
print(f'50 miles: {driving_cost(miles_per_gallon, dollars_per_gallon, 50):.2f}')
print(f'400 miles: {driving_cost(miles_per_gallon, dollars_per_gallon, 400):.2f}')
   

   
    






    
   