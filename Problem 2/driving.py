
def driving_cost(miles_per_gallon, dollars_per_gallon, miles_driven):
    return (miles_driven / miles_per_gallon) * dollars_per_gallon


if __name__ == '__main__':
    
    miles_per_gallon = float(input("Enter miles per gallon: "))
    dollars_per_gallon = float(input("Enter dollars per gallon: "))

    print(f'Cost for 10 miles: {driving_cost(miles_per_gallon, dollars_per_gallon, 10):.2f}')
    print(f'Cost for 50 miles: {driving_cost(miles_per_gallon, dollars_per_gallon, 50):.2f}')
    print(f'Cost for 400 miles: {driving_cost(miles_per_gallon, dollars_per_gallon, 400):.2f}')


   
    






    
   