# -*- coding: utf-8 -*-
#! python3
import telebot # Librería de la API del bot.
import datetime
import os

from telebot import types # Tipos para la API del bot.
import time # Librería para hacer que el programa que controla el bot no se acabe.

TOKEN = '187268667:AAGgQIzgvBGLlceDfW9KfS9hgI_kah43euM' # Nuestro tokken del bot (el que @BotFather nos dió).

bot = telebot.TeleBot(TOKEN) # Creamos el objeto de nuestro bot.
replyTo="None"
def listener(messages): # Con esto, estamos definiendo una función llamada 'listener', que recibe como parámetro un dato llamado 'messages'.
    for m in messages: # Por cada dato 'm' en el dato 'messages'
        if m.content_type == 'text': # Filtramos mensajes que sean tipo texto.
            cid = m.chat.id # Almacenaremos el ID de la conversación.
            print ( "[" + str(cid) + "]: " + m.text) # Y haremos que imprima algo parecido a esto -> [52033876]: /start

bot.set_update_listener(listener) # Así, le decimos al bot que utilice como función escuchadora nuestra función 'listener' declarada arriba.
#Funciones

@bot.message_handler(commands=['hola']) # Indicamos que lo siguiente va a controlar el comando '/miramacho'
def command_hola(m): # Definimos una función que resuleva lo que necesitemos.
    cid = m.chat.id # Guardamos el ID de la conversación para poder responder.
    cu=str(m.from_user.first_name)
    bot.send_message( cid, "Hola " + cu + " Bienvenido al Grupo de Usimte") # Con la función 'send_message()' del bot, enviamos al ID almacenado el texto que queremos.

@bot.message_handler(commands=['blog'])    
def command_blog(m):
    t=time.strftime("%d%m%y")
    if(str(m.chat.title) == 'None'):
        cna=m.chat.id
    else:
        cna =m.chat.title
    t+= str(cna) + ".txt"
    f=open(t,'a')
    def name(m):
        if(str(m.from_user.username) is 'None'):
            us=str(m.from_user.username)
        else: 
             us=str(m.from_user.first_name)+" "+str(m.from_user.last_name)
        f.write(datetime.datetime.fromtimestamp(    int(m.date)   ).strftime('%H:%M:%S')+" "+ us+" : ")
    ci=m.chat.id
    c=m.text[5:].replace("@practi_bot"," ")
    if ( c == ' ' or c is " " or c == " " or c is ' ' ):
        re=bot.send_message(ci,"Cual es el mensaje que desea guardar",reply_markup=types.ForceReply())
        
        def process_reply(message):
              assert re.from_user.id == message.reply_to_message.from_user.id
              c=str(message.text)
              name(message)
              f.write(c+"\n")
              f.close()
        bot.register_for_reply(re,process_reply)
    else:
        name(m)
        f.write(c+"\n")
        f.close()
    
@bot.message_handler(commands=['bloge'])    
def command_blogE(m):
    import time
    t=time.strftime("%d%m%y")
    ci=m.chat.id
    if(str(m.chat.title) == 'None'):
        cna=m.chat.id
    else:
        cna =m.chat.title
    t+= str(cna) + ".txt"
    try:
        doc = open(t, 'rb')
        response=bot.send_document(ci, doc)
        assert response.message_id
        response=bot.send_document(ci, response.document.file_id)
        assert response.message_id
        doc.close()
        os.remove(t)
    except:
        bot.send_message(ci,"Primero debe hacer un blog para este chat")
        
bot.polling(none_stop=True) # Con esto, le decimos al bot que siga funcionando incluso si encuentra algún fallo.