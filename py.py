import requests
import vk_api
from vk_api.utils import get_random_id

vk_session = vk_api.VkApi(token='93b83b59163cec519369a125684f1eb6ae9adcf6e10fc74799dceaa8bcaacc7f8af7d09318586ed7733b3')

from vk_api.longpoll import VkLongPoll, VkEventType
longpoll = VkLongPoll(vk_session)
vk = vk_session.get_api()
for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
   #Слушаем longpoll, если пришло сообщение то:         
        if event.from_user: #Если написали в ЛС
            vk.messages.send( #Отправляем сообщение
                user_id = event.user_id,
                random_id = get_random_id(),
                message = 'Ходор'
            )       