import json
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
#from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from timeprocessing import condition_all
from skypeMessaging import *


url = "https://www.linkedin.com/uas/login"

user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.50 Safari/537.36'
options=Options()
options.headless=True
options.add_argument(f'user-agent={user_agent}')
options.add_argument("--enable-webgl")
options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.add_argument("--incognito")


# ChromeDriverManager used
# service = Service(executable_path="C:/Users/Dell/Desktop/Devfinity_post_monitor/venv_dev/driver/chromedriver.exe")
# browser = webdriver.Chrome(service=service, options=options)

browser = webdriver.Chrome(ChromeDriverManager().install(), options=options)
browser.maximize_window()
browser.refresh()
browser.implicitly_wait(20)


content = open('config/linkedInlogin.json')
config = json.load(content)


def login():

    browser.get(url)
    elementID = browser.find_element(By.ID,"username")
    elementID.send_keys(config['username'])
    time.sleep(2)
    elementID = browser.find_element(By.ID,"password")
    elementID.send_keys(config['password'])
    time.sleep(2)
    elementID.submit()
    
    time.sleep(2)


    
    visitingProfileID = "/company/devfinity/posts/?feedView=all"
    fulllink= "https://www.linkedin.com" + visitingProfileID
    browser.get(fulllink)
    #response = requests.get(fulllink, verify=False, headers=headers)
    #print(response)
    print(browser.title)

    time.sleep(2)

    #Minimizing msg box
    try:
        wait = WebDriverWait(browser, 20)
        button_0=wait.until(EC.presence_of_element_located((By.XPATH,"//button[contains(@class,'msg-overlay-bubble-header__control')][2]")))
        ActionChains(browser).move_to_element(button_0).click(button_0).perform()
    except:
        print('message box not rechable')

    time.sleep(3)

    #clicking Short by
    try:
        button = browser.find_element(By.XPATH,"//button[contains(@class,'artdeco-dropdown__trigger') and contains(@data-control-name,'feed_sort_dropdown_trigger')]")
        #browser.implicitly_wait(20)
        browser.find_element(By.ID, button.get_attribute("id")).click()
        #ActionChains(browser).move_to_element(button).click(button).perform()
        #button.click()
        print("Short by button clicked")
        print(browser.title)
    except:
        print("Sort by not detected")

    time.sleep(2)

    try:
        wait = WebDriverWait(browser, 10)
        button = wait.until(EC.presence_of_element_located((By.XPATH,"//div[contains(@class,'artdeco-dropdown__content') and contains(@aria-hidden,'false')]//child::li[2]")))
        ActionChains(browser).move_to_element(button).click(button).perform()
        print("Short By: Recent clicked")
        print(browser.title)
    except:
        print("Sort by: Recent not detected")


    time.sleep(2)

# Extraction of Post details

def postExtraction():
    
    #extraction of time of post
    XPATH_TIME_POSTED = "(//span[@class='visually-hidden'])[1]"
    #(//span[@class="visually-hidden"])[1]/text() ----for first recent post
    # (//span[@class="visually-hidden"])[4]/text() ----for second recent post                       
    time_posted = browser.find_element(By.XPATH, XPATH_TIME_POSTED).text
    #print('Time of post :', time_posted)
    post_details["Post_date"]=time_posted
    


    time.sleep(2)

    # # Extraction of caption
    # XPATH_CAPTION = "(//span[contains(@dir,'ltr')])[3]"
    # # (//span[contains(@dir,'ltr')])[3]/text() ----for first recent
    # # (//span[contains(@dir,'ltr')])[5]/text() ----for second recent 
    # raw_caption = browser.find_element(By.XPATH, XPATH_CAPTION).text
    # caption= ''.join(raw_caption).strip().replace('\n','',-1).replace('#','',-1) if raw_caption else 'No Caption'
    # #print('Caption of Post :', caption)
    # post_details["Caption"]=caption

    
    # #Extraction of _#_ keywords
    # child_element_list = browser.find_element(By.XPATH,'(//span[@class="break-words"])[1]//child::a')
    # print(child_element_list)
    # tag_List=[]
    # taglist =  browser.find_elements(By.XPATH,'(//span[@class="break-words"])[1]//child::a')
    # #print(taglist)
    # #print(type(taglist))
    # for e in taglist:
        
    #     # print(e.get_attribute('value'))
    #     tag = str(e.get_attribute('innerHTML'))
    #     tag_List.append(tag)
        
    #     #type(e.get_attribute('innerHtml'))
    #     #tag_List.append(tags)    
    #     # print(e.get_attribute('outerHTML'))
    #     #print(e)
    # post_details["tag_list"] = tag_List
    # print(post_details)
        
    try:
        button = browser.find_element(By.XPATH,"(//button[contains(@class,'feed-shared-control-menu__trigger') and contains(@type,'button')])[1]")
        #browser.implicitly_wait(20)
        #print(button.get_attribute("id"))
        browser.find_element(By.ID, button.get_attribute("id")).click()
    except:
        print("Post option menu not rechable")

    time.sleep(2)

    try:
        wait = WebDriverWait(browser, 10)
        button_1=wait.until(EC.presence_of_element_located((By.XPATH,"(//div[contains(@class,'feed-shared-control-menu__content') and contains(@aria-label,'Control Menu Options')])[1]//child::li[2]")))
        ActionChains(browser).move_to_element(button_1).click(button_1).perform()
    except:
        print("Copy link to post not rechable ")

    #(//p[contains(@class,'artdeco-toast-item__message') and contains(@role,'alert')])//child::a

    try:
        button_2 =  browser.find_element(By.XPATH,"(//p[contains(@class,'artdeco-toast-item__message') and contains(@role,'alert')])//child::a")
        post_url = button_2.get_attribute("href")
        #print(post_url)
        post_details['Post_URL']=post_url
    except:
        print("Link not rechable")
    
    # print(post_url)
    # post_details["Post_URL"]=post_url

    time.sleep(20)
    browser.close()
    browser.quit()
    return(post_details)

if __name__=="__main__":
    post_details = {}   

    login()
    post_detail = postExtraction()     
    #print(post_detail)

    status , dict = condition_all(post_detail)
    #print(status, dict)

    if status==1:
        data = get_post_data(dict)
        send_message(data)


