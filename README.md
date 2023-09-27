# Tailnode Python Intern Assignment
## Implementation
### Part A
- First established a connection with Mongodb using URI.
- Created functions for making API calls to populate database.
- Started an infinite loop and took user inputs to perform the mentioned functionalities of creating users and posting data.
- After getting the required data it was inserted to the database and a success message is displayed.

### Part B
- First established a connection with Mongodb using URI.
- Created functions for scraping data from the mentioned websites.
- Then started a for loop for navigating to different pages for scraping data.
- After getting the required data the database is updated.


## How to use
### Step1. Cloning this repo
Run this either in gitbash terminal or VsCode terminal

### Step2. Installing and Creating virtual envirnoment
Install virtual envirnomen
```
pip install virtualenv
```


Create your virtual envirnoment
```
virtualenv tailnode_env 
```

Activate your env
```
cd tailnode_env
Scripts/activate
cd .. 
```

You should see tailnode_env written in brackets in the beginning of your terminal.

### Step3. Install requirements.txt
Now, inside your main folder install all the requirements using
```
pip -r install requirements.txt
```

### Step4. Adding your URI
- Go to https://account.mongodb.com/account/login <br>
- After logging in create your database<br>
- Now connect using python driver<br>
- Create you URI and replace it on places mentioned in the code


### Step5. Run Files
