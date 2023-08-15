import requests
import zipfile
import os

class Dlogz:
    def __init__(self, api_url):
        self.api_url = api_url

    def compress_files(self, files, compressed_filename):
        with zipfile.ZipFile(compressed_filename, 'w') as zipf:
            for file_path in files:
                zipf.write(file_path, os.path.basename(file_path))

    def send_compressed_files(self, files):
        try:
            compressed_filename = 'compressed_files.zip'
            self.compress_files(files, compressed_filename)

            with open(compressed_filename, 'rb') as compressed_file:
                response = requests.post(self.api_url, files={'compressed_file': compressed_file})
                if response.status_code == 200:
                    print('Compressed files sent successfully!')
                else:
                    print('Failed to send compressed files. Status code:', response.status_code)

            os.remove(compressed_filename)
        except Exception as e:
            print('Error:', e)