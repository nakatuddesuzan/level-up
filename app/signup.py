import re

class User(object):


    def __init__(self, fname, lname, ccode, pnumber, email, password):
        self.fname = fname
        self.lname = lname
        self.ccode = ccode
        self.pnumber = pnumber
        self.email = email
        self.password = password

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, pwd):
        if not pwd:
            raise Exception("Field can't be empty")
        if len(pwd) < 8:
            raise Exception("Weak password \n Password must have atleast 8 characters ")
        if len(pwd) > 12:
            raise Exception('Weak password \n password is too long It must be between 6 and 12 characters')
        if not re.search(r'[0-9]', pwd):
            raise Exception('Weak password \n Password should have atleast one integer')
        if pwd.isupper() or pwd.islower() or pwd.isdigit():
            print("Weak password \n Either you need to include alphabets or \n try include both letter cases")
        self._password = pwd

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        if not value:
            raise Exception("Email field can't be empty")
        if not re.match(r"([\w\.-]+)@([\w\.-]+)(\.[\w\.]+$)", value):
            raise ValueError('Enter Valid Email ID forexample "sue@gmail.com"')
        self._email = value

    @property
    def fname(self):
        return self._name
    
    @fname.setter
    def fname(self, value):
        if not value:
            raise Exception("Field can't be empty")
        if len(value) <= 2:
            raise Exception("Name too sort \n  Not allowed") 
        if re.compile('[!@#$%^&*:;?><.0-9]').match(value):
            raise ValueError("Invalid characters not allowed")
            
        self._name = value

    @property
    def lname(self):
        return self._name
    
    @lname.setter
    def lname(self, value):
        if not value:
            raise Exception("Field can't be empty")
        if len(value) <= 2:
            raise Exception("Name too sort \n  Not allowed") 
        if value == self.fname:
            raise Exception('Firstname cannot be the same as second name')
        if re.compile('[!@#$%^&*:;?><.0-9]').match(value):
            raise ValueError("Invalid characters not allowed")   
        self._name = value

    @property
    def pnumber(self):
        return self._pnumber

    @pnumber.setter
    def pnumber(self, value):
        if not value:
            raise Exception("Field can't be empty")
        if len(str(value ))> 9:
            raise ValueError('Invalid contact not allowed')
        
        self._pnumber = value




        






