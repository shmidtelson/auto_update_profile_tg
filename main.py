import os
import shutil
import requests
from faker import Faker
from telethon import TelegramClient, functions, sync
from telethon.tl.functions.account import UpdateProfileRequest

from dotenv import load_dotenv

load_dotenv()

APP_PATH = os.path.dirname(os.path.abspath(__file__))
PATH_TO_IMAGE = os.path.join(APP_PATH, 'ava.jpg')
with TelegramClient(os.getenv("NAME"), os.getenv("APP_ID"), os.getenv("API_HASH")) as client:
    # CHANGE PROFILE
    fake = Faker()
    client(UpdateProfileRequest(
        first_name=fake.first_name_male(),
        last_name=fake.last_name_male(),
        about=fake.sentence(nb_words=6, variable_nb_words=True, ext_word_list=None)
    ))

    # GET IMAGE
    img_url = 'https://cataas.com/c?type=square'

    with open(PATH_TO_IMAGE, 'wb') as output_file, \
            requests.get(img_url, stream=True) as response:
        shutil.copyfileobj(response.raw, output_file)

        # CHANGE AVATAR
        result = client(functions.photos.UploadProfilePhotoRequest(
            file=client.upload_file(PATH_TO_IMAGE)
        ))
