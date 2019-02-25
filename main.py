from instabot import Bot

LOGIN='cosmicpython'
PASSWORD='Evx9WBDCv7xIaXYX8j0'

bot = Bot()
bot.login(username=LOGIN, password=PASSWORD)
user_id = bot.get_user_id_from_username("lego")
user_info = bot.get_user_info(user_id)
print(user_info['biography'])