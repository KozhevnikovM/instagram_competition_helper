# Instagram competition helper
Script print users, who leave comment with friend name,
liked post,
and subscribe as follower

## System requirements:
python 3.6

## Installation:
```bash
$ pip install -r requirements.txt
```

## How to use:

python main.py your_url_here

```bash
$ python main.py https://www.instagram.com/p/BtON034lPhu/
2019-02-26 13:42:01,845 - INFO - Instabot Started
2019-02-26 13:42:03,486 - INFO - Logged-in successfully as 'cosmicpython'!
2019-02-26 13:42:09,828 - ERROR - Request returns 404 error!
[(6997916230, 'ev_k110791')]
2019-02-26 13:42:16,164 - INFO - Bot stopped. Worked: 1 day, 1:16:46.878143
2019-02-26 13:42:16,166 - INFO - Total requests: 2340
```

## Warning:
Checking than user exist make take a long time.
And I decided use files for caching responses.
If you do not want to use old cached info, you need to clear folder named 'cache' 