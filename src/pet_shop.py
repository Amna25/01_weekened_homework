# WRITE YOUR FUNCTIONS HERE
def get_pet_shop_name(name):
    return name["name"]

#no:2
def get_total_cash(sum):
    return sum["admin"]["total_cash"]
#no3
def add_or_remove_cash(cash,add):
     if add > 0:
        x=cash["admin"]["total_cash"]+add
        cash["admin"]["total_cash"]=x
        return x
     else :
        x=cash["admin"]["total_cash"]+add
        cash["admin"]["total_cash"]=x
        return x
    
#no4
def get_pets_sold(sold):
    return sold["admin"]["pets_sold"]
#no5
def increase_pets_sold(sold, value):
    x=sold["admin"]["pets_sold"]+value
    sold["admin"]["pets_sold"]=x
#no6
def get_stock_count(count):
    x=len(count["pets"])
    return x
#no7
def get_pets_by_breed(pet_shop,animal):
    x = len(animal["pets"])
    return x
    





        







    
