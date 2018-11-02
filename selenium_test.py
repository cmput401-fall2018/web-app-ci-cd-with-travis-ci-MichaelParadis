from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from unittest import TestCase
import pytest
import time

class test_selenium(TestCase):
    def test_home(self):
        driver = webdriver.Chrome()
        driver.get("http://162.246.157.225:8000")
        time.sleep(3)
        ids = ['name', 'about', 'education', 'skills', 'work', 'contact']
        default = ['Name', 'About', 'Education', 'Skills', 'Work', 'Contact']
        for i in range(len(ids)):
            elem = driver.find_element_by_id(ids[i])
            assert(elem.text != default[i])
