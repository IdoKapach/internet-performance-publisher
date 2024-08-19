import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import os

def get_speed():
    speedtest_url = "https://www.speedtest.net/"
    driver.get(speedtest_url)
    time.sleep(5)
    con_buttom = driver.find_element(By.CSS_SELECTOR, "#onetrust-button-group div button")
    con_buttom.click()
    go_button = driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a')
    go_button.click()
    time.sleep(60)
    try:
        close_button = driver.find_element(By.XPATH,
                                           '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[8]/div/div/p[2]/button')
        close_button.click()
        time.sleep(2)
    except selenium.common.exceptions.ElementNotInteractableException():
        time.sleep(10)
        close_button = driver.find_element(By.XPATH,
                                           '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[8]/div/div/p[2]/button')
        close_button.click()
        time.sleep(2)
    download_mbps = driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span').text
    print(download_mbps)
    upload_mbps = driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text
    print(upload_mbps)
    return download_mbps, upload_mbps

def send_message(message):
    twitter_username = os.environ.get("TWITTER_USERNAME_PYTHON")
    twitter_password = os.environ.get("TWITTER_PASSWORD_PYTHON")

    twit_url = "https://twitter.com/home"
    driver.get(twit_url)

    time.sleep(2)
    user_name = driver.find_element(By.NAME, "text")
    user_name.send_keys(f"{twitter_username}{Keys.ENTER}")
    time.sleep(1)
    user_name = driver.find_element(By.NAME, "text")
    user_name.send_keys(f"idopython10{Keys.ENTER}")
    time.sleep(1)
    password_input = driver.find_element(By.NAME, "password")
    password_input.send_keys(f"{twitter_password}{Keys.ENTER}")
    time.sleep(3)
    tweet_input = driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div/div[2]/div/div/div/div')
    tweet_input.send_keys(message)

    post_button = driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/div/div[3]/div/span/span')
    post_button.click()


chrom_options = webdriver.ChromeOptions()
chrom_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrom_options)
download_mbps, upload_mbps = get_speed()
message = f"download_mbps: {download_mbps}\nupload_mbps: {upload_mbps}"
send_message(message)
time.sleep(3)
driver.quit()
