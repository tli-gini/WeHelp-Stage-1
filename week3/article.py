from datetime import datetime
import os
import ssl
import bs4
import csv
ssl._create_default_https_context = ssl._create_unverified_context

import urllib.request as req

def getData(url):
    request=req.Request(url,headers={
        "cookie":"over18=1",
        "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
    })
  
    with req.urlopen(request) as response:
        data=response.read().decode("utf-8")

    
    soup=bs4.BeautifulSoup(data,"html.parser")
    posts = soup.find_all('div', class_='r-ent')

    base_url = "https://www.ptt.cc/"

    with open("article.csv",mode="a",encoding="utf-8") as file:  
        writer = csv.writer(file)
        
        for post in posts:
            data = []
            title = post.find('div', class_='title').find('a')
            title_text = title.string if title else ""
            if title_text == "":
                continue

            nrec = post.find('div', class_='nrec').get_text(strip=True) or '0'
            
            if not nrec.isdigit():
                nrec = '0' 

            link_tag = post.find('div', class_='title').find('a', href=True)
            
            relative_path = link_tag['href']

            full_url = base_url + relative_path
        
            time = get_time_from_url(full_url)
            data.append(title_text)
            data.append(nrec)
            data.append(time)

            writer.writerow(data)
           
       
    nextLink = soup.find("a",string="‹ 上頁")
    
    return nextLink["href"]

def get_time_from_url(url):
    request=req.Request(url,headers={
        "cookie":"over18=1",
        "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
    })
  
    with req.urlopen(request) as response:
        data=response.read().decode("utf-8")

    linked_page_soup = bs4.BeautifulSoup(data, 'html.parser')
    ttime_span = linked_page_soup.find_all('div', class_='article-metaline')
    if ttime_span:
        time_span = ttime_span[-1].find('span', class_='article-meta-value')
        time_value = time_span.text if time_span else 'Time not found'

        parsed_time = datetime.strptime(time_value, "%a %b %d %H:%M:%S %Y")

        formatted_time_str = parsed_time.strftime("%a %b %d %H:%M:%S %Y")

        return formatted_time_str
    

def main():
    filename = "article.csv"
    if os.path.exists(filename):
        os.remove(filename)
    pageURL="https://www.ptt.cc/bbs/Lottery/index.html"   
    count=0
    while count<3:
        pageURL="https://www.ptt.cc"+getData(pageURL)  
        count+=1  

main()