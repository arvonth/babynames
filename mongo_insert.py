import pymongo
from pprint import pprint as pp
import babynames as bn

uri = "mongodb://arvont:1234@localhost/?authSource=babynames&authMechanism=SCRAM-SHA-1"
client = pymongo.MongoClient(uri)
print("Connected to Database")

db = client.babynames
collection = db.allnames

#names_male,most_pop,top_names = bn.read_all_names(1880,2019,'m','names')
#names_female,most_pop,top_names = bn.read_all_names(1880,2019,'f','names')
names_male = bn.read_all_names(1880,2019,'m','names')
names_female = bn.read_all_names(1880,2019,'f','names')

name_list = []
for item in names_male:
    name_dict = {}    
    name_dict['name'] = item
    name_dict.update(names_male[item])
    name_list.append(name_dict)

try:
    collection.insert_many(name_list)
except pymongo.errors.BulkWriteError as bwe:
    pp(bwe.details)
   

name_list = []
for item in names_female:
    name_dict = {}    
    name_dict['name'] = item
    name_dict.update(names_female[item])
    name_list.append(name_dict)


try:
    collection.insert_many(name_list)
except pymongo.errors.BulkWriteError as bwe:
    pp(bwe.details)
