import requests


class YaDiskManager:
    def __init__(self, token):
        self.token = token

    def upload_file(self, file_path, filename):
        upload_url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        headers = {'Content-Type': 'application/json', 'Authorization': f'OAuth {self.token}'}
        params = {'path': file_path, 'overwrite': 'true'}
        resp = requests.get(upload_url, headers=headers, params=params)
        href = resp.json()['href']
        resp = requests.put(href, data=open(filename, 'rb'))
        if resp.status_code == 201:
            print('Success')
        else:
            print('Fall')


TOKEN = ''
uploader = YaDiskManager(TOKEN)
uploader.upload_file('upload_file.txt', 'upload_file.txt')
