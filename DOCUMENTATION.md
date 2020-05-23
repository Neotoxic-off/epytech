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
```

```PY
# len is the len of the data
# return INT
len()
```

### Example:
```PY
notif = notif.init()
notif.load(data.key)
data.notif.search(0)
print(data.notif.data)
data.notif.len()
```