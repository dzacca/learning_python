my_name = 'Zed A. Shaw'
my_age = 35 # not a lie
my_height = 74 # inches
my_weight = 180 # lbs
my_eyes = 'Blue'
my_teeth = 'White'
my_hair = 'Brown'

inches_to_cm = 2.54
lbs_to_kg = 0.454

my_height = my_height * inches_to_cm
my_weight = my_weight * lbs_to_kg

print(f"Let's talk about {my_name}.")
print(f"He's {my_height} cm tall.")
print(f"He's {my_weight} kg heavy.")
print(f"Actually that's not too heavy.")
print(f"He's got {my_eyes} eyes and {my_hair} hair.")
print(f"His teeth are usually {my_teeth} depending on the coffee.")

# this line is tricky, try to get it exactly right
total = my_age + my_height + my_weight
print(f"If I add {my_age}, {my_height}, and {my_weight} I get {total}")
