# Print total number of mobiles

from products.models import mobiles
print(len(mobiles))

# Print all mobile names
# for mob in mobiles:
#     print(mob.get("name"))
# OR
print([mob.get("name") for mob in mobiles])

# Print all samsung mobile names
print([m.get("name") for m in mobiles if m.get("brand") == 'samsung'])

# sort mobiles wrt price
print(sorted(mobiles,key=lambda m:m.get("price"),reverse=True))

# print costly mobile
print(max(mobiles,key=lambda m:m.get("price")))