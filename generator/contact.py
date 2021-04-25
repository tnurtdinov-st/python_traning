import random
import string
import os.path
import json
import getopt
import sys
import jsonpickle
from model.contact import Contact


try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of groups", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 5
f = "data/contact.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o =="-f":
        f = a

def random_string(prefix, maxlen):
    symbol = string.ascii_letters + string.digits + " "*10
    return prefix +"".join([random.choice(symbol) for i in range(random.randrange(maxlen))])

def random_number(maxlen):
    symbol = string.digits
    return "+7"+ "("+"".join([random.choice(symbol) for i in range(random.randrange(maxlen))])+")"+"".join([random.choice(symbol) for i in range(random.randrange(maxlen))]) +"".join([random.choice(symbol) for i in range(random.randrange(maxlen))])

def random_email(prefix, maxlen):
    symbol = string.ascii_letters + string.digits
    return prefix +"".join([random.choice(symbol) for i in range(random.randrange(maxlen))])+ "@"+prefix+"".join([random.choice(symbol) for i in range(random.randrange(maxlen))])+".ru"

def random_month():
    months = ["January", "February","March", "April", "May", "June", "July", "August", "September", "October", "November","December"]
    return random.choice(months)

def random_day():
    day = list(range(1, 28))
    return str(random.choice(day))

def random_year():
    year = list(range(1900, 2019))
    return str(random.choice(year))

testdata=[Contact(firstname=random_string("firstname", 10),
                  lastname=random_string("lastname", 10),
                  middlename=random_string("middlename", 10),
                  nickname=random_string("nickname", 10),
                  title=random_string("firstname", 10),
                  company=random_string("company", 10),
                  address1=random_string("address1", 10),
                  homephone=random_number(5),
                  mobilephone=random_number(5),
                  workphone=random_number(5),
                  fax=random_number(5),
                  email1=random_email("email1", 3),
                  email2=random_email("email2", 3),
                  email3=random_string("email3", 3),
                  homepage=random_string("homepage", 5),
                  bdaydate=random_day(),
                  bmonth=random_month(),
                  byear=random_year(),
                  aday=random_day(),
                  amonth=random_month(),
                  ayear=random_year(),
                  address2=random_string("address2", 10),
                  phone2=random_number(5),
                  notes1=random_string("notes1", 10))for i in range(3)]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))