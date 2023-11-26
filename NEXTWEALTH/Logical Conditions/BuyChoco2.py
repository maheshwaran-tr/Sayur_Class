#buy choc and cake
# one choc is Rs 200
# one cake is 150
#get budget from user.Also get the total number of choc and cakes that the shop has
#Hint - you can buy choc/Cake only if shop has it.
#find how many choc and cake the user can buy

chocolate_price = 200
cake_price = 150

# getting budget from user
budget = float(input("Enter your budget: "))

# getting total chocs and cakes available in the store
tot_chocs = int(input("Enter the number of chocolates available in the shop: ")) 
tot_cakes = int(input("Enter the number of cakes available in the shop: "))

max_chocs = budget//chocolate_price    # calculating how many chocs they can buy
max_cake = budget//cake_price           # calculating how many cakes they can buy

if tot_chocs <= max_chocs:
    max_chocs = tot_chocs

if tot_cakes <= max_cake:
    max_cake = tot_cakes

print("With a budget of", budget, "rupees, you can buy:")
print("Chocolates:", max_chocs)
print("Cakes:", max_cake)