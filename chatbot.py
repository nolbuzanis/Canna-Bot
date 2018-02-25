
# coding: utf-8

# In[106]:


import json
import requests


# In[107]:


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


# In[108]:


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


# In[112]:


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


# In[110]:


questions = ["Yo, tell me about the discolorings on your leaves and where they are at", 
             "Bruh, I need to know more about ya plant's discoloration, where are they on the plant?", 
             "Where on the leaf, would you say the discolorings are", 
             "Describe the texture of your leaves?", 
             "Is your plant spotted and patterned all over or is it basic and plain? Please tell me more, I am dying to hear.",
             "Tell me about the colors on your plant's patterns and spots",
             "How would you describe the location of your plant's spots?", 
             "It would help to know whether there are any bites on your plants, assuming you didn't get really hungry, you might have some critters up in that.", 
              "I heard the cast of Bug's Life is all up in your plant? Is this true?", 
             "Paint me a word picture of the bugs and other critters in your plants. What colors are they?", 
             "I hope you don't get intimidated by my big words, but is your plant hydroponically grown or nah?",
             "What color are your roots, and no I am not talking about your hair!",
             "Are your plant's roots slimey?",
             "Are your humidity levels under 20%?",
             "How often do you make it rain on your plants? Over three times per week or under one? Tell ya boy the truth",
             "Describe the state of your leaves, are they wilting?", 
             "Are your leaves curling? Do they even lift?", 
             "How close do you keep the light from your plants. Better not be more than 10 inches."
            ]


# In[125]:

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


class PlantResponse:
    
    def main():
        with open("data.json", "r") as jsonFile:
            data = json.load(jsonFile)
        if not data['user-data']['values']:
            userData = {key: None for key in attributes}
        userData = data['user-data']['values']
        subject = data["previous_subject"].lower()
        
        if subject == "pattern" or entity['attribute'] == "pattern": #######
            subject = pattern
            userData['pattern'] = 'true'
            for entity in data['user_response']['entities']:
                characteristic = entity['attribute']
                if characteristic == "colour" or characteristic == 'location':
                    characteristic = subject + characteristic
                value = entity['value'][0]
                userData[characteristic] = value
                
        if subject == "no value" or subject == "leaf": #######
            for entity in data['user_response']['entities']:
                characteristic = entity['attribute']
                if characteristic == "colour" or characteristic == "curling" or characteristic == "texture":
                    characteristic = "leaf " + characteristic
                if characteristic == 'location':
                    characteristic = 'colour ' + characteristic
                value = entity['value'][0]
                userData[characteristic] = value
        
        
        profileName, probability, profile = getLikelyProfile(userData)
        
        i = 0
        for key in profile:
            if userData[key].lower() == "no value":
                index = attributes.index(key)
                if index < 4:
                    data['previous_subject'] = 'leaf'
                elif index < 7:
                    data['previous_subject'] = 'pattern'
                elif index < 10:
                    data['previous_subject'] = 'bug'
                elif index < 13:
                    data['previous_subject'] = 'root'
                else:
                    data['previous_subject'] = 'leaf'
                    
                data['bot-response'] = questions[index]
                with open("data.json", "w") as jsonFile:
                    json.dump(data, jsonFile)
                break
            i = i + 1
        
        if i == len(profile):
            for attribute in attributes:
                if userData[attribute] == "no value":
                    index = attributes.index(attribute)
                    if index < 4:
                        data['previous_subject'] = 'leaf'
                    elif index < 7:
                        data['previous_subject'] = 'pattern'
                    elif index < 10:
                        data['previous_subject'] = 'bug'
                    elif index < 13:
                        data['previous_subject'] = 'root'
                    else:
                        data['previous_subject'] = 'leaf'
                    
                    if index == 7 or index == 12 or index == 13 or index == 14 index == 15 or index == 16 or index == 17:
                        print("1")
                    else:
                        print("0")

                    data['bot-response'] = questions[index]
                    with open("data.json", "w") as jsonFile:
                        json.dump(data, jsonFile)
                    break
                    
                
            #if entity['type'] == 'location' and plantPart == 'leaf':
    
    if __name__ == '__main__':
        main()


# In[122]:



