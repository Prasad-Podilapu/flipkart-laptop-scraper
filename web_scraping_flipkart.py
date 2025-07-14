#                                                           web scraping project on flipkart 
#importing required libaries
import requests
from bs4 import BeautifulSoup
import pandas

web_link="https://www.flipkart.com/search?q=laptops&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"
page_request=requests.get(web_link)  #sends an HTTP GET request to the URL stored in 'web_link' and see the server's response
print(page_request) # Prints the response object, if status code is 200, it means the request was successful (green signal)

#information of the current page
inf=BeautifulSoup(page_request.content,'html.parser')
print(inf.text)

#laptops name and model
names=inf.find_all('div',class_="KzDlHZ")
name=[]
for i in names[1:10]:
    n=i.get_text()
    name.append(n)
print(name)

#laptop prices
prices=inf.find_all('div',class_='Nx9bqj _4b5DiR')
price=[]
for i in prices[1:10]:
    p=i.get_text()
    price.append(p)
print(price)

#ratings
ratings=inf.find_all('div',class_='XQDdHH')
rate=[]
for i in ratings[1:10]:
    r=i.get_text()
    rate.append(float(r))
print(rate)

#reviews
reviews=inf.find_all('span',class_='Wphh3N')
review=[]
for i in reviews[1:10]:
    re=i.get_text()
    review.append(re)
print(review)

#features
features=inf.find_all('ul',class_='G4BRas')
feature=[]
for i in features[1:10]:
    f=i.get_text()
    feature.append(f)
print(feature)

#links 
links=inf.find_all('a',class_='CGtC98')
link=[]
for i in links[1:10]:
    l="https://www.flipkart.com"+i['href']
    link.append(l)
print(link)

#images
images=inf.find_all('img',class_='DByuf4')
image=[]
for i in images[1:10]:
    im=i['src']
    image.append(im)
print(image)

#pushing data to dataframe and formating to csv
data={'name and model':name,'prices':price,'ratigs':rate,'reviwes':review,'features':feature,'links':link,'images':image}
store=pandas.DataFrame(data)
print(store)
store.to_csv("laptop_data.csv")
