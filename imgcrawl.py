import time
import datetime
import urllib.request
from selenium import webdriver
from selenium.webdriver.common.by import By

links = [
         'https://www.google.com/search?sa=G&hl=ko&tbs=simg:CAESgQIJTNR6-LvWQlca9QELEKjU2AQaBAhCCEMMCxCwjKcIGjoKOAgEEhSmDPAt2hHuJJAixyPYKMITsjCOGRoarQLXJem7uBAEIQVLwL2ZBEhRHJWz8jIuhc8gBTAEDAsQjq7-CBoKCggIARIEaHggqgwLEJ3twQkaiAEKGAoFZXZlbnTapYj2AwsKCS9tLzA4MXBragoZCgdsZWlzdXJl2qWI9gMKCggvbS8wNGczcgoXCgNmdW7apYj2AwwKCi9tLzBkczk5bGgKHQoKdXJiYW4gYXJlYdqliPYDCwoJL20vMDM5amJxChkKBnN0cmVldNqliPYDCwoJL20vMDFjOGJyDA&q=event&tbm=isch&ved=2ahUKEwjdv4ruzOX4AhV1p1YBHV2_DKsQjJkEegQICBAC&biw=1278&bih=1311&dpr=1',
         'https://www.google.com/search?sa=G&hl=ko&tbs=simg:CAEShgIJDObE3bbaASUa-gELEKjU2AQaAghCDAsQsIynCBo6CjgIBBIT8C2yPJAi2hEuvxaWHqwtsjDCExobpTTLf1Vh1KNZBMRr3esAHQ_1x_1nU5aDYRIcKfIAUwBAwLEI6u_1ggaCgoICAESBLQ9jo8MCxCd7cEJGo8BChgKBWV2ZW502qWI9gMLCgkvbS8wODFwa2oKJwoUYWNhZGVtaWMgaW5zdGl0dXRpb27apYj2AwsKCS9tLzA2YmRwawoXCgNmdW7apYj2AwwKCi9tLzBkczk5bGgKFwoEbWFza9qliPYDCwoJL20vMDFrcjQxChgKBWNyb3dk2qWI9gMLCgkvbS8wM3F0d2QM&q=event&tbm=isch&ved=2ahUKEwixtNuFzeX4AhX3mFYBHSNNCaoQjJkEegQICBAC&biw=1278&bih=1311&dpr=1',
         'https://www.google.com/search?q=travel+with+wear+mask&tbm=isch&ved=2ahUKEwiU-uWmzeX4AhUYx4sBHelsDtEQ2-cCegQIABAA&oq=travel+with+wear+mask&gs_lcp=CgNpbWcQAzoICAAQgAQQsQM6BQgAEIAEOggIABCxAxCDAToLCAAQgAQQsQMQgwE6BAgAEBM6CAgAEB4QCBATOggIABAeEAUQEzoECAAQHjoGCAAQHhAIUJcDWMQ8YL89aAlwAHgAgAGdAYgBsRuSAQUxMi4xOZgBAKABAaoBC2d3cy13aXotaW1nsAEAwAEB&sclient=img&ei=3DPGYpScJ5iOr7wP6dm5iA0&bih=1311&biw=1278&hl=ko',
         'https://www.google.com/search?sa=G&hl=ko&tbs=simg:CAES_1wEJIK3Aw5cPCP4a8wELEKjU2AQaAghCDAsQsIynCBo5CjcIBBITsjDwLdoRxyMukCKSCJIUwhO_1Fhoa08lk24c3Dpsfd8RV93CQYNkIkudGVaBueEcgBTAEDAsQjq7-CBoKCggIARIES9t9GQwLEJ3twQkaiQEKHAoIc3RhbmRpbmfapYj2AwwKCi9tLzAyd3pibWoKGwoIc25hcHNob3TapYj2AwsKCS9tLzA2cGcyMgoZCgdsZWlzdXJl2qWI9gMKCggvbS8wNGczcgoYCgVldmVudNqliPYDCwoJL20vMDgxcGtqChcKA2Z1btqliPYDDAoKL20vMGRzOTlsaAw&q=people+with+mask+walking&tbm=isch&ved=2ahUKEwjrkPK6zeX4AhV3t1YBHds3DKkQjJkEegQIDhAC&biw=1278&bih=1311&dpr=1',
         ]

save_path = 'test'

for i in range(len(links)):

    search = links[i]
    driver = webdriver.Chrome('chromedriver.exe')

    driver.get(links[i])

    SCROLL_PAUSE_TIME = 1
    TIME_OUT = 5

    # Get scroll height
    last_height = driver.execute_script("return document.body.scrollHeight")
    SAVE_FLAG = False

    while True:
        # Scroll down to bottom
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        # Wait to load page
        time.sleep(SCROLL_PAUSE_TIME)
        # Calculate new scroll height and compare with last scroll height
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            try:
                driver.find_element(".mye4qd").click()
            except:
                break
        last_height = new_height

    images = driver.find_elements(By.CSS_SELECTOR, ".rg_i.Q4LuWd")
    count = 0
    for image in images:
        SAVE_FLAG = False
        try:
            image.click()
            # timer.start() # eHAdSb
            imgUrl = driver.find_element(By.XPATH, '//*[@id="Sva75c"]/div/div/div[3]/div[2]/c-wiz/div/div[1]/div[1]/div[3]/div/a/img').get_attribute("src")
            stt = time.time()
            while 'data:image/' in imgUrl or 'encrypted-tbn0.gstatic.com/' in imgUrl:
                time.sleep(0.2)
                imgUrl = driver.find_element(By.XPATH, '//*[@id="Sva75c"]/div/div/div[3]/div[2]/c-wiz/div/div[1]/div[1]/div[3]/div/a/img').get_attribute("src")
                if time.time() - stt > TIME_OUT:
                    print(imgUrl)
                    break
            date = datetime.datetime.now().strftime("%y%m%d_%H%M%S.%f")[:-3]
            urllib.request.urlretrieve(imgUrl, f'{save_path}/{date}.jpg')
            print(f'Save images :  {save_path}/{date}.jpg')
            SAVE_FLAG = True
            count += 1

        except Exception as e:
            print(e)
            continue

    print(f'Total images : {count}')
    driver.close()
