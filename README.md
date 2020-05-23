<p align = "left">
    <img alt = "logo" width="451" height="152" src = "https://raw.githubusercontent.com/Neotoxic-off/epytech/master/images/logo.png"/>
</p>

# Epytech 0.8

## IMPORTANT YOUR NEED YOUR AUTOLOGIN URL !
<a href = "https://intra.epitech.eu/admin/autolog?format=json">Generate Autologin Link</a>

## Documentation
<a href = "https://github.com/Neotoxic-off/epytech/blob/master/DOCUMENTATION.md">Documentation</a>

## Install:
```
pip install --upgrade epytech
```
### Import
```PY
from epytech import session, user, login, notif
```

## Example:
```PY
from epytech import user, session, login, notif

class content:
    # Initialisation of the classes
    user = user.init()
    login = login.init()
    notif = notif.init()

    key = session.create("https://intra.epitech.eu/******************")

def loader():
    # Load the content into the classes
    content.user.load(content.key)
    content.login.load(content.key)
    content.notif.load(content.key)

def test():
    i = 0
    loader()

    if content.login.search('message') == "Success":
        print("Login Success")
        print("Welcome %s" % content.user.search('login'))

        if content.notif.data:
            if content.notif.len() > 1:
                print("Your Notifications:\n")
                while i < content.notif.len():
                    print(content.notif.search(i))
                    i += 1
            else:
                print("Your notification: %s" % content.notif.search(0))
    else:
        print("Login Failed")

test()
```
### Result:
```
Login Success
Welcome *********@epitech.eu
You have a notification: Your login time is insufficient (0).
```
