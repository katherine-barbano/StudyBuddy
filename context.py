# This will contain the dating algorithm

import Algorithmia
from nltk.stem import SnowballStemmer
import copy
import random, string

example_input = {
  "scoring_weights": {
      "interests": 7,
      "position": 1,
      "coordinates": 2
  },
  "mentors": [
    {
          "name": "Samo",
          "interests": [
        "ai",
        "rpa",
        "finance",
        "sports"
      ],
          "position": "2",
          "coordinates": {
              "lat": 47.599088077746394,
              "long": -122.3339125374332
      }
    },
    {
          "name": "Liam",
          "interests": [
        "tech",
        "blockchain",
        "di",
        "ppm"
      ],
          "position": "2",
          "coordinates": {
              "lat": 47.599088077746394,
              "long": -122.3339125374332
      }
    },
    {
          "name": "Caoimhe",
          "interests": [
        "sports",
        "di",
        "finance",
        "rpa"
      ],
          "position": "4",
          "coordinates": {
              "lat": 47.599088077746394,
              "long": -122.3339125374332
      }
    },
    {
          "name": "Hannah",
          "interests": [
        "ai",
        "sports",
        "ppm",
        "strategy",
        "risk"
      ],
          "position": "5",
          "coordinates": {
              "lat": 47.599088077746394,
              "long": -122.3339125374332
      }
    },
    {
          "name": "James",
          "interests": [
        "strategy",
        "tax",
        "risk",
        "sports"
      ],
          "position": "7",
          "coordinates": {
              "lat": 47.599088077746394,
              "long": -122.3339125374332
      }
    },
    {
          "name": "Conor",
          "interests": [
        "ai",
        "rpa",
        "risk",
        "tax"
      ],
          "position": "5",
          "coordinates": {
              "lat": 47.599088077746394,
              "long": -122.3339125374332
      }
    },
    {
          "name": "Alan",
          "interests": [
        "strategy",
        "tax"
      ],
          "position": "3",
          "coordinates": {
              "lat": 47.599088077746394,
              "long": -122.3339125374332
      }
    },
    {
          "name": "Saad",
          "interests": [
        "risk",
        "tech",
        "sports",
        "ppm"
      ],
          "position": "3",
          "coordinates": {
              "lat": 47.599088077746394,
              "long": -122.3339125374332
      }
    },
    {
          "name": "Orlaith",
          "interests": [
        "ai",
        "tech",
        "finance"
      ],
          "position": "5",
          "coordinates": {
              "lat": 47.599088077746394,
              "long": -122.3339125374332
      }
    },
    {
          "name": "Lily",
          "interests": [
        "rpa",
        "tech",
        "blockchain",
        "tax"
      ],
          "position": "7",
          "coordinates": {
              "lat": 47.599088077746394,
              "long": -122.3339125374332
      }
    }
  ],
  "mentees": [
    {
          "name": "Samo",
          "interests": [
        "ai",
        "rpa",
        "finance",
        "sports"
      ],
          "position": "2",
          "coordinates": {
              "lat": 47.599088077746394,
              "long": -122.3339125374332
      }
    },
    {
          "name": "Liam",
          "interests": [
        "tech",
        "blockchain",
        "di",
        "ppm"
      ],
          "position": "2",
          "coordinates": {
              "lat": 47.599088077746394,
              "long": -122.3339125374332
      }
    },
    {
          "name": "Caoimhe",
          "interests": [
        "sports",
        "di",
        "finance",
        "rpa"
      ],
          "position": "4",
          "coordinates": {
              "lat": 47.599088077746394,
              "long": -122.3339125374332
      }
    },
    {
          "name": "Hannah",
          "interests": [
        "ai",
        "sports",
        "ppm",
        "strategy",
        "risk"
      ],
          "position": "5",
          "coordinates": {
              "lat": 47.599088077746394,
              "long": -122.3339125374332
      }
    },
    {
          "name": "James",
          "interests": [
        "strategy",
        "tax",
        "risk",
        "sports"
      ],
          "position": "7",
          "coordinates": {
              "lat": 47.599088077746394,
              "long": -122.3339125374332
      }
    },
    {
          "name": "Conor",
          "interests": [
        "ai",
        "rpa",
        "risk",
        "tax"
      ],
          "position": "5",
          "coordinates": {
              "lat": 47.599088077746394,
              "long": -122.3339125374332
      }
    },
    {
          "name": "Alan",
          "interests": [
        "strategy",
        "tax"
      ],
          "position": "3",
          "coordinates": {
              "lat": 47.599088077746394,
              "long": -122.3339125374332
      }
    },
    {
          "name": "Saad",
          "interests": [
        "risk",
        "tech",
        "sports",
        "ppm"
      ],
          "position": "3",
          "coordinates": {
              "lat": 47.599088077746394,
              "long": -122.3339125374332
      }
    },
    {
          "name": "Orlaith",
          "interests": [
        "ai",
        "tech",
        "finance"
      ],
          "position": "5",
          "coordinates": {
              "lat": 47.599088077746394,
              "long": -122.3339125374332
      }
    },
    {
          "name": "Lily",
          "interests": [
        "rpa",
        "tech",
        "blockchain",
        "tax"
      ],
          "position": "7",
          "coordinates": {
              "lat": 47.599088077746394,
              "long": -122.3339125374332
      }
    }
  ]
}
# class AlgorithmError(Exception):
#      def __init__(self, value):
#          self.value = value
#      def __str__(self):
#          return repr(self.value)

# def apply(input):
#     # default weights for the scoring function
#     default_weights = {
#         "interests": 1.0,
#         "values": 5.0,
#         "age": 0.5,
#         "coordinates": 0.005
#     }
#     # overwrite the weights if given by user
#     if "scoring_weights" in input:
#         weights = overwriteWeights(default_weights, input["scoring_weights"])
#     else:
#         weights = default_weights
    
#     # get the input and do some checking
#     validateInput(input)
    
#     stableMarriageInput = {"optimal": {}, "pessimal": {}}
    
#     male_scoring_list = {}
#     female_scoring_list = {}
#     # create a preference list for each individual using the scoring function
#     for maleObject in input["group1"]:
#         male_scoring_list[maleObject["name"]] = {}
#         for femalObject in input["group2"]:
#             score = scoring_function(weights, maleObject, femalObject)
#             male_scoring_list[maleObject["name"]][femalObject["name"]] = score
    
#     for femalObject in input["group2"]:
#         female_scoring_list[femalObject["name"]] = {}
#         for maleObject in input["group1"]:
#             score = scoring_function(weights, femalObject, maleObject)
#             female_scoring_list[femalObject["name"]][maleObject["name"]] = score
    
#     tmp_male_scoring_list = copy.deepcopy(male_scoring_list)
#     tmp_female_scoring_list = copy.deepcopy(female_scoring_list)
    
#     # map & sort the scoring lists into a format that preserves the order of the objects
#     for male in tmp_male_scoring_list:
#         # map into a sortable format
#         male_scoring_list[male] = map(lambda x: {"name": x, "similarity": male_scoring_list[male][x]}, male_scoring_list[male])
#         # sort the preference list
#         male_scoring_list[male] = sorted(male_scoring_list[male], key=lambda k: k['similarity'], reverse=True)
#         # remove the similarity scores from the preference lists
#         male_scoring_list[male] = map(lambda x: x["name"], male_scoring_list[male])
    
#     for female in tmp_female_scoring_list:
#         # map into a sortable format
#         female_scoring_list[female] = map(lambda x: {"name": x, "similarity": female_scoring_list[female][x]}, female_scoring_list[female])
#         # sort the preference list
#         female_scoring_list[female] = sorted(female_scoring_list[female], key=lambda k: k['similarity'], reverse=True)
#         # remove the similarity scores from the preference lists
#         female_scoring_list[female] = map(lambda x: x["name"], female_scoring_list[female])
    
#     # if one group has a larger preference list, add null characters to the end of the list
#     # this is to ensure that the stable marriage algorithm works properly
#     group_difference = len(male_scoring_list) - len(female_scoring_list)
#     null_people = []
#     if group_difference == 0.0:
#         # create stable pairs using the given preference lists with the stable marriage algorithm
#         stable_marriage_input = {
#             "optimal": male_scoring_list,
#             "pessimal": female_scoring_list
#         }
#     else:
#         if group_difference > 0:
#             for i in range(group_difference):
#                 null_female = randomword(20)
#                 null_people.append(null_female)
#                 female_scoring_list[null_female] = []
#                 for male in male_scoring_list:
#                     male_scoring_list[male].append(null_female)
#                     female_scoring_list[null_female].append(male)
#         elif group_difference < 0:
#             for i in range(group_difference):
#                 null_male = randomword(20)
#                 null_people.append(null_male)
#                 male_scoring_list[null_female] = []
#                 for female in female_scoring_list:
#                     female_scoring_list[female].append(null_male)
#                     male_scoring_list[null_female].append(female)
                    
#         # create stable pairs using the given preference lists with the stable marriage algorithm
#         stable_marriage_input = {
#             "optimal": male_scoring_list,
#             "pessimal": female_scoring_list
#         }
#     stable_marriages = Algorithmia.algo("matching/StableMarriageAlgorithm").pipe(stable_marriage_input).result["matches"]
    
#     if group_difference == 0.0:
#         return stable_marriages
#     elif group_difference > 0:
#         tmp = copy.deepcopy(stable_marriages)
#         stable_marriages = dict((v,k) for k,v in tmp.iteritems())
#         for person in null_people:
#             stable_marriages.pop(person)
#         return stable_marriages
#     elif group_difference < 0:
#         for person in null_people:
#             stable_marriages.pop(person)
#         return stable_marriages

# def randomword(length):
#     return ''.join(str(random.choice).lower for i in range(length))

# def overwriteWeights(default, new):
#     rVal = default
    
#     if "interests" in new:
#         rVal["interests"] = float(new["interests"])
#     if "values" in new:
#         rVal["values"] = float(new["values"])
#     if "age" in new:
#         rVal["age"] = float(new["age"])
#     if "coordinates" in new:
#         rVal["coordinates"] = float(new["coordinates"])
    
#     return rVal

# def scoring_function(weights, person1, person2):
#     # returns a score that gives the similarity between 2 people
#     # scoring function:
#     #   +add for each interest * weight
#     #   +add for each value * weight
#     #   -subtract age difference * weight
#     #   -subtract location difference * weight
#     ss = SnowballStemmer("english")
#     score = 0.0
    
#     interest_list1 = person1["interests"]
#     interest_list2 = person2["interests"]
    
#     # compare similar interests
#     for interest1 in interest_list1:
#         for interest2 in interest_list2:
#             stem1 = ss.stem(interest1.lower())
#             stem2 = ss.stem(interest2.lower())
            
#             if stem1 == stem2:
#                 score += weights["interests"]
    
#     # compare similar values if it exists in each person
#     if "values" in person1 and "values" in person2:
#         values_list1 = person1["values"]
#         values_list2 = person2["values"]
        
#         for value1 in values_list1:
#             for value2 in values_list2:
#                 stem1 = ss.stem(value1.lower())
#                 stem2 = ss.stem(value2.lower())
            
#             if stem1 == stem2:
#                 score += weights["values"]
                
#     # compare age similarity if it exists for each person
#     if "age" in person1 and "age" in person2:
#         age1 = float(person1["age"])
#         age2 = float(person2["age"])
        
#         score -= abs(age1 - age2) * weights["age"]
    
#     # score proximity of the paired couple if coordinates exists for each person
#     if "coordinates" in person1 and "coordinates" in person2:
#         coord_inputs = {
#             "lat1": person1["coordinates"]["lat"],
#             "lon1": person1["coordinates"]["long"],
#             "lat2": person2["coordinates"]["lat"],
#             "lon2": person2["coordinates"]["long"],
#             "type": "miles"
#             }
#         distance = Algorithmia.algo("geo/GeoDistance").pipe(coord_inputs).result
#         #print "distance: {}".format(distance)
#         #print "weights: {}".format(weights)
#         score -= distance * weights["coordinates"]
    
#     return score
    
# def validateInput(input):
#     # Validate the initial input fields
#     if "group1" not in input and "group2" not in input:
#         raise AlgorithmError("Please provide both the male and female groups")
#     elif "group2" not in input:
#         raise AlgorithmError("Please provide the female group.")
#     elif "group1" not in input:
#         raise AlgorithmError("Please provide the male group.")
    
#     # The only required field for a user object is "name" and "interests"
#     for gender in ["group1", "group2"]:
#         if not isinstance(input[gender], list):
#             raise AlgorithmError("Please provide a list of people for each group.")
        
#         if len(input[gender]) == 0:
#             raise AlgorithmError("Groups cannot be empty.")
        
#         for person in input[gender]:
#             if "name" not in person or "interests" not in person:
#                 raise AlgorithmError("Please provide the name and interests for all people.")
            
#             if not isinstance(person["interests"], list):
#                 raise AlgorithmError("Please provide a list of interests for each person.")
                
#             # Check validity for the longitude and latitude if the coordinates field exists
#             if "coordinates" in person:
#                 if not isinstance(person["coordinates"], dict):
#                     raise AlgorithmError("Please provide valid coordinates")
#                 if "lat" not in person["coordinates"] or "long" not in person["coordinates"]:
#                     raise AlgorithmError("Please provide valid coordinates")
#                 if not isinstance(person["coordinates"]["lat"], float) or not isinstance(person["coordinates"]["long"], float):
#                     raise AlgorithmError("coordinate values can only be in float.")
    
    # unequal groups are now supported
    # if len(input["group1"]) != len(input["group2"]):
    #     raise AlgorithmError("The size of both groups should be same.")
client = Algorithmia.client('simxlvnvTyzFJIGg8lagiRLZOmx1')
algo = client.algo('JachiOnuoha/FinalMatching/0.1.0')
algo.set_options(timeout=300) # optional
print(algo.pipe(example_input).result)