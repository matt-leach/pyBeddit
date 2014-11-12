pyBeddit
========

Library to connect to the Beddit API.


Usage:

```
>>> from pyBeddit.clients import BedditClient
>>> b = BedditClient(api_endpoint="https://cloudapi.beddit.com")
>>> b.get_token(USERNAME, PASSWORD)
>>> sleep = b.get_latest_sleep()
>>> print sleep
< Sleep 2014-11-11 >
>>> print sleep.properties
< Sleep Properties: Score 100.0 >
>>> print sleep.start_timestamp
1415665948
>>> print sleep.properties.score_amount_of_sleep
90.0
```
