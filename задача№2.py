from pprint import pprint

import requests

TOKEN = ""
class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': f'OAuth {self.token}'
        }

    def upload_file_to_disk(self, file_path, filename):
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'OAuth {self.token}'
        }
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        params = {"path": file_path, "overwrite": "true"}
        response = requests.get(upload_url, headers=headers, params=params)
        response_data = response.json()
        pprint(response_data)
        upload_to_url = response_data["href"]

        response = requests.put(upload_to_url, data=open(filename, 'rb'))
        if response.status_code == 201:
            print("Success")

if __name__ == '__main__':
    uploader = YaUploader(token=TOKEN)
    uploader.upload_file_to_disk("test2205.txt", "test.txt")




