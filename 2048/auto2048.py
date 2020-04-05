from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import random
import time

browser = webdriver.Firefox()
browser.get('https://play2048.co/')

htmlElem = browser.find_element_by_tag_name('html')


gameoverElem = browser.find_element_by_css_selector('.game-message > p:nth-child(1)').is_displayed()
retryElem = browser.find_elements_by_class_name('restart-button')

highscore = 0

outFile = open('scores.txt','w', buffering=1)

while True:
    scoreElem = browser.find_element_by_class_name('score-container')
    score = scoreElem.text
    rand_key = random.randrange(1,5) 
    if gameoverElem == False:
        if rand_key == 1:
            htmlElem.send_keys(Keys.UP)
        elif rand_key == 2:
            htmlElem.send_keys(Keys.DOWN)
        elif rand_key == 3:
            htmlElem.send_keys(Keys.LEFT)
        elif rand_key == 4:
            htmlElem.send_keys(Keys.RIGHT)
        gameoverElem = browser.find_element_by_css_selector('.game-message > p:nth-child(1)').is_displayed()
        time.sleep(0.3)
    else:
        if int(score) > highscore:
            highscore = int(score)
        outFile.write(str(highscore) + '\n')
        retryElem[0].click()
        gameoverElem = False
outFile.close()
print("WE WON!")
