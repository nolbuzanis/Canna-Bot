
# coding: utf-8

# In[87]:


# Plant Attributes
LEAF_COLOR = 0
COLOR_LOCATION = 1
COLOR_AREA = 2
HOLES_OR_BITES = 3
VISIBLE_BUGS = 4
BUG_COLOR = 5
PH_LEVEL = 6 #Discontinued
SPOTS = 7
SPOT_COLOR = 8
SPOT_LOCATION = 9
DYING_LEAVES = 10
LINES_INSIDE_LEAF = 11 #Discontinued
DROOPING_OR_WILTING = 12
LIGHT_DISTANCE = 13
BURN = 14
BURN_LOCATION = 15
WATER_FREQUENCY = 16
LEAF_TEXTURE = 17
SOIL_MOISTURE = 18
MEDIUM = 19
CLOSE_FAN = 20
RECENT_TRANSPLANT = 21 #Discontinued
DISFIGURATION = 22
CYCLE = 23
WEEK = 24
LEAF_CURLING = 25
HUMIDITY = 26
SHADED = 27
ROOT_COLOR = 28
ROOT_SLIME = 29

attributes = [
    "leaf color",#0
    "color location",#1
    "color area",#2
    "holes/bites",#3
    "visible bugs",#4
    "bug color",#5
    "ph",#6
    'spots',#7
    "spot color",#8
    "spot location",#9
    "dying leaves",#10
    "lines inside leaf",#11
    "drooping/wilting",#12
    "light distance",#13
    "burn",#14
    "burn location",#15
    "water frequency",#16
    "leaf texture",#17
    "soil moisture",#18
    "medium",#19
    "close fan",#20
    "recent transplant",#21
    "disfiguration",#22
    "cycle",#23
    "week",#24
    "leaf curling",#25
    "humidity",#26
    "shaded", #27
    "root color", #28
    "root slime" #29
]



# In[88]:


disease_list = [ #Calcium
          {attributes[LEAF_COLOR]:["green"],
           attributes[COLOR_LOCATION]:["top"],
           attributes[COLOR_AREA]:["all"],
           attributes[SPOTS]:["true"], 
           attributes[SPOT_COLOR]:["brown", "black"],
           attributes[SPOT_LOCATION]:["top"],
           attributes[DISFIGURATION]:["true"],
           attributes[SHADED]:["true"]
           }, #Phosphorus
           {attributes[SPOTS]:["true"], 
            attributes[SPOT_COLOR]:["purple", "brown"],
            attributes[LEAF_COLOR]:["green"],
            attributes[COLOR_AREA]:["all"],
            attributes[COLOR_LOCATION]:["bottom"],
            attributes[SPOT_LOCATION]:["all"],
            attributes[CYCLE]:["flower"],
            attributes[WEEK]:["4", "5", "6"],
            attributes[SHADED]:["true"]
           }, #Nitrogen
           {attributes[LEAF_COLOR]:["yellow"], 
            attributes[COLOR_LOCATION]:["bottom"], 
            attributes[COLOR_AREA]:["all"],
            attributes[DYING_LEAVES]:["true"],
            attributes[CYCLE]:["flower"],
            attributes[WEEK]:["1", "2", "9", "10", "11"]
           }, #Potassium
            {attributes[LEAF_COLOR]:["yellow", "brown"], 
             attributes[COLOR_LOCATION]:["all"],
             attributes[COLOR_AREA]:["sides"],
             attributes[BURN]:["true"],
             attributes[BURN_LOCATION]:["sides"]
           }, #Boron
            {attributes[LEAF_COLOR]:["yellow", "green"],
             attributes[SHADED]:["light"],
             attributes[COLOR_LOCATION]:["top"],
             attributes[COLOR_AREA]:["all"],
             attributes[DISFIGURATION]:["true"],
             attributes[HUMIDITY]:["true"] #less than <20%
           }, #Copper
            {attributes[LEAF_COLOR]:["green", "blue", "purple"],
             attributes[SHADED]:["true"],
             attributes[COLOR_LOCATION]:["top"],
             attributes[COLOR_AREA]:["all"],
             attributes[LEAF_COLOR]:["green", "blue", "purple"]
           },#Fungus gnats
            {attributes[LEAF_COLOR]:["yellow, green"],
             attributes[SHADED]:["false"],
             attributes[COLOR_LOCATION]:["all"],
             attributes[COLOR_AREA]:["all"],
             attributes[VISIBLE_BUGS]:["true"],
             attributes[BUG_COLOR]:["brown"],
             attributes[BURN]:["true"],
             attributes[BURN_LOCATION]:["all"],
             attributes[WATER_FREQUENCY]:["greater"], #>3 per week
             attributes[SOIL_MOISTURE]:["wet"],
             attributes[MEDIUM]:["soil"],
             attributes[LEAF_CURLING]:["true"]
           },#Heat stress
            {attributes[LEAF_COLOR]:["yellow", "brown"],
             attributes[COLOR_LOCATION]:["top"],
             attributes[COLOR_AREA]:["all"],
             attributes[LIGHT_DISTANCE]:["close"],
             attributes[BURN]:["true"],
             attributes[BURN_LOCATION]:["all"],
             attributes[DISFIGURATION]:["true"],
             attributes[LEAF_CURLING]:["true"]
           },#Iron
            {attributes[LEAF_COLOR]:["green", "yellow"],
             attributes[COLOR_LOCATION]:["top"],
             attributes[COLOR_AREA]:["all"],
             attributes[SHADED]:["close"]
           },#Light burn
            {attributes[LEAF_COLOR]:["yellow"],
             attributes[COLOR_LOCATION]:["top"],
             attributes[COLOR_AREA]:["between veins"],
             attributes[LIGHT_DISTANCE]:["close"],
             attributes[BURN]:["true"],
             attributes[BURN_LOCATION]:["tip"],
           },#Magnesium
            {attributes[LEAF_COLOR]:["yellow", "green"],
             attributes[COLOR_LOCATION]:["bottom"],
             attributes[COLOR_AREA]:["between veins"],
             attributes[SHADED]:["true"]
           },#Mildew
            {attributes[LEAF_COLOR]:["white"],
             attributes[COLOR_LOCATION]:["all"],
             attributes[COLOR_AREA]:["all"],
             attributes[SPOTS]:["true"],
             attributes[SPOT_COLOR]:["white"],
             attributes[SPOT_LOCATION]:["all"]
           },#Nute burn
            {attributes[LEAF_COLOR]:["yellow"],
             attributes[COLOR_LOCATION]:["all"],
             attributes[COLOR_AREA]:["tip"],
             attributes[BURN]:["true"],
             attributes[BURN_LOCATION]:["tip"]
           },#Overwatering
            {attributes[SPOTS]:["true"],
             attributes[SPOT_COLOR]:["yellow"],
             attributes[SPOT_LOCATION]:["between veins"],
             attributes[DROOPING_OR_WILTING]:["true"],
             attributes[WATER_FREQUENCY]:["greater"],
             attributes[LEAF_TEXTURE]:["hard"],
             attributes[SOIL_MOISTURE]:["wet"],
             attributes[MEDIUM]:["soil", "hydro"]
           },#pH fluctuation
            {attributes[LEAF_COLOR]:["yellow"],
             attributes[COLOR_LOCATION]:["bottom"],
             attributes[COLOR_AREA]:["between veins"]
           },#Root rot
            {attributes[MEDIUM]:["hydro"],
             attributes[ROOT_COLOR]:["brown"],
             attributes[ROOT_SLIME]:["true"]
           },#Spider mites
            {attributes[VISIBLE_BUGS]:["true"],
             attributes[BUG_COLOR]:["white"],
             attributes[SPOTS]:["true"],
             attributes[SPOT_COLOR]:["white"],
             attributes[SPOT_LOCATION]:["all"]
            },#Underwatering
            {attributes[DROOPING_OR_WILTING]:["true"],
             attributes[WATER_FREQUENCY]:["less"], #Less than 1/week
             attributes[LEAF_TEXTURE]:["soft"],
             attributes[SOIL_MOISTURE]:["dry"]
            },#Wind burn
            {attributes[CLOSE_FAN]:["true"],
             attributes[LEAF_CURLING]:["true"]
            },#Worm/ caterillars/ slugs/ snails
            {attributes[HOLES_OR_BITES]:["true"]
            }
]


# In[ ]:


def getLikelyDisease(userData):
    #userData = {key:"No Value" for key in attributes}
    #userData[attributes[LEAF_COLOR]] = 'yellow'
    #userData[attributes[SPOT_COLOR]] = 'brown'

    # Iron Deficiency
    sum = 0
    max = -5
    match = dict()

    for disease in disease_list:

        for symptom in disease:
            #print(symptom)
            #print(disease[symptom])
            #print(len(disease[symptom]))
            i = 0
            for i in range(0, len(disease[symptom])):
                if int(userData[symptom] == str(disease[symptom][i])):
                    sum += 1

        if sum > max:
            match = disease
            max = sum
        sum = 0

    print(match)    
    print(max)
    print("Match:" + str(max/len(disease[symptom])*100) + "%")
    return (match, max/len(disease[symptom]))


# In[89]:


userData = {key:"No Value" for key in attributes}
userData[attributes[LEAF_COLOR]] = 'yellow'
userData[attributes[SPOT_COLOR]] = 'brown'

sum = 0
max = -5
match = dict()

for disease in disease_list:

    for symptom in disease:
        #print(symptom)
        #print(disease[symptom])
        #print(len(disease[symptom]))
        i = 0
        for i in range(0, len(disease[symptom])):
            if int(userData[symptom] == str(disease[symptom][i])):
                sum += 1

    if sum > max:
        match = disease
        max = sum
    sum = 0

print(match)    
print(max)
print("Match: " + str(max/len(match)*100) + "%")

