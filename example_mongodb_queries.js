//Example queries

//Top 10 Girls names for 2018
db.allnames.find(
    {'gender':'F','ranks.2018':{$lte:10}},{'name':1,'_id':0}).
    sort({'ranks.2018':1})

//number of names in 1957 (remove the count command to get all of the names)
db.allnames.find({'pops.1957':{$gt:1}}).count()

//Number of names used by both genders
db.allnames.aggregate([
    {
        $group:
            {
                _id: {name: "$name"},
                uniqueIds: {$addToSet: "$_id"},
                count: {$sum: 1}
            }
    },
    {
        $match:
            {
                count: {"$gt":1}
            }
    },
    {
        $count: "names_on_both_lists"
    }
])

//girl's names on the 1880 list that aren't on the 2018 list
db.allnames.find(
    { $and: [{gender:'F'},{'pops.1880':{$exists:true}},{'pops.2018':{$exists:false}}] },{'name':1,'_id':0})


/*{name:'Khaleesi':{'intro_year_pop': 28, '
pops': {'2018': 560, '2015': 341, '2014': 369, '2017': 467, '2016': 370, '2011': 28, '2013': 243, '2012': 146},
'ranks': {'2018': 549, '2015': 821, '2014': 757, '2017': 631, '2016': 765, '2011': 4982, '2013': 1023, '2012': 1518}, 
'intro_year_rank': 4982, 'gender': 'F', 'intro_year': '2011'}}*/