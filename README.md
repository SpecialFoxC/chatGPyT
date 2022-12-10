**ChatGPyTClient**

Unofficial Implementation on chatGPT in python, to use import ChatGPyTClient and initialize the chat: chat = ChatGPyTClient.chatGPT().

To send messages simply use the function: chat.conversation(message), this function replies with the answer.
To reset a conversation use the function: chat.reset().



**discordSelfGPyT**

To use this in the form of a discord selfbot simply put your discord TOKEN in the token field and your discord user_id in the USER_ID field. 
This provides you with 2 self bot commands, 

- /askChatGPT <question>
- /resetChatGPT