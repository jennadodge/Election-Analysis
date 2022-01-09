counties=["Arapahoe", "Denver", "Jefferson"]
if 'El Paso' in counties:
    print("El Paso is in the list of counties.")
else:
    print("El Paso is not in the list of counties.")

#compound membership and logical operation
if "Arapahoe" in counties or "El Paso" in counties:
    print("Arapahoe or El Paso is in the list of counties.")
else:
    print("Arapahoe and El Paso are not in the list of counties.")

for county in counties:
    print(county)

for i in range(len(counties)):
    print(counties[i])


counties_dict = {"Arapahoe": 422829, "Denver":463353, "Jefferson":432438}

for county in counties_dict:
    print(county)

for county in counties_dict.keys():
    print(county)

print("----------------------------------------")

#print values
for voters in counties_dict.values():
    print(voters)

print("----------------------------------------")

#print values using dictionary_name[key] format
for county in counties_dict:
    print(counties_dict[county])

print("----------------------------------------")

#print values using get() method
for county in counties_dict:
    print(counties_dict.get(county))

print("----------------------------------------")

#print value-key pairs
for county, voters in counties_dict.items():
    print(county, voters)

print("----------------------------------------")

for county, voters in counties_dict.items():
    print(f'{county} county has {voters} registered voters.')

print("----------------------------------------")

voting_data=[{"county":"Arapahoe","registered_voters":422829}, 
                {"county":"Denver","registered_voters":463353},
                {"county":"Jefferson", "registered_voters":432438}]

print("----------------------------------------")

for county_dict in voting_data:
    print(county_dict)

print("----------------------------------------")

#use range() to print counties from each dictionary in the list
for i in range(len(voting_data)):
    print(voting_data[i]["county"])

print("----------------------------------------")

#get the values from the list of dictionaries voting_data
for county_dict in voting_data:
    for value in county_dict.values():
        print(value)

print("----------------------------------------")        

#print only the registered number of voters from each dictionary
for county_dict in voting_data:
    print(county_dict['registered_voters'])      

print("----------------------------------------")

#print the county name only
for county_dict in voting_data:
    print(county_dict['county'])

print("----------------------------------------")

for county, voters in counties_dict.items():
    print(f'{county} county has {voters:,} registered voters.')

print("----------------------------------------")

for county_dict in voting_data:
    print(f'{county_dict["county"]} county has {county_dict["registered_voters"]:,} registered_voters.')