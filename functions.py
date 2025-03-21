import random
import string

from db import db
from models import URL

def generate_short_url():

    length = 10

    short_url =''.join(random.choices(string.ascii_letters + string.digits, k=length))
    return short_url



def fetch_url(shorten_name):
    shorten = db.session.query(URL).filter_by(short_url=shorten_name).first()
    return shorten