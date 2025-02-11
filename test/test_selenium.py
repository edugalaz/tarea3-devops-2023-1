# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestCreardirector():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_creardirector(self, director):
    self.driver.get("http://localhost:8001/")
    self.driver.set_window_size(1269, 804)
    self.driver.find_element(By.ID, ":r1:-tab-1").click()
    self.driver.find_element(By.CSS_SELECTOR, "#add-director-btn .w-16").click()
    self.driver.find_element(By.ID, "name").click()
    self.driver.find_element(By.ID, "name").send_keys(director)
    self.driver.find_element(By.CSS_SELECTOR, ".h-min > .flex").click()
    element = self.driver.find_element(By.CSS_SELECTOR, ".h-min > .flex")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()

class TestCrearpelicula():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_crearpelicula(self, title, year, director, description):
    self.driver.get("http://localhost:8001/")
    self.driver.set_window_size(1269, 804)
    self.driver.find_element(By.CSS_SELECTOR, "#add-movie-btn .w-16").click()
    element = self.driver.find_element(By.CSS_SELECTOR, "#add-movie-btn .w-16")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(self.driver)
    actions.move_to_element(element, 0, 0).perform()
    self.driver.find_element(By.ID, "title").click()
    self.driver.find_element(By.ID, "title").send_keys(title)
    self.driver.find_element(By.ID, "year").click()
    self.driver.find_element(By.ID, "year").send_keys(year)
    self.driver.find_element(By.ID, "director_id").click()
    dropdown = self.driver.find_element(By.ID, "director_id")
    dropdown.find_element(By.XPATH, "//option[. = '" + director + "']").click()
    self.driver.find_element(By.ID, "description").click()
    self.driver.find_element(By.CSS_SELECTOR, ".flex-1").click()
    self.driver.find_element(By.ID, "description").click()
    self.driver.find_element(By.CSS_SELECTOR, ".flex-1").click()
    self.driver.find_element(By.ID, "description").click()
    self.driver.find_element(By.ID, "description").send_keys(description)
    self.driver.find_element(By.CSS_SELECTOR, ".h-min > .flex").click()
  
directors = [
    'Francis Ford Coppola',
    'James Wan',
    'Cristopher Nolan'
]

movies = [
    {
        'title': 'The Godfather',
        'year': '1972',
        'director': directors[0],
        'description': 'Filme sobre la familia mafiosa Corleone, poder, lealtad y traición en el mundo criminal.'
    },
    {
        'title': 'The Conjuring',
        'year': '2013',
        'director': directors[1],
        'description': 'Filme de horror basado en hechos reales, sigue a investigadores paranormales enfrentando entidades malignas.'
    },
    {
        'title': 'Inception',
        'year': '2010',
        'director': directors[2],
        'description': 'Filme de ladrones que entran en mentes, explorando realidades enredadas y percepciones alteradas.'
    },
    {
        'title': 'Interstellar',
        'year': '2014',
        'director': directors[2],
        'description': 'Filme de ciencia ficción que explora viajes especiales, agujeros de gusano y amor interdimensional en busca de un nuevo hogar para la humanidad.'
    }
]

testDirector = TestCreardirector()
testDirector.setup_method()
testDirector.test_creardirector(directors[0])
testDirector.test_creardirector(directors[1])

testMovie = TestCrearpelicula()
testMovie.setup_method()
testMovie.test_crearpelicula(movies[0]['title'], movies[0]['year'], movies[0]['director'], movies[0]['description'])
testMovie.test_crearpelicula(movies[1]['title'], movies[1]['year'], movies[1]['director'], movies[1]['description'])
testMovie.test_crearpelicula(movies[2]['title'], movies[2]['year'], movies[2]['director'], movies[2]['description'])
testMovie.test_crearpelicula(movies[3]['title'], movies[3]['year'], movies[3]['director'], movies[3]['description'])