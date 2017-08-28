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
