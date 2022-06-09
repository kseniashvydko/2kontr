import os
import numpy as np
import threading
import requests

pathh = 'planet_data/'

def parse_users(planet, save_path):
    for planets in planet: #проверяем данные
        if len(planets['collection']['items']) == 0:
            continue
        path = save_path + str(planets['collection']['href'][42:52])
        os.mkdir(path)
        with open(path + "/title.txt", "w") as file: #заголовок
            title = planets['collection']['items'][0]['data'][0]['title']
            file.writelines(f"{str(title)}")
        with open(path + "/description.txt", "w") as file: #описание
            file.writelines(f"{str(planets['collection']['items'][0]['data'][0]['description'])}")


# получение планет
def get_planet():
    images = []
    for page in range(1, 31):
        response = requests.get(f'https://images-api.nasa.gov/search?q=earth%2022-05-{page}&media_type=image')
        currencies = response.json() #загоняем все из файла в переменную
        images.append(currencies)
    return images




# запускаем в 4 потоках
def start_thread(save_path):
    users = get_planet()
    threads = []
    for list_slice in np.array_split(users, 4):
        thread = threading.Thread(target=parse_users, args=(list(list_slice), save_path)) #создаем и запускаем поток
        thread.start()
        threads.append(thread)
    for thread in threads:
        thread.join()

start_thread(pathh)