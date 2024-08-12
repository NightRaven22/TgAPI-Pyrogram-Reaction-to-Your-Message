from pyrogram import Client, filters

api_id = 
api_hash = ""

app = Client("my_account", api_id=api_id, api_hash=api_hash)

group_usernames = ["PiterVpiskaNarodChatSpb"]
blacklist = [1215934741, 1099575384]

@app.on_message(filters.text)
def main(_, message):
    try:
        if message.chat.username in group_usernames:
            if message.from_user.id not in blacklist:
                print(f"Новое сообщение - {message.chat.id} | {message.from_user.id} | {message.id}")
                app.send_reaction(message.chat.id, message.id, "👍")
    except Exception as e:
        print(f"Ошибка: {e}")

app.run()
