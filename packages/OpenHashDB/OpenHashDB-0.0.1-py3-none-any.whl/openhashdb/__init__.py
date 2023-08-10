import json
import os
import requests


class OpenHashDB:
    def __init__(self, api_key):
        self.base_url = "https://api.openhashdb.com/v1/"
        self.headers = {
            "content-type": "application/json; charset=iso-8859-15",
        }
