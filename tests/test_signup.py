import unittest
import json
from app.signup import User


class TestUser(unittest.TestCase):
  
    def setUp(self):
       pass

    def test_user_creation(self):
        self.assertTrue(User("sue" ,"mart", "256", "774868529", "sue@gmail.com", "Sensible123"))

    def test_empty_password_field(self):
        user = User("sue" ,"mart", "256", "774868529", "sue@gmail.com", "Sensible123")
        self.assertRaises( Exception,  user.password)

            


    

