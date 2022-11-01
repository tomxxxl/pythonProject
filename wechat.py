# 获取微信好友的位置统计信息
from wxpy import *
bot = Bot()
my_friends = bot.friends(update=False)
print(my_friends.stats_text())