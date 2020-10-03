from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import json
import os
from urllib import parse

def main():
  if not os.path.exists('creds.json'):
    print('MAKE YOUR `creds.json` FILE FIRST!!!')
    return

  with open('creds.json') as F:
    data = json.load(F)


  url = f'https://docs.google.com/forms/d/e/{data["FORM_ID"]}/formResponse?'

  params = data["entries"]
  keys = list(params.keys())
  for x in keys:
    params[f"entry.{x}"] = params.pop(x)

  url_query = parse.urlencode(params)
  new_url = url + url_query

  browser = webdriver.Firefox()
  browser.get(new_url)
  time.sleep(1)

  elem = browser.find_element_by_id('identifierId')
  elem.send_keys(data["email"] + Keys.RETURN)

  time.sleep(2)

  elem = browser.find_element_by_name('password')
  elem.send_keys(data["password"] + Keys.RETURN)
  time.sleep(2)

  elem = browser.find_element_by_class_name('appsMaterialWizButtonPaperbuttonLabel')
  elem.click()
  time.sleep(1)

  browser.close()

if __name__ == "__main__":
    main()