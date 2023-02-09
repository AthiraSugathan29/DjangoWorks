from json import load
with open("db.json","r",encoding="utf-8") as f:
    data = load(f)
#Length of data
#print(len(data))

#Total Movie names
#print([m.get("title") for m in data])

#Name of Movies released in 2002
#print([m.get("title") for m in data if m.get("year") == "2002"])

#Monday Questions
# Movies in Comedy generes

print([m.get("title") for m in data for i in m.get("genres") if i == "Comedy"])
# for m in data:
#     for i in m.get("genres"):
#         if i == "Comedy":
#             print(m.get("title"))


# Year wise movie numbers {2002:5,1990:3...}
print("Year-wise Movie count")
mc = {}
for m in data:
    year = m.get("year")
    if year in mc:
        mc[year] += 1
    else:
        mc[year]=1
print(mc)
# Most movies released year
print(max(mc,key=lambda k:mc.get(k)))
# Most runtime movie
# lar = ""
# runt = 0
# for i in range(len(data)):
#     if runt < int(data[i]["runtime"]):
#         lar = data[i]
#         runt = int(data[i]["runtime"])
# print(lar)
#  OR
lengthy_movie = max(data,key=lambda m:int(m.get("runtime")))
print("Lengthy movie")
print(lengthy_movie)

# Short movie
short_movie = min(data,key=lambda m:int(m.get("runtime")))
print("Short movie")
print(short_movie)
# Install VS Code
