sample_dict = {
 "name": "Kelly",
 "surname": "Jones",
 "age": 25,
 "salary": 8000,
 "city": "New york"}
# kay = []
# value = []


for kay, value in sample_dict.items():
 print(f"{kay:<10} : {value:>10}")

for key in sample_dict.keys():
 print(key, sample_dict[key])

newdict = {}
l1 = ["age", "salary", "name", "abcd"]
for i in l1:
 if i in sample_dict:
  newdict[i] = sample_dict[i]
print(newdict)

for i in l1:
 print(sample_dict.pop(i, "Bland"))
print(sample_dict)

if "Js" in sample_dict.values():
 print("yes")
else:
 print("No")

sample_dict["location"] = sample_dict.pop("city")

print(sample_dict)



