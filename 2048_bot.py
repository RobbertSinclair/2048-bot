from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import random
import time
#Open the Chrome Browser you will need a webdriver in
#order for this to work
browser = webdriver.Chrome()
#This list will store all of the scores that the bot gets
score_list = []
# Open up 2048
browser.get("https://gabrielecirulli.github.io/2048/")
htmlElem = browser.find_element_by_tag_name("html")
#This list tells the computer the controls
direction_dict = [Keys.UP, Keys.RIGHT, Keys.DOWN, Keys.LEFT]
for i in range(5):
    while True:
        try:
            #This block checks to see if the game is over
            browser.find_element_by_class_name("game-message.game-over")
            print("GAME OVER")
            #This is so that I only get the score
            time.sleep(1)
            break
        except:
            #Get a random direction
            direction = random.randint(0, 3)
            #Apply a key to the game and delay by 0.2 seconds
            htmlElem.send_keys(direction_dict[direction])
            time.sleep(0.2)
    #Now we get the score by finding the score container and append it to a list
    score = browser.find_element_by_class_name("score-container").text
    score = int(score)
    score_list.append(score)
    print("The Score was {0}".format(score))
    #The bot then clicks on the play again button
    retry = browser.find_element_by_class_name("retry-button")
    retry.click()
#Get the best score
best = browser.find_element_by_class_name("best-container").text
print("The best score was {0}".format(best))
#Get the mean of the scores
score_mean = sum(score_list) / len(score_list)
print("The mean score was {0}".format(score_mean))
time.sleep(2)
#Quit the browser
browser.quit()
