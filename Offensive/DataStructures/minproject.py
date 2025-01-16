#!/usr/bin/env python3
#Genre

limit = 500

games = ["Super Mario", "Crash of the titans", "A Hat In Time", "Rayman", "Skyblock"]


genre = {
    "Super Mario" : "Adventure",
    "Crash of the titans": "Platform",
    "A Hat In Time": "Platform",
    "Rayman": "Platform",
    "Skyblock": "MMO"
}

#sales n stock
sales_stock = {
    "Super Mario" : (100, 240),
    "Crash of the titans": (900, 1000),
    "A Hat In Time": (1200, 90000),
    "Rayman": (830, 109),
    "Skyblock": (1000, 1)
}

#customers

customers = {
    "Super Mario": {"John Doe", "Emily Clark", "Michael Smith", "Sophia Johnson"},
    "Crash of the titans": {"Emily Clark", "David Brown", "Michael Smith", "Isabella Lee"},
    "A Hat In Time": {"Liam Martinez", "Emma Davis", "John Doe", "Mia Taylor"},
    "Rayman": {"Sophia Johnson", "David Brown", "Liam Martinez", "Olivia Garcia"},
    "Skyblock": {"Michael Smith", "Emma Davis", "Elijah Moore", "Abigail Walker"}
}


#summary
def summary(game):
    print(f"[+] Summary of {game}:\n")
    print(f"\t Genre: {genre[game]}")
    print(f"\t Sales and Stock: {sales_stock[game]}")
    print(f"\t Customers: {', '.join(customers[game])}\n")


for game in games:
    if sales_stock[game][0] > 900:
        summary(game) 

#two ways
total_sales = lambda: sum(cost for cost, _ in sales_stock.values() if cost > limit)

print(total_sales())

total_sales = lambda: sum(cost for game, (cost, _) in sales_stock.items() if sales_stock[game][0] > limit)


print(total_sales())