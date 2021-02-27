import datetime
from selenium import webdriver

objs = []
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
driver = webdriver.Chrome(options=chrome_options)

def collect_news_post(url):
    driver.get(url)
    elements = driver.find_element_by_class_name("xwlist").find_elements_by_xpath("./*")
    for element in elements:
        date = element.find_element_by_tag_name("span").text
        title = element.find_element_by_tag_name("a").text[:-7]
        url = element.find_element_by_tag_name("a").get_property("href")
        print(date, title, url)
        if (title.find("2021") != -1):
            objs.append((date, title, url))

def download_news_text(date, title, url):
    driver.get(url)
    elements = driver.find_element_by_class_name("text_content").find_elements_by_tag_name('p')
    content = ''
    for element in elements:
        strongs = element.find_elements_by_xpath("./strong")
        if len(strongs) > 0 :
            content += "## "
        content += element.text
        content += "  \n"
    print(title)
    f = open("../_posts/2021-" + date + "-News-2021" + date[:2] + date[3:] +".md", 'w+', encoding='utf8')
    f.write(
'''---
title: ''' + title + '''
published: true
categories: [news]
---

''')
    f.write(content)
    f.close()

def create_today_news_post():
    today = str(datetime.date.today())[-5:]
    url = 'http://www.xwlbo.com/txt.html'
    driver.get(url)
    elements = driver.find_element_by_class_name("xwlist").find_elements_by_xpath("./*")
    for element in elements:
        date = element.find_element_by_tag_name("span").text
        title = element.find_element_by_tag_name("a").text[:-7]
        url = element.find_element_by_tag_name("a").get_property("href")
        if date == today:
            objs.append((date, title, url))

if __name__ == "__main__":
    # collect_news_post('http://www.xwlbo.com/txt.html')
    # collect_news_post('http://www.xwlbo.com/txt_2.html')
    create_today_news_post() 
    for obj in objs:
        download_news_text(obj[0], obj[1], obj[2])
    driver.close()