import os
import telebot

bot = telebot.TeleBot(os.getenv("TOKEN"))


@bot.message_handler(commands=['start'])
def start(message):
    mess = f"Hello,<b>{message.from_user.first_name} <u>{message.from_user.last_name}!</u> </b>\n use this " \
           f"bot to check if you subscribed to speciffic telegram channel or not by /help "
    bot.send_message(message.chat.id, mess, parse_mode='html')


@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, "/user_id to see your user id \n /group_id to check the id of group you reposted",
                     parse_mode='html')


@bot.message_handler(commands=['user_id'])
def get_user_id(message):
    bot.send_message(message.chat.id, message.from_user.id, parse_mode='html')


@bot.message_handler(content_types=['photo','text'])
def get_group_id(message):
    if message.forward_from_chat != None:
        bot.send_message(message.chat.id, f"Id of {message.forward_from_chat.type} is"
                                          f" {message.forward_from_chat.id}", parse_mode='html')
    else:
        if message.forward_from != None:
            bot.send_message(message.chat.id, f"Id of bot is {message.forward_from.id}", parse_mode='html')
        else:
            bot.send_message(message.chat.id, f"Please send repost from channel, current message is {message}",
                             parse_mode='html')



    # bot.send_message(message.chat.id, message.text, parse_mode='html')




bot.polling(none_stop=True)

#
# {'content_type': 'text', 'id': 311, 'message_id': 311,
#  'from_user': {'id': 196611193, 'is_bot': False, 'first_name': 'Bulat', 'username': 'Bulatmustafin',
#                'last_name': 'Mustafin', 'language_code': 'ru', 'can_join_groups': None,
#                'can_read_all_group_messages': None, 'supports_inline_queries': None, 'is_premium': None,
#                'added_to_attachment_menu': None}, 'date': 1672580413,
#  'chat': {'id': 196611193, 'type': 'private', 'title': None, 'username': 'Bulatmustafin', 'first_name': 'Bulat',
#           'last_name': 'Mustafin', 'is_forum': None, 'photo': None, 'bio': None, 'join_to_send_messages': None,
#           'join_by_request': None, 'has_private_forwards': None, 'has_restricted_voice_and_video_messages': None,
#           'description': None, 'invite_link': None, 'pinned_message': None, 'permissions': None,
#           'slow_mode_delay': None, 'message_auto_delete_time': None, 'has_protected_content': None,
#           'sticker_set_name': None, 'can_set_sticker_set': None, 'linked_chat_id': None, 'location': None,
#           'active_usernames': None, 'emoji_status_custom_emoji_id': None}, 'sender_chat': None, 'forward_from': None,
#  'forward_from_chat': {'id': -1001137013667, 'type': 'channel', 'title': 'Канал Булата Мустафина',
#                        'username': 'tomyumbulat', 'first_name': None, 'last_name': None, 'is_forum': None,
#                        'photo': None, 'bio': None, 'join_to_send_messages': None, 'join_by_request': None,
#                        'has_private_forwards': None, 'has_restricted_voice_and_video_messages': None,
#                        'description': None, 'invite_link': None, 'pinned_message': None, 'permissions': None,
#                        'slow_mode_delay': None, 'message_auto_delete_time': None, 'has_protected_content': None,
#                        'sticker_set_name': None, 'can_set_sticker_set': None, 'linked_chat_id': None, 'location': None,
#                        'active_usernames': None, 'emoji_status_custom_emoji_id': None}, 'forward_from_message_id': 1491,
#  'forward_signature': None, 'forward_sender_name': None, 'forward_date': 1672562195, 'is_automatic_forward': None,
#  'reply_to_message': None, 'via_bot': None, 'edit_date': None, 'has_protected_content': None, 'media_group_id': None,
#  'author_signature': None, 'text': 'С новым годом, дорогие! В этом году я точно буду социальнее ))', 'entities': None,
#  'caption_entities': None, 'audio': None, 'document': None, 'photo': None, 'sticker': None, 'video': None,
#  'video_note': None, 'voice': None, 'caption': None, 'contact': None, 'location': None, 'venue': None,
#  'animation': None, 'dice': None, 'new_chat_member': None, 'new_chat_members': None, 'left_chat_member': None,
#  'new_chat_title': None, 'new_chat_photo': None, 'delete_chat_photo': None, 'group_chat_created': None,
#  'supergroup_chat_created': None, 'channel_chat_created': None, 'migrate_to_chat_id': None,
#  'migrate_from_chat_id': None, 'pinned_message': None, 'invoice': None, 'successful_payment': None,
#  'connected_website': None, 'reply_markup': None, 'message_thread_id': None, 'is_topic_message': None,
#  'forum_topic_created': None, 'forum_topic_closed': None, 'forum_topic_reopened': None, 'json': {'message_id': 311,
#                                                                                                  'from': {
#                                                                                                      'id': 196611193,
#                                                                                                      'is_bot': False,
#                                                                                                      'first_name': 'Bulat',
#                                                                                                      'last_name': 'Mustafin',
#                                                                                                      'username': 'Bulatmustafin',
#                                                                                                      'language_code': 'ru'},
#                                                                                                  'chat': {
#                                                                                                      'id': 196611193,
#                                                                                                      'first_name': 'Bulat',
#                                                                                                      'last_name': 'Mustafin',
#                                                                                                      'username': 'Bulatmustafin',
#                                                                                                      'type': 'private'},
#                                                                                                  'date': 1672580413,
#                                                                                                  'forward_from_chat': {
#                                                                                                      'id': -1001137013667,
#                                                                                                      'title': 'Канал Булата Мустафина',
#                                                                                                      'username': 'tomyumbulat',
#                                                                                                      'type': 'channel'},
#                                                                                                  'forward_from_message_id': 1491,
#                                                                                                  'forward_date': 1672562195,
#                                                                                                  'text': 'С новым годом, дорогие! В этом году я точно буду социальнее ))'}}