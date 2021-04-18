from sys import maxsize

class Contact:
    def __init__(self, firstname=None, lastname=None, middlename=None, nickname=None, title=None, company=None, address1=None, homephone=None, mobilephone=None,
                  workphone=None, fax=None, email1=None, email2=None, email3=None, homepage=None, bdaydate=None, bmonth=None, byear=None, aday=None, amonth=None, ayear=None,
                  address2=None, phone2=None, notes1=None, id=None):

        self.firstname = firstname
        self.lastname = lastname
        self.middlename = middlename
        self.nickname = nickname
        self.title = title
        self.company = company
        self.address1 = address1
        self.homephone = homephone
        self.mobilephone = mobilephone
        self.workphone = workphone
        self.fax = fax
        self.email1 = email1
        self.email2 = email2
        self.email3 = email3
        self.homepage = homepage
        self.bdaydate = bdaydate
        self.bmonth = bmonth
        self.byear = byear
        self.aday = aday
        self.amonth = amonth
        self.ayear = ayear
        self.address2 = address2
        self.phone2 = phone2
        self.notes1 = notes1
        self.id = id

    def __repr__(self):
        return "%s:%s %s" % (self.id, self.firstname, self.lastname)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.firstname == other.firstname and self.lastname == other.lastname

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
