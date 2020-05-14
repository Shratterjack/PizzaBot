import string
import random



def generateSessionId():
    res = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))
    return res.lower()
    

