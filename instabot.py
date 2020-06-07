from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from pynput.mouse import Button, Controller

import os
import time



class InsagramBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password

        self.driver = webdriver.Chrome('chromedriver.exe')

        self.login()

    def login(self):
        self.driver.get('https://www.instagram.com/')


        time.sleep(2)
        self.driver.find_element_by_name('username').send_keys(self.username)
        self.driver.find_element_by_name('password').send_keys(self.password)
        time.sleep(1)
        self.driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[4]/button/div').click() #clicks on the login button
        time.sleep(4)
        try:
            self.driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div/div/div/button').click() #clicks on the Not Now button
        except:
                ""
        time.sleep(2)
        self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div[3]/button[2]').click()  # clics on the not now button
        time.sleep(2)
        # goes to enderpostaggio page
        self.driver.get('target link')
        time.sleep(2)
        self.driver.find_element_by_xpath('/html/body/div[1]/section/main/div/header/section/ul/li[2]/a').click()  #clicks on followers
        time.sleep(1)


        followers = self._get_names()

        count = 0
        
        for follower in followers:
            self.driver.get('https://www.instagram.com/' + follower )
            try:
                self.driver.find_element_by_class_name(
                "_9AhH0").click()  # clicks on the immage
                time.sleep(3)
                self.driver.find_element_by_xpath(
                '/html/body/div[4]/div[2]/div/article/div[2]/section[1]/span[1]/button').click()
                self.driver.find_element_by_xpath(
                '/html/body/div[4]/div[3]/button').click()
                time.sleep(3)
                self.driver.execute_script("window.history.go(-1)")
                count = count + 1

            except:
                ""

        print("I have liked " + str(count) + " photos")    

       
    def _get_names(self):
        
        mouse = Controller()
        mouse.position = (670, 767)

        mouse.press(Button.left)
        time.sleep(30)
        mouse.release(Button.left)
    
        scroll_box = self.driver.find_element_by_xpath(
            "/html/body/div[4]/div")
        last_ht, ht = 0, 1
        while last_ht != ht:
            last_ht = ht
            time.sleep(1)
            ht = self.driver.execute_script("""
                arguments[0].scrollTo(0, arguments[0].scrollHeight); 
                return arguments[0].scrollHeight;
                """, scroll_box)
        links = scroll_box.find_elements_by_tag_name('a')
        names = [name.text for name in links if name.text != '']
        # close button
        self.driver.find_element_by_xpath("/html/body/div[4]/div/div[1]/div/div[2]/button")\
            .click()
        return names
        
    
























if __name__ == '__main__':
    ig_bot = InsagramBot('username', 'password')




    





        
     
     
