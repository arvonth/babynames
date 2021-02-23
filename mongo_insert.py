import pymongo
from pprint import pprint as pp
import babynames as bn
import json

cred_file = 'secrets.json'
uri_template = "mongodb://{0}:{1}@localhost/?authSource=babynames&authMechanism=SCRAM-SHA-1"
with open(cred_file,'r') as fp:
    creds = json.load(fp)
user = creds['user']
pw = creds['pw']


client = pymongo.MongoClient(uri_template.format(user,pw))
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
