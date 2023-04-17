from python_wialon.api import Wialon
from business_logic.wialon.auth import login
from business_logic.wialon.wialon_lib import *
import os
from dotenv import load_dotenv
load_dotenv(verbose=True)

token = os.getenv('WIALON_TOKEN')

wialon_api = Wialon()

def test():

    login(wialon_api, token)
    # print(view_units(wialon_api))
    # print(view_users(wialon_api))
    print(get_resources(wialon_api))
