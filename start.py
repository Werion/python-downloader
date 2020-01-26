# File Host CBA.PL
# Download/Update mechanism, kinda, at first it was to download files from file server and show status of progress.
# It was then scraped, and used to make update system in my other projects.
# Creator Werion
from tqdm import tqdm
import requests
import time
import zipfile
import os


input("Click Enter to start")
# dir = input('Type path (directory have to exist)(to download where downloader are located write .\ ): ')
# a = r'{}gtts.zip'
# b = a.format(dir)
# print(b)
# print("1/2")
chunk_size = 1024
url = "https://www.dropbox.com/s/2s2howpoxj466ar/codename_quantum_%28a_new_way_of_shitposting%29.exe?dl=0"
r = requests.get(url, stream=True)

total_size = int(r.headers['content-length'])
filename = url.split('/')[-1]

with open('codename_quantum_(a new way of shitposting).exe', 'wb') as f:
    for data in tqdm(iterable=r.iter_content(chunk_size=chunk_size), total=total_size / chunk_size, unit='KB'):
        f.write(data)
# Next file
print("")
print("2/2")
url = "http://projectpl.cba.pl/Shiginima_Launcher_SE_v4200.exe"
r = requests.get(url, stream=True)

total_size = int(r.headers['content-length'])
filename = url.split('/')[-1]

with open('Shiginima_Launcher_SE_v4200.exe', 'wb') as f:
    for data in tqdm(iterable=r.iter_content(chunk_size=chunk_size), total=total_size / chunk_size, unit='KB'):
        f.write(data)

print("")
print("Download complete!")

time.sleep(3)
print("Unziping files")
zib_obj = zipfile.ZipFile('gtts.zip', 'r')
zib_obj.extractall('gtts')
zib_obj.close()
print()
print("Deleting waste files")
os.remove('gtts.zip')
print()
print("Done closing downloader")
time.sleep(2)
# os.system(".\gtts\gtts.exe")
