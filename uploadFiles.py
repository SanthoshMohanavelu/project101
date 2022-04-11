import dropbox
import os

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)


        f = open(file_from, 'rb')
        dbx.files_upload(f.read(), file_to)

def main():
    access_token = 'sl.BFd4fPi-CpnvRGFwDE1CwwFtUG9w0w0RQ0J818WyMxqPlkCi6m5Px7nYe8X2Iqzuv1m8ZSn0UXE1kCF4rITRDm3zh31-KrsOijwbo7Sa1nZ_t82qzWcubmLTUygnOY4QmTw5HqF0hGFK'
    transferData = TransferData(access_token)
    for root,dirs, files in os.walk(file_from):
        relative_path = os.path.relpath(local_path, file_from)
        dropbox_path = os.path.join(file_to, relative_path)

    file_from = input("Enter the file path to transfer : -")
    file_to = input("enter the full path to upload to dropbox:- ") 

    with open(local_path, 'rb') as f:
        dbx.files_upload(f.read(), dropbox_path, mode=WriteMode('overwrite'))

        transferData.upload_file(file_from, file_to)
        print("file has been moved !!!")



