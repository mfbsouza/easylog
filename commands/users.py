from bot import bot
from database import db

# database collections
users_col = db.collection('users')

@bot.message_handler(commands=['start'])
def new_user(message):
    try:
        # check if the user already exists
        docs = users_col.where("user_id", "==", message.from_user.id).get()

        if not docs:
            # create a new user
            user = {
                "user_id": message.from_user.id,
                "username": message.chat.username,
            }
            # add user to the users collection
            users_col.document().set(user)
            bot.send_message(message.chat.id, "Usuário adicionado com sucesso")
        else:
            bot.send_message(message.chat.id, "Usuário já cadastrado")
    
    except Exception as e:
        print(f'An Error Accured: {e}')
