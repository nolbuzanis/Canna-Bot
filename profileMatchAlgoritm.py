
# coding: utf-8

# In[17]:


# Plant Attributes
LEAF_COLOUR = 0
COLOUR_LOCATION = 1
COLOUR_AREA = 2
LEAF_TEXTURE = 3

PATTERN = 4
PATTERN_COLOUR = 5
PATTERN_LOCATION = 6

HOLES_OR_BITES = 7 #T/F
VISIBLE_BUGS = 8
BUG_COLOUR = 9

MEDIUM = 10
ROOT_COLOUR = 11
ROOT_SLIME = 12 #T/F

HUMIDITY = 13 #T/F
WATER_FREQUENCY = 14 #T/F
DROOPING_OR_WILTING = 15 #T/F
LEAF_CURLING = 16 #T/F
LIGHT_DISTANCE = 17 #T/F

attributes = [
    "leaf colour",#0
    "colour location",#1
    "colour area",#2
    "leaf texture",#3
    
    'pattern',#4
    "pattern colour",#5
    "pattern location",#6
    
    "holes/bites",#7
    "visible bugs",#8
    "bug colour",#9
    
    "medium",#10
    "root colour", #11
    "root slime", #12
    
    "humidity",#13
    "water frequency",#14
    "drooping/wilting",#15
    "leaf curling",#16
    "light distance"#17
]



# In[18]:


profile_list = [ #Calcium
          {attributes[LEAF_COLOUR]:["dark green", "green"],
           attributes[COLOUR_LOCATION]:["top"],
           attributes[COLOUR_AREA]:["all"],
           attributes[PATTERN]:["true"], 
           attributes[PATTERN_COLOUR]:["brown", "black"],
           attributes[PATTERN_LOCATION]:["top"]
           }, #Phosphorus
           {attributes[PATTERN]:["true"], 
            attributes[PATTERN_COLOUR]:["dark purple", "purple", "brown", "dark brown"],
            attributes[LEAF_COLOUR]:["green"],
            attributes[COLOUR_AREA]:["all"],
            attributes[COLOUR_LOCATION]:["bottom"],
            attributes[PATTERN_LOCATION]:["all"]
           }, #Nitrogen
           {attributes[LEAF_COLOUR]:["yellow"], 
            attributes[COLOUR_LOCATION]:["bottom"], 
            attributes[COLOUR_AREA]:["all"]
           }, #Potassium
            {attributes[LEAF_COLOUR]:["yellow", "brown"], 
             attributes[COLOUR_LOCATION]:["all"],
             attributes[COLOUR_AREA]:["sides"]
           }, #Boron
            {attributes[LEAF_COLOUR]:["yellow", "light yellow", "light green"],
             attributes[COLOUR_LOCATION]:["top"],
             attributes[COLOUR_AREA]:["all"],
             attributes[LEAF_CURLING]:["true"],
             attributes[HUMIDITY]:["false"] #less than <20%
           }, #Copper
            {attributes[LEAF_COLOUR]:["light green", "yellow", "blue", "purple", "green"],
             attributes[COLOUR_LOCATION]:["top"],
             attributes[COLOUR_AREA]:["all"],
             attributes[LEAF_COLOUR]:["green", "blue", "purple"]
           },#Fungus gnats
            {attributes[LEAF_COLOUR]:["yellow", "light yellow", "light green"],
             attributes[COLOUR_LOCATION]:["all"],
             attributes[COLOUR_AREA]:["all"],
             attributes[VISIBLE_BUGS]:["true"],
             attributes[BUG_COLOUR]:["brown"],
             attributes[WATER_FREQUENCY]:["true"], #>3 per week
             attributes[MEDIUM]:["soil"],
             attributes[LEAF_CURLING]:["true"]
           },#Heat stress
            {attributes[LEAF_COLOUR]:["yellow", "brown"],
             attributes[COLOUR_LOCATION]:["top"],
             attributes[COLOUR_AREA]:["all"],
             attributes[LIGHT_DISTANCE]:["close"],
             attributes[LEAF_CURLING]:["true"]
           },#Iron
            {attributes[LEAF_COLOUR]:["light green", "yellow", "light yellow"],
             attributes[COLOUR_LOCATION]:["top"],
             attributes[COLOUR_AREA]:["all"]
           },#Light burn
            {attributes[LEAF_COLOUR]:["yellow"],
             attributes[COLOUR_LOCATION]:["top"],
             attributes[COLOUR_AREA]:["between veins"],
             attributes[LIGHT_DISTANCE]:["close"]
           },#Magnesium
            {attributes[LEAF_COLOUR]:["light yellow", "yellow", "light green"],
             attributes[COLOUR_LOCATION]:["bottom"],
             attributes[COLOUR_AREA]:["between veins"]
           },#Mildew
            {attributes[LEAF_COLOUR]:["white"],
             attributes[COLOUR_LOCATION]:["all"],
             attributes[COLOUR_AREA]:["all"],
             attributes[PATTERN]:["true"],
             attributes[PATTERN_COLOUR]:["white"],
             attributes[PATTERN_LOCATION]:["all"]
           },#Nute burn
            {attributes[LEAF_COLOUR]:["yellow"],
             attributes[COLOUR_LOCATION]:["all"],
             attributes[COLOUR_AREA]:["tip"]
           },#Overwatering
            {attributes[PATTERN]:["true"],
             attributes[PATTERN_COLOUR]:["yellow"],
             attributes[PATTERN_LOCATION]:["between veins"],
             attributes[DROOPING_OR_WILTING]:["true"],
             attributes[WATER_FREQUENCY]:["true"],
             attributes[LEAF_TEXTURE]:["hard"],
             attributes[MEDIUM]:["soil", "hydro"]
           },#pH fluctuation
            {attributes[LEAF_COLOUR]:["yellow"],
             attributes[COLOUR_LOCATION]:["bottom"],
             attributes[COLOUR_AREA]:["between veins"]
           },#Root rot
            {attributes[MEDIUM]:["hydro"],
             attributes[ROOT_COLOUR]:["brown"],
             attributes[ROOT_SLIME]:["true"]
           },#Spider mites
            {attributes[VISIBLE_BUGS]:["true"],
             attributes[BUG_COLOUR]:["white"],
             attributes[PATTERN]:["true"],
             attributes[PATTERN_COLOUR]:["white"],
             attributes[PATTERN_LOCATION]:["all"]
            },#Underwatering
            {attributes[DROOPING_OR_WILTING]:["true"],
             attributes[WATER_FREQUENCY]:["false"], #Less than 1/week
             attributes[LEAF_TEXTURE]:["soft"]
            },#Worm/ caterillars/ slugs/ snails
            {attributes[HOLES_OR_BITES]:["true"]
            }
]


# In[19]:


def getLikelyProfile(userData):
    
    sum = 0
    max = -1
    match = dict()
    

    for profile in profile_list:

        for symptom in profile:
            i = 0
            for i in range(0, len(profile[symptom])):
                if userData[symptom] == str(profile[symptom][i]):
                    sum += 1
                elif userData[symptom] != "no value":
                    sum -=0.5

        if (sum > 0 and sum/len(profile[symptom]) > max):
            match = profile
            max = sum/len(profile[symptom])
                          
        sum = 0  
        
    print(match)    
    print(max)
    print("Profile Match:" + str(max/len(profile[symptom])*100) + "%")
    return (match, max/len(profile[symptom]))


# In[43]:


def getLikelyProfile(userData):
    
    userData = {key:"no value" for key in attributes}
    userData[attributes[LEAF_COLOUR]] = 'yellow'
    userData[attributes[PATTERN_COLOUR]] = 'brown'
    userData[attributes[COLOUR_LOCATION]] = 'bottom'

    sum = 0
    max = -1
    match = dict()
    index = 0
    profileNames = ['Calcium deficiency', 'Phosphorus deficiency', 'Nitrogen deficiency', 'Potassium deficiency', 'Boron deficiency', 'Copper deficiency', 'Fungus gnats', 'Heat Stress', 'Iron deficiency', 'Light Burn', 'Magnesium deficiency', 'Mildew', 'Nute burn', 'Overwatering', 'pH fluctuation', 'Root rot', 'Spider mites', 'Underwatering', 'Worm/ caterpillar Infestation']

    for profile in profile_list:
        
        for symptom in profile:
            i = 0
            for i in range(0, len(profile[symptom])):
                if userData[symptom] == str(profile[symptom][i]):
                    sum += 1
                elif userData[symptom] != "no value":
                    sum -=0.5
            
        if (sum > 0 and sum/len(profile) > max):
            match = profile
            max = sum/len(match)
            
        sum = 0  
        
    if match != {}:
        print(match)
        print(max)
        print("Profile Match:" + str(max*100) + "%")
    else:
        print("No Match!")

    for profile in profile_list:
        if match == profile:
            break
        index += 1
        
    print(profileNames[index])
    
    return (profileNames[index], str(max*100), match)

