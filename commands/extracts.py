from bot import bot
from database import db
from helpers import float_formater

# database collections
users_col = db.collection('users')
extracts_col = db.collection('extracts')

@bot.message_handler(commands=['new'])
def new_extract(message):
    try:
        # check if user is registred
        docs = users_col.where("user_id", "==", message.from_user.id).get()
        if docs:
            text = message.text.split()
            category = text[1]
            price = float_formater(text[2])

            # create a new extract
            extract = {
                "extract_id": message.message_id,
                "user_id": message.from_user.id,
                "username": message.chat.username,
                "category": category,
                "price": price,
                "timestamp": message.date
            }
            # add extract to the extract collection
            extracts_col.document().set(extract)
            bot.send_message(message.chat.id, "extrato adicionado com sucesso")
        else:
            bot.send_message(message.chat.id, "Usuario não cadastrado, por favor cadastre primeiro antes de tentar adicionar extratos")

    except Exception as e:
        print(f'An Error Accured: {e}')
