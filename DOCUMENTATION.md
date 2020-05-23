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

### Example:
```PY
user = user.init()
user.load(access_key)
user.search('promo')
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

### Example:
```PY
login = login.init()
login.load(access_key)
login.search('message')
```