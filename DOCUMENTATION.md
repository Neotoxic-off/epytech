<p align = "center">
    <img alt = "logo" width="374" height="148" src = "https://raw.githubusercontent.com/Neotoxic-off/epytech/master/images/logo.png"/>
</p>

# Documentation

<p align = "left">
    <a href = "https://intra.epitech.eu/admin/autolog?format=json">Autologin</a>
</p>

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
# Type: item's type
search(item):
```

```PY
# data is the complete data list
# Type: LIST
data
```

```PY
# len is the len of the data
# Type: INT
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
# Type: item's type
search(item):
```

```PY
# data is the complete data list
# Type: LIST
data
```

```PY
# len is the len of the data
# Type: INT
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
# Type: STR
search(group):
```

```PY
# data is the complete data list
# Type: LIST
data
```

```PY
# len is the len of the data
# Type: INT
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
|      VALUE      | TYPE |
| :-------------: | :--: |
|login            | str  |
|title            | str  |
|internal_email   | str  |
|lastname         | str  |
|firstname        | str  |
|userinfo         | list |
|referent_used    | bool |
|picture          | str  |
|picture_fun      | str  |
|scolaryear       | str  |
|promo            | int  |
|semester         | int  |
|location         | str  |
|documents        | str  |
|userdocs         | str  |
|shell            | str  |
|close            | bool |
|ctime            | str  |
|mtime            | str  |
|id_promo         | str  |
|id_history       | str  |
|course_code      | str  |
|semester_code    | str  |
|school_id        | str  |
|school_code      | str  |
|school_title     | str  |
|old_id_promo     | str  |
|old_id_location  | str  |
|rights           | list |
|invited          | bool |
|studentyear      | int  |
|admin            | bool |
|editable         | bool |
|restrictprofiles | bool |


### Login's data:
|      VALUE      | TYPE |
| :-------------: | :--: |
|login            | str  |
|message          | str  |
|access_token     | str  |

### Notif's data:
```PY
# INT MAX size
```
