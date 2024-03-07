supermarket = {
    #First section
    "Electronics":{
        "aisle_1":{
                "samsung":{
                    123:{
                        "product_name": "phone1",
                        "price": 999,
                        "reviews": {
                            "review_1": "I didn't like it whatsoever",
                            "review_2": "Could be better",
                            "review_3": "I fking love this phone!"
                            }
                    },
                    234:{
                        "product_name": "phone2",
                        "price": 888,
                        "reviews": {
                            "review_1": "My fav",
                            "review_2": "LETS BE HONEST, IPHONE IS BETTER",
                            "review_3": "the comment above me is straight up shit"
                        }
                    },
                    345:{
                        "product_name": "phone3",
                        "price": 888,
                        "reviews": {
                            "review_1": "THE DISPLAY IS SO UGLY",
                            "review_2": "THE COLORS ARE AWESOME 10/10",
                            "review_3": "DID YO GUYS NOTICED THAT 1 + 1 = 2?"
                        }
                    }
                }, 
                
                "Apple":{
                    123:{
                        "product_name": "Iphone 15",
                        "price": 2000,
                        "reviews": {
                            "review_1": "Samsung Better!",
                            "review_2": "Xiamoi better!",
                            "review_3": "Earth is flat btw"
                            }
                    },
                    234:{
                        "product_name": "Iphone 17",
                        "price": 3000,
                        "reviews": {
                            "review_1": "NAH DUDE DIS PHONE SO TRASH!!!",
                            "review_2": "THE CAMERA IS SO SMOOTH UWU",
                            "review_3": "so basically my girl and i broke up :("
                        }
                    },
                    345:{
                        "product_name": "Mac 15 pro max ultra",
                        "price": 4500,
                        "reviews": {
                            "review_1": "This is apples best feature",
                            "review_2": "Fire in the hole",
                            "review_3": "cat + cat  = 2cat =w="
                        }
                    }
                }  
            },
        "aisle_2":{
            "Lenovo":{
                123:{
                    "product_name": "Lenovo Legion Y530",
                    "price": 300,
                    "reviews": {
                        "review_1": "left fan works whenever it feels like it"
                        }
                    },
                234:{
                    "product_name": "Lenovo Legion 5",
                    "price": 1200,
                    "reviews": {
                        "review_1": "buy it if it's on sale"
                        }
                    }
                }
            }, 
        "aisle_3":{
            "intel": {
                123: {
                    "product_name": "Intel Core i7",
                    "price": 300,
                    "reviews": {
                        "review_1": "Great performance, worth the price"
                    }
                },
                234: {
                    "product_name": "Intel Core i9",
                    "price": 1200,
                    "reviews": {
                        "review_1": "Top-notch processor, excellent for gaming"
                    }
                }
            },
            "nvidia":{
                345: {
                    "product_name": "NVIDIA GeForce GTX 1650",
                    "price": 250,
                    "reviews": {
                        "review_1": "Decent graphics card for the price"
                    }
                },
                456: {
                    "product_name": "NVIDIA GeForce RTX 3080",
                    "price": 1000,
                    "reviews": {
                        "review_1": "Absolute beast of a GPU, worth every penny"
                    }
                }
            }
        }
    },
    #Second section
    "Food":{
        "aisle_1":{
            "Diana":{
                123:{
                    "product_name": "Arroz Diana",
                    "price": 10,
                    "reviews": {
                        "review_1": "Good quality rice"
                    }
                },
                234:{
                    "product_name": "Aceite",
                    "price": 5,
                    "reviews": {
                        "review_1": "Affordable!"
                    }
                }
            }
        },
        "aisle_2": {
            "Coca-Cola": {
                345: {
                    "product_name": "Sprite",
                    "price": 3,
                    "reviews": {
                        "review_1": "FUNTINE DRAKE"
                    }
                },
                456: {
                    "product_name": "Fanta",
                    "price": 8,
                    "reviews": {
                        "review_1": "FANTASTIC! did yo guys get THE JOKE?"
                    }
                }
            }
        },
        "aisle_3": {
            "Ramo": {
                567: {
                    "product_name": "Chocorramo",
                    "price": 4,
                    "reviews": {
                        "review_1": "Chocolate yummy yummy"
                    }
                },
                678: {
                    "product_name": "Colacaiones",
                    "price": 6,
                    "reviews": {
                        "review_1": "Delicious and nutritious option"
                    }
                }
            }
        }
    },
    #THIRD SECTION
    "Cleaning":{
        "aisle_1":{
            "Colgate": {
                123: {
                    "product_name": "ToothPaste",
                    "price": 4.99,
                    "reviews": {
                        "review_1": "My mouth fresh as always"
                    }
                },
                234: {
                    "product_name": "ToothBrush",
                    "price": 3.49,
                    "reviews": {
                        "review_1": "my teeths white as fuck!"
                    }
                }
            }
        }, 
        "aisle_2": {
            "Gillette": {
                345: {
                    "product_name": "Shaving Razor",
                    "price": 2.99,
                    "reviews": {
                        "review_1": "THERES BLOOD EVERYWHERE, HELP ME!"
                    }
                },
                456: {
                    "product_name": "Shaving Cream",
                    "price": 5.49,
                    "reviews": {
                        "review_1": "its so yummy"
                    }
                }
            }
        },
        "aisle_3": {
            "Johnson & Johnson": {
                567: {
                    "product_name": "Shampoo",
                    "price": 1.99,
                    "reviews": {
                        "review_1": "My bae so happy with it!"
                    }
                },
                678: {
                    "product_name": "Body Soap",
                    "price": 7.99,
                    "reviews": {
                        "review_1": "Removes dirt effectively, pleasant scent"
                    }
                }
            }
        }
    }
}

#print(supermarket["Electronics"]["aisle_1"]["samsung"][123])

def sum_all_electronics(supermarket):
    total = 0
    for aisle in supermarket["Electronics"].values():
        for brand in aisle.values():
            for product in brand.values():
                total += product["price"]
    return total


total_electronics = sum_all_electronics(supermarket)
print(f"omg sum all: ${total_electronics}")

#1: Print all products in aisle_1
for brand, items in supermarket["Electronics"]["aisle_1"].items():
    for item_id, item_details in items.items():  
        print(item_details["product_name"])

#2: Print the total number of products in aisle_1
total_products = sum(len(items) for items in supermarket["Electronics"]["aisle_1"].values())
print("Total number of products in aislE 11:", total_products)

#3: Print the average price of products in aisle 1
prices = [item_details["price"] for items in supermarket["Electronics"]["aisle_1"].values() for item_details in items.values()]
average_price = sum(prices) / len(prices)
print("Average price of products in aisle 1:", average_price)

#4: Find the cheapest product in aisle 1
cheapest_product = min((item_details["price"], item_details["product_name"]) for items in supermarket["Electronics"]["aisle_1"].values() for item_details in items.values())
print("Cheapest product in aisle 1:", cheapest_product)

#5: Find the most expensive product in aisle 1
most_expensive_product = max((item_details["price"], item_details["product_name"]) for items in supermarket["Electronics"]["aisle_1"].values() for item_details in items.values())
print("Most expensive product in aisle 1:", most_expensive_product)

#6: Print all products with prices less than $5 in aisle 1
print("Products with prices less than $5 in aisle 1:")
for items in supermarket["Electronics"]["aisle_1"].values():
    for item_details in items.values():
        if item_details["price"] < 5:
            print(item_details["product_name"])

#7: Print all products with prices greater than $10 in aisle 1
print("Products with prices greater than $10 in aisle 1:")
for items in supermarket["Electronics"]["aisle_1"].values():
    for item_details in items.values():
        if item_details["price"] > 10:
            print(item_details["product_name"])

#8: Print all products with reviews containing the word "awesome" in aisle 1
print("Products with reviews containing the word 'awesome' in aisle 1:")
for items in supermarket["Electronics"]["aisle_1"].values():
    for item_details in items.values():
        for review in item_details["reviews"].values():
            if "awesome" in review.lower():
                print(item_details["product_name"])

#9: Print all products with reviews containing the word "trash" in aisle 1
print("Products with reviews containing the word 'trash' in aisle 1:")
for items in supermarket["Electronics"]["aisle_1"].values():
    for item_details in items.values():
        for review in item_details["reviews"].values():
            if "trash" in review.lower():
                print(item_details["product_name"])

#10: Print all products in aisle 1 sorted by price (ascending)
print("Products in aisle 1 sorted by price (ascending):")
sorted_products = sorted((item_details["price"], item_details["product_name"]) for items in supermarket["Electronics"]["aisle_1"].values() for item_details in items.values())
for price, product_name in sorted_products:
    print(product_name, "-", price)

#11: Print all products in aisle 1 sorted by price (descending)
print("Products in aisle_1 sorted by price (descending):")
sorted_products_desc = sorted(((item_details["price"], item_details["product_name"]) for items in supermarket["Electronics"]["aisle_1"].values() for item_details in items.values()), reverse=True)
for price, product_name in sorted_products_desc:
    print(product_name, "-", price)


#12: Print the total number of reviews for products in aisle 1
total_reviews = sum(len(item_details["reviews"]) for items in supermarket["Electronics"]["aisle_1"].values() for item_details in items.values())
print("Total number of reviews for products in aisle 1:", total_reviews)

#13: Print all unique product names in aisle 1
unique_product_names = set(item_details["product_name"] for items in supermarket["Electronics"]["aisle_1"].values() for item_details in items.values())
print("Unique product names in aisle 1:", unique_product_names)

#14: Print all unique brand names in aisle 1
unique_brand_names = set(brand for brand in supermarket["Electronics"]["aisle_1"].keys())
print("Unique brand names in aisle_1:", unique_brand_names)

#15: Print the average number of reviews per product in aisle 1
average_reviews_per_product = total_reviews / total_products
print("Average number of reviews per product in aisle 1:", average_reviews_per_product)

#16: Print the total number of brands in aisle 1
total_brands = len(supermarket["Electronics"]["aisle_1"])
print("Total number of brands in aisle 1:", total_brands)

#17: Print all product names containing the word "phone" in aisle 1
print("Product names containing the word 'phone' in aisle 1:")
for items in supermarket["Electronics"]["aisle_1"].values():
    for item_details in items.values():
        if "phone" in item_details["product_name"].lower():
            print(item_details["product_name"])

#18: Print all product names containing the word "Mac" in aisle 1
print("Product names containing the word 'Mac' in aisle 1:")
for items in supermarket["Electronics"]["aisle_1"].values():
    for item_details in items.values():
        if "Mac" in item_details["product_name"]:
            print(item_details["product_name"])

#19: Print all product names containing the word "Legion" in aisle_1
print("Product names containing the word 'Legion' in aisle 1:")
for items in supermarket["Electronics"]["aisle_1"].values():
    for item_details in items.values():
        if "Legion" in item_details["product_name"]:
            print(item_details["product_name"])


