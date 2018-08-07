import unittest
import json
from app.signup import User


class TestUser(unittest.TestCase):
  
    def setUp(self):
       pass

    def test_user_creation(self):
        self.assertTrue(User("sue" ,"mart", "256", "774868529", "sue@gmail.com", "Sensible123"))

    def test_empty_password_field(self):
        password = ""
        self.assertRaises( Exception,  User, password)

    def test_empty_email_field(self):
        email = ""
        self.assertRaises( Exception,  User, email)

    def test_invalid_email_address(self):
        email = "sue@gmail.com"
        self.assertRaises( Exception,  User, email)

            


    

