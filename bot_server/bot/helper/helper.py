import os
import string
import random
import dialogflow_v2 as dialogflow



def generateSessionId():
    res = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))
    return res.lower()
    

