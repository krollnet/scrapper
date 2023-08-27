import requests


class Downloader:
    def __init__(self, url, method="GET", params=None):
        self.url = url
        self.methods = method
        self.params = params

    def get_html(self):
        data = requests.get(self.url, params=self.params)
        return data.text

    def save(self, path):
        with open(path, 'w+', encoding='utf-8') as file:
            file.write(self.get_html())









