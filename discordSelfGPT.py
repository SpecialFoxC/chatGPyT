from ChatGPTClient import chatGPT
from discum.utils.embed import Embedder
import discum 

TOKEN = "ODY2NzcxMTU1NDA2MTU5ODgy.Gh7mIG.3CIiMmxg3Bpo98Kn29r686CNqBhjb8y37M3THc"
USER_ID = "866771155406159882"
bot = discum.Client(token=TOKEN, log=False)

chat = chatGPT()



@bot.gateway.command
def helloworld(resp):
    if resp.event.ready_supplemental: #ready_supplemental is sent after ready
        user = bot.gateway.session.user
        print("Logged in as {}#{}".format(user['username'], user['discriminator']))
    if resp.event.message:
        m = resp.parsed.auto()
        if m["author"]["id"] == USER_ID:
            message = m['content']
            if message.startswith("/askChatGPT "):
                channelID = m['channel_id']
                messageID = m["id"]
                bot.editMessage(channelID, messageID, "Query: " + message.replace("/askChatGPT ", "") + "\nPending...")
                try:
                    answer = chat.conversation(message.replace("/askChatGPT ", ""))
                except Exception as e:
                    answer = "An unexpected Error has occured."
                bot.editMessage(channelID, messageID, "Query: " + message.replace("/askChatGPT ", "") + "\nchatGPT Answer: " + str(answer))
                print("Sent")
            elif message == "/resetChatGPT":
                chat.reset()
                bot.editMessage(channelID, messageID, "chatGPT conversation reset.")
            else:
                pass
        else:
            pass


bot.gateway.run(auto_reconnect=True)

    
