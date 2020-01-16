rom selenium import webdriver
import csv
import re
import time

with open('all.csv', 'r', encoding="utf8") as file:
    reader = csv.reader(file)
    num = 0
    for row in reader:
        try:
            num = num + 1
            time.sleep(10)
            search_query = '"' + str(
                row[4]) + '" (Gmail.com OR Outlook.com OR Yahoo.com OR iCloud.com OR aol.com OR Mail.com)'
            search_query = search_query.replace(' ', '+')  # structuring our search query for search url.
            executable_path = "chromedriver"
            browser = webdriver.Chrome(executable_path=executable_path)
            time.sleep(10)
            browser.get("https://www.google.com/search?q=" + search_query)
            alllinks = browser.find_elements_by_xpath('//div[starts-with(@class, "srg")]/div')
            email = ''
            for e in alllinks:
                if str(row[4]).lower() in e.text.lower() and "@" in e.text.lower() and "etsy" in e.text.lower():
                    email = re.findall(r'([\w0-9._-]+@[\w0-9._-]+\.[\w0-9_-]+)', e.text.lower())
                    print(str(email))
                    break

            if email != '':
                data = open("all_new.csv", "a")  # open file in append mode
                updatestr = '"' + str(email) + '"' + str(row) + "\n"
                updatestr = updatestr.replace("[", "")
                updatestr = updatestr.replace("]", "")
                data.write(updatestr)  # separator in file
                data.close()
                time.sleep(5)

            browser.quit()
            if num == 50:
                num = 0
                print("sleep for 15 min")
                time.sleep(900)
        except:
            pass
