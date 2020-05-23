# Epytech 

<p align = "left">
    <img alt = "epietch" width="234.1" height="310.7" src = "images/epitech.png"/>
    <img alt = "version" src = "https://img.shields.io/badge/version-0.3-blue.svg"/>
</p>

## IMPORTANT YOUR NEED YOUR AUTOLOGIN URL !
https://intra.epitech.eu/admin/autolog?format=json

## Install:
```
git clone https://github.com/Neotoxic-off/epytech
cp -rf epytech/epytech <YOUR PROJECT>
```

## Import:
```PY
from epytech import attempt, session, user, login
```

### User's data:
```          
login            
title            
internal_email   
lastname         
firstname        
userinfo         
referent_used    
picture          
picture_fun	     
scolaryear	     
promo	         
semester	     
location	     
documents	     
userdocs	     
shell	         
close	         
ctime	         
mtime	         
id_promo	     
id_history	     
course_code	     
semester_code    
school_id	     
school_code	     
school_title	 
old_id_promo	 
old_id_location	 
rights	         
invited	         
studentyear	     
admin	         
editable	     
restrictprofiles 
```

### Login's data:
```
data        
login       
message    
access_token
```

## Examples:
```PY
from epytech import user, session, login

def test():
    # Initialise the classes
    user_data = user.init()
    login_data = login.init()

    # The 'create' is your key to acces to your data
    # and to keep access to your session
    key = session.create("<AUTOLOGIN LINK>")

    # The 'load' is the initialisation and the update
    # of the elemennts for 'user' and 'login'
    # You need to use 'load' before the search
    user_data.load(key)
    login_data.load(key)

    # The 'search' will search on the data, the item
    # asked
    print(user_data.search('login'))
    print(login_data.search('message'))

test()
```

```PY
from epytech import user, session, login

class data():
    key = session.create("<AUTOLOGIN LINK>")
    user = user.init()
    login = login.init()

def complex_test():
    data.user.load(data.key)
    data.login.load(data.key)

    if data.login.search('message') == "Success":
        print("Welcome: %s" % data.user.search('firstname'))
        print("Promo: %s\nSemester: %s" % (data.user.search('promo'), data.user.search('semester')))
    else:
        print("You are not logged")

complex_test()
```
