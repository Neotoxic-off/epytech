# Epitech.py 0.1

## IMPORTANT YOUR NEED YOUR AUTOLOGIN URL !

## Install:
```
git clone https://github.com/Neotoxic-off/epitech.py
cp -rf epitech.py <YOUR PROJECT>
```

## Import:
```PY
from epitech.py import attempt, session, user, login
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
def test():
    # The 'create' is your key to acces to your data
    # and to don't loose your login
    key_session = session.create("<YOUR AUTOLOGIN URL>")

    # The 'load' is the initialisation and the update
    # of the elemennts for 'user' and 'load'
    # You need to use 'load' before the search
    user.load(key_session)
    login.load(key_session)

    # The 'search' will search on the data, the item
    # asked
    print(login.search("login"))
    print(user.search("promo"))
```