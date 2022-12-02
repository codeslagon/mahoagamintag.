# Zorunlu gereklidir. Eklemek istediğin bilgileri burda belirt çekinme 😏

import os

class Config(object):
    APP_ID = int(os.environ.get("APP_ID", "29569563"))
    API_HASH = os.environ.get("API_HASH", "d4df9f3d9c24a5292d5cf5a514d11a7a")
    TOKEN = os.environ.get("TOKEN", "5733444846:AAEDB6uDo7Mml9hmUVTczE3jwmqzkXCKQ9E")
