from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import pyperclip
import pyautogui


# 브라우저 꺼짐 방지 옵션
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)



# 웹페이지 해당 주소 이동
driver.get("https://nid.naver.com/nidlogin.login?mode=form&url=https://www.naver.com/")
driver.maximize_window() # 화면 최대화

# 아이디 입력창
id = driver.find_element(By.CSS_SELECTOR, "#id")
id.click()
pyperclip.copy("lizamong")
pyautogui.hotkey("ctrl","v")
time.sleep(2)

# 비밀번호 입력
password = driver.find_element(By.CSS_SELECTOR, "#pw")
password.click()
pyperclip.copy("Rjsgml2324!")
pyautogui.hotkey("ctrl","v")
time.sleep(2)

# 로그인 버튼 누르기
driver.find_element(By.CSS_SELECTOR, "#log\.login").click()
time.sleep(3)

# 메일함 이동
driver.get("https://mail.naver.com/v2/folders/0/all")
time.sleep(2)

#메일 쓰기 버튼 클릭
mail_list = driver.find_element(By.CSS_SELECTOR, "#root > div > nav > div > div.lnb_header > div.lnb_task > a.item.button_write").click()
time.sleep(2)

#받는 사람 주소 입력
driver.find_element(By.CSS_SELECTOR, "#recipient_input_element").send_keys("lizamong@naver.com")
time.sleep(1)

# 제목
driver.find_element(By.CSS_SELECTOR, "#subject_title").send_keys("파이썬으로 자동화한 메일")
time.sleep(1)

#본문 (iframe 안으로 들어가기)
iframe = driver.find_element(By.CSS_SELECTOR, "#content > div.contents_area > div > div.editor_area > div > div.editor_body > iframe")
driver.switch_to.frame(iframe)
driver.find_element(By.CSS_SELECTOR, "body > div > div.workseditor-content").send_keys("본문 내용")
time.sleep(2)

# iframe 밖으로 나오기
driver.switch_to.default_content()


#보내기 버튼
driver.find_element(By.CSS_SELECTOR, "#content > div.mail_toolbar.type_write > div:nth-child(1) > div > button.button_write_task").click()