from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import time

# Step 1: Launch browser

driver = webdriver.Chrome()
driver.get('https://web.whatsapp.com')
print("Scan the QR code and wait...")

time.sleep(20)  # Time to scan QR

# Step 2: Main loop

while True:
    try:
        # Find unread chats
        unread_chats = driver.find_elements(By.CLASS_NAME, '_2aBzC')
        for chat in unread_chats:
            chat.click()
            time.sleep(1)

            # Get last message
            messages = driver.find_elements(By.CLASS_NAME, '_21Ahp')
            if messages:
                last_msg = messages[-1].text.lower()
                print(f"Last message: {last_msg}")

                # Auto-reply condition
                if 'hello' in last_msg:
                    msg_box = driver.find_element(By.XPATH, '//div[@contenteditable="true"][@data-tab="10"]')
                    msg_box.send_keys('Hi! How can I help you?' + Keys.ENTER)
                    print("Replied: Hi! How can I help you?")
        time.sleep(5)

    except Exception as e:
        print("Error:", e)
        time.sleep(5)
