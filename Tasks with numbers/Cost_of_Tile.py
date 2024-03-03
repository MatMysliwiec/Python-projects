def Cost_Tile(width_floor,height_floor,price):
    coverage=width_floor*height_floor
    coverage_m2 = coverage/1000000
    total = round(coverage_m2)*price
    return total


w = float(input("Enter width of floor: "))
h = float(input("Enter height of floor: "))
p = float(input("Enter price of tile per square meter: "))
print("Total cost of tiles to cover your floor: ",Cost_Tile(w,h,p))
