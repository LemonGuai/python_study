from wxpy import *
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer, ChatterBotCorpusTrainer

chatbot = ChatBot("training demo")
trainer = ListTrainer(chatbot)
trainer.train(["hi", "在？"])

print(chatbot.get_response("hi"))
print(chatbot.get_response("在？"))
bot = Bot()
target = input('请输入要聊天的对象id:')
my_friend = ensure_one(bot.search(target))


@bot.register(my_friend, except_self=True)
def reply_msg(msg):
    print("1", msg.text)
    response = chatbot.get_response(msg.text)
    msg.reply(response)


embed()