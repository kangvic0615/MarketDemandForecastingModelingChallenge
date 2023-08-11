#최종 완성본!!
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import time
import csv

browser = webdriver.Chrome()
browser.get('http://kssc.kostat.go.kr/ksscNew_web/kssc/common/ClassificationContent.do?gubun=1&strCategoryNameCode=001&categoryMenu=007&addGubun=no')
time.sleep(3)
act = ActionChains(browser)

filename = "test_TEXT데이타.csv"
f = open(filename, "w", encoding="utf8",newline="")
writer = csv.writer(f)

for a in range(20):
  line = 'li .hitarea.hasChildren-hitarea.expandable-hitarea'
  lineword = browser.find_elements(By.CSS_SELECTOR, line)
  for l in lineword:
    try:
      l.click()
    except:
      print("Not Clickable")
      pass
      
# lineword2 = browser.find_elements(By.XPATH, '//*[@id="fm"]/table[1]/tbody/tr[5]/td')
for n in range(1110, 99010):
  num = str(n)
  if len(num) < 5: num = "0" + num
  try:
    lineword2 = browser.find_elements(By.CSS_SELECTOR, "#source{}".format(num))
    lineword2[0].click()
    time.sleep(2)
    tab = browser.find_elements(By.XPATH, '//*[@id="fm"]/table[1]/tbody/tr[5]/td')
    print(lineword2[0].text.split(".")[1])
    print(tab[0].text)
    #파일생성
    writer.writerow(lineword2[0].text.split(".")[1])
    writer.writerow([tab[0].text])
    time.sleep(2)
  except:
    pass

while(True):
  pass