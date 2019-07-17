import os
import requests
import shutil
from telethon import TelegramClient, functions, sync
from telethon.tl.functions.account import UpdateProfileRequest

from dotenv import load_dotenv

load_dotenv()

with TelegramClient(os.getenv("NAME"), os.getenv("APP_ID"), os.getenv("API_HASH")) as client:
    from faker import Faker

    # CHANGE PROFILE
    fake = Faker()
    client(UpdateProfileRequest(
        first_name=fake.first_name_male(),
        last_name=fake.last_name_male(),
        about=fake.sentence(nb_words=6, variable_nb_words=True, ext_word_list=None)
    ))

    # GET IMAGE
    img_url = 'https://cataas.com/c?type=square'
    with open('ava.jpg', 'wb') as output_file, \
            requests.get(img_url, stream=True) as response:
        shutil.copyfileobj(response.raw, output_file)

        # CHANGE AVATAR
        result = client(functions.photos.UploadProfilePhotoRequest(
            file=client.upload_file('ava.jpg')
        ))
