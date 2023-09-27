#importing for mongo db
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

#importing for data scraping
import requests
import os

from dotenv import load_dotenv
load_dotenv()

#uri connects you to  mongodb atlas
uri = os.environ['MONGODBURI']



# Set API version when creating a new client
client = MongoClient(uri, server_api=ServerApi('1'))
                          
# successful connection
try:
    client.admin.command('ping')
    print("successfully connected to MongoDB!")
except Exception as e:
    print(e)


#creating a new database if does not already exists
mydb = client["Tailnodedatabase"]

#creating collections 
mycol = mydb["user"]
myposts = mydb["post"]

print("Available collections are:-")
print(mydb.list_collection_names())

# Helper functions
def fetch_users(limit):
    url = f'https://dummyapi.io/data/v1/user?limit={limit}'
    headers = {'app-id': "6514368d64575f79d6403775"}  

    response = requests.get(url, headers=headers)
    users_data = response.json().get('data')
    
    return users_data
    

def fetch_posts(user_id):

    url = 'https://dummyapi.io/data/v1/user/{}/post'
    headers = {'app-id': '6514368d64575f79d6403775'}  

   
    response = requests.get(url.format(user_id), headers=headers)
    posts_data = response.json().get('data')
    x = myposts.insert_many(posts_data)
    

def insert_users(number):

    # inserting users
    mylist=fetch_users(number) 
    x = mycol.insert_many(mylist)
    print("\nUsers Created successfully ......\n\n")

def upload_posts():
    for x in mycol.find({},{"_id":0,"id":1}):
        fetch_posts(x['id'])
    print("\nPosts Uploaded successfully ......\n\n")

# Min Program Starts
while True:
    print('''
    Enter you choice:-
    -> Press 1 to Insert users
    -> Press 2 to Upload Posts
    ''')
    option=int(input("What would you like to do?  "))

    if(option==1):
        number=int(input("How many Users would you like to upload? "))
        insert_users(number)
    elif(option==2):
        upload_posts()



