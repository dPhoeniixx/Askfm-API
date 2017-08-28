# Askfm API

Askfm's private API. Can access all askfm android app features with this repo !

### Prerequisites

```
sudo pip install requests
```

### Installing

1 - Download `` askapi.py `` file and put it in project folder

2 - import the module
```python
#!/usr/bin/env python

import askapi

```


## Example

```python

#!/usr/bin/env python
# -*- coding: utf-8 -*-

import askapi

AskFm = askapi.askapi() # init class
AskFm.login("ASKFM_USERNAME", "ASKFM_PASSWORD") # login 
print AskFm.user # print user data

```

### Features

1. like **( username, answer_id )**
2. register **( username, email, password, Full_Name, GenderId[ 2 = Male, 1 = Female ], BirthDate[28.6.1998] )**
3. follow **( username )**
4. askSomeone **( ['username1', 'username2'], question_body, type [ anonymous, user ] )**
5. getQuestions **( limit=defualt(25), offset=default(0), skip_shoutouts=default(false) )**
6. getNotifications **( limit=default(25), offset=default(0), type=[ANSWER,SHOUTOUT_ANSWER,LIKE,PHOTOPOLL_VOTE,GIFT,MENTION,REGISTRATION,FRIEND_JOIN,FRIEND_ANSWER,FRIEND_AVATAR,FRIEND_BACKGROUND,FRIEND_MOOD,PHOTOPOLL,PHOTOPOLL_MENTION,SELF_BULLYING_NOTICE,SELF_BULLYING_WARNING,SELF_BULLYING_BAN] choice one or more )**
7. streamProfile **( username, limit=default(25), offset=default(0) )**
8. userLikes **( username, limit=default(25), offset=default(0) )**
9. userGifts **( username, limit=default(25), offset=default(0) )**
10. getFriends **( limit=default(25), offset=default(0) )**
11. accountDetails **( username )**
12. getWall **( limit=default(25), from = 0 = from begin )**
13. setAccessToken **( Access_Token )**
14. getAccessToken **()**
