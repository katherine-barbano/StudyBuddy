# This will contain the dating algorithm

from nltk.stem import SnowballStemmer
import copy
import random, string
import nltk
nltk.download('wordnet')
from nltk.corpus import wordnet
from math import sqrt
import operator

example_input = {
  "inp_name": "Samo",
  "people": [
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
    },
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


def apply(input, username):
    # default weights for the scoring function

    # get the input and do some checking

    output = {"username": username}
    scoring_list = {}
    for user in input["people"]:
        if user["name"] == username:
            target_user = user

    # create a preference list for each individual using the scoring function
    for person in input["people"]:
        if person["name"] == target_user["name"]:
            continue
        score = scoring_function(target_user, person)
        scoring_list[person["name"]] = score
        
    scoring_list = sorted(scoring_list.items(), key=operator.itemgetter(1), reverse=True)
    
    output['results'] = scoring_list
    print(output)
    return output
    

def scoring_function(person1, person2):
    # returns a score that gives the similarity between 2 people
    # scoring function:
    ss = SnowballStemmer("english")
    score = 0.0
    # print(type(person1))
    # print(person1)
    
    interest_list1 = person1["interests"]
    interest_list2 = person2["interests"]
    # compare similar interests
    for interest1 in interest_list1:
        for interest2 in interest_list2:
            stem1 = ss.stem(interest1.lower())
            stem2 = ss.stem(interest2.lower())
            try:
            
                if stem1 == stem2:
                    score += 1
                else:
                    syn1 = wordnet.synsets(interest1.lower())[0]
                    syn2 = wordnet.synsets(interest2.lower())[0]
                    score += 0.5*(syn1.wup_similarity(syn2))
            except:
                score += 0.01
    score /= sqrt(len(interest_list1)* len(interest_list2))
    return score


apply(example_input, 'James')


# client = Algorithmia.client('simWHASJXduWEr33Ct12rvvEnSr1')
# algo = client.algo('rtekriwal1927/RandomRandom/0.1.0')
# algo.set_options(timeout=300) # optional
# print(algo.pipe().result)

