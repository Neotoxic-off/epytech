# Documentation

## SESSION:
```PY
# The Session object allows you to persist certain
# parameters across requests. It also persists
# cookies across all requests made from the session
# instance.

# Create an access to your account with the autologin
# link, given in parameter
create(link):
```

### Example:
```PY
access_key = session.create("<AUTOLOGIN LINK>")
```

## USER:
```PY
# Init the class to store the elements
# REQUIRED BEFORE LOAD AND SEARCH
init():
```

```PY
# Load the elements inside the class and store
# the user session elements inside, and update them
# REQUIRED BEFORE SEARCH
load(session):
```

```PY
# Search is searching into the datas, the item searched
# and return it, if it doesn't exists it will return 'None'
# REQUIRED THE INIT AND THE LOAD BEFORE
search(item):
```

```PY
# data is the complete data list
data
```

```PY
# len is the len of the data
# return INT
len()
```

### Example:
```PY
user = user.init()
user.load(access_key)
user.search('promo')
user.len()
user.data
```

## LOGIN:
```PY
# Init the class to store the elements
# REQUIRED BEFORE LOAD AND SEARCH
init():
```

```PY
# Load the elements inside the class and store
# the login session elements inside, and update them
# REQUIRED BEFORE SEARCH
load(session):
```

```PY
# Search is searching into the datas, the item searched
# and return it, if it doesn't exists it will return 'None'
# REQUIRED THE INIT AND THE LOAD BEFORE
search(item):
```

```PY
# data is the complete data list
data
```

```PY
# len is the len of the data
# return INT
len()
```

### Example:
```PY
login = login.init()
login.load(access_key)
login.search('message')
login.len()
login.data
```

## NOTIF:
```PY
# Init the class to store the elements
# REQUIRED BEFORE LOAD AND SEARCH
init():
```

```PY
# Load the elements inside the class and store
# the notifs session elements inside, and update them
# REQUIRED BEFORE SEARCH
load(session):
```

```PY
# Search is searching into the datas, the item searched
# and return it, if it doesn't exists it will return 'None'
# REQUIRED THE INIT AND THE LOAD BEFORE
# Group must be a int !
search(group):
```

```PY
# data is the complete data list
data
```

```PY
# len is the len of the data
# return INT
len()
```

### Example:
```PY
notif = notif.init()
notif.load(key)
notif.search(0)
notif.len()
notif.data
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

### Notif's data:
```PY
# INT MAX size
```
