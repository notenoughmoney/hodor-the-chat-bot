import requests
import vk_api
from vk_api.utils import get_random_id

vk_session = vk_api.VkApi(token='24811ca70527c81349ea62068601b77e33eef86d919b7ab51f3ac3ba1d216283f3ec42e920a8783843f47')

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