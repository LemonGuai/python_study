from wxpy import *

bot = Bot()
api_key = "ae401f77c0824d9d9270b49b1a5df5b3"
tuling = Tuling(api_key = api_key)
# flag = True

# while flag:
target = input('请输入要聊天的对象id:')
my_friend = ensure_one(bot.search(target))
    # break


@bot.register(my_friend, except_self=True)
def reply_my_friend(msg):
    tuling.do_reply(msg)


def print_msg(msg):
    print(msg.text)

bot.join()