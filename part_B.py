import requests
import os
from bs4 import BeautifulSoup

from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi



from dotenv import load_dotenv
load_dotenv('./.env')

#uri connects you to  mongodb atlas
uri = os.environ['MONGODBURI']
client = MongoClient(uri, server_api=ServerApi('1'))
                          
#  successful connection
try:
    client.admin.command('ping')
    print("successfully connected to MongoDB!")
except Exception as e:
    print(e)

#creating a new database if does not already exists
mydb = client["teachdatabase"]
#creating collections 
mybooks = mydb["books"]

def get_rating(str_rating):
    if(str_rating=="One"):
        return 1
    elif(str_rating=="Two"):
        return 2
    elif(str_rating=="Three"):
        return 3
    elif(str_rating=="Four"):
        return 4
    elif(str_rating=="Five"):
        return 5
        
complete_data=[]
for page in range(1, 51):
    url = f'http://books.toscrape.com/catalogue/page-{page}.html'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    # Find all book containers
    books = soup.find_all('article', class_='product_pod')
    # Extract book attributes and store in the database
    for book in books:
        name = book.h3.a['title']
        price = book.find('p', class_='price_color').text[1:]
        availability = book.find('p', class_='instock availability').text.strip()
        string_rating = book.find('p', class_='star-rating').get('class')[1]
        rating=get_rating(string_rating)
        mydict={
            "Name":name,
            "Price":price,
            "Rating":rating,
            "Availability":availability
        }
        complete_data.append(mydict)

x = mybooks.insert_many(complete_data)
print("Completed.........")
