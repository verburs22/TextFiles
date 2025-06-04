#sarah verburg 06-04

data = [
    "Andromeda - Shrub",
    "Bellflower - Flower",
    "China Pink - Flower",
    "Daffodil - Flower",
    "Evening Primrose - Flower",
    "French Marigold - Flower",
    "Hydrangea - Shrub",
    "Iris - Flower",
    "Japanese Camellia - Shrub",
    "Lavender - Shrub",
    "Lilac - Shrub",
    "Magnolia - Shrub",
    "Peony - Shrub",
    "Queen Anne's Lace - Flower",
    "Red Hot Poker - Flower",
    "Snapdragon - Flower",
    "Sunflower - Flower",
    "Tiger Lily - Flower",
    "Witch Hazel - Shrub",
]

# plants_filename ="flowers_print.txt"
# # print data to new file
# with open(plants_filename, "w") as plants:
#     for plant in data:
#         print(plant, file= plants)

#new_plants = []
# with open(plants_filename, "r") as plants:
#     for plant in plants:
#         new_plants.append(plant.rstrip())
# print(new_plants)

# plants_filename = "flowers_write.txt"
# # write data to new file
# with open(plants_filename, "w") as plants:
#     for plant in data:
#         plants.write(plant)
# print(data)

# string_rep = data.__str__()
# print(type(string_rep))

#print number to text file
filename = "test_numbers.txt"
with open(filename, "w") as numbers:
    for num in range(10):
        print(num, file=numbers)

# must pass numbers as a string to be able to use write method
with open(filename, "w") as numbers:
    for num in range(10):
        numbers.write(str(num) + "\n")
