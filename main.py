from instabot import Bot
import json, re, os
from dotenv import load_dotenv
from pprint import pprint
import argparse


def run_with_cache(func):
    def wrapper(*args, **kwargs):
        filename = func.__name__ + '_cache.json'
        filepath = os.path.join('cache', filename)
        if not os.path.exists(filepath):
            result = func(*args, **kwargs)
            with open(filepath, 'w') as file:
                file.write(json.dumps(result, indent=2))
        with open(filepath, 'r') as file:
            result = json.loads(file.read())
        return result
    return wrapper


@run_with_cache
def fetch_comments(url):
    media_id = bot.get_media_id_from_link(url)
    return bot.get_media_comments_all(media_id)


def get_mentioned_users(comment):
    pattern = r'(?:@)([A-Za-z0-9_](?:(?:[A-Za-z0-9_]|(?:\.(?!\.))){0,28}(?:[A-Za-z0-9_]))?)'
    yield from re.finditer(pattern, comment['text'])


def is_user_exist(user):
    if bot.get_user_id_from_username(user):
        return True
    else:
        return False


@run_with_cache
def get_suited_commenters(comments):
    users = []
    for comment in comments:
        mentioned_users = get_mentioned_users(comment)
        for user in mentioned_users:
            if is_user_exist(user.group(0)[1:]):
                users.append((comment['user_id'], comment["user"]["username"]))
    return users


@run_with_cache
def get_likers(url):
    media_id = bot.get_media_id_from_link(url)
    liker_ids = bot.get_media_likers(media_id)
    likers = []
    for id in liker_ids:
        likers.append(id)
    return likers


@run_with_cache
def get_followers(username):
    user_id = bot.get_user_id_from_username(username=username)
    return bot.get_user_followers(user_id)


if __name__ == '__main__':
    load_dotenv()
    LOGIN = os.getenv('INSTA_LOGIN')
    PASSWORD = os.getenv('INSTA_PASSWORD')

    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument('url', type=str,
                            help='Your instagram post url',
                            default='https://www.instagram.com/p/BtON034lPhu/'
                            )
    args = arg_parser.parse_args()
    if args.url:
        post_url = args.url

    bot = Bot()
    bot.login(username=LOGIN, password=PASSWORD)

    comments = fetch_comments(post_url)
    commenters = get_suited_commenters(comments)
    likers = map(int, get_likers(post_url))
    followers = map(int, get_followers('beautybar.rus'))
    # followers = map(int, get_followers(LOGIN))
    competition = []
    for commenter in commenters:
        if commenter[0] in (set(likers) & set(followers)):
            competition.append(tuple(commenter))
    pprint(competition)
