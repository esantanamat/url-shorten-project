import random
import string

def generate_short_url():

    length = 10

    short_url =''.join(random.choices(string.ascii_letters + string.digits, k=length))
    return short_url