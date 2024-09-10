from Shoes import Shoes

low = Shoes("And 1s", 30)
medium = Shoes("Air Force 1s", 120)
high = Shoes("Off White", 400)

try:
    shoe_budget = float(input("What is your shoe budget?  "))

    if shoe_budget < low.price:
        print("Sorry, you need to hustle more :(")
        exit()

except ValueError:
    exit("Please enter a number.")

for shoes in [high, medium, low]:
    shoes.buy(shoe_budget)