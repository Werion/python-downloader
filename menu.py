print("########################")
print("Loading...")
print("########################")
from tqdm import tqdm
import webbrowser
import requests
import config
from colorama import init
from colorama import Fore, Back, Style
from configparser import ConfigParser
import time
from google_speech_recognizer import gsr
from cgtts import gotts
import os
from urllib.request import urlopen
from audio import audio_def


clear = lambda: os.system('cls')

# config read
parser = ConfigParser()
parser.read('config.ini')


# Update check   #######################################

def update_check():
                         # Jakub Siepka
    try:
        checked_ver = urlopen("http://projectpl.cba.pl/quantum/ver.txt")
        checked_ver = str(checked_ver.read(), 'utf-8')
        current_ver_raw = "2"
        current_ver_print = "0.3"
        print("########################")
        print('Current version: ' + current_ver_print)

        if current_ver_raw < checked_ver:
            print("########################")
            print(Back.GREEN + "New update found! Opening link for download new version")
            print(Style.RESET_ALL + "########################")
            webbrowser.open('https://www.dropbox.com/sh/024y3v6k7l3fujy/AABEEIqXkS4njtBv_7nYErKSa?dl=0')
        else:
            print("########################")
            print("No updates found")
            print("########################")
    except:
        print("########################")
        print("Failed to check for updates, check your internet connection!")
        print("########################")
    time.sleep(3)


##################################################

def changelog():
    try:
        clear()
        changelog_ = urlopen("http://projectpl.cba.pl/quantum/changelog.txt")
        print(str(changelog_.read(), 'utf-8'))
        print()
        print()
        input("Press enter to continue...")
        clear()
    except:
        input("Failed to establish internet connection, click enter to go back to menu")
        clear()


def changelog_start():
    if parser.get('settings', 'changelog_automatic_open_at_start') == "True":
        changelog()


## Text menu in Python

def print_menu():  ## Your menu design here
    print(30 * "-", "MENU", 30 * "-")
    print("1. Speech recognition")
    print("2. gTTS")
    print("3. Changelog")
    print("4. Check for updates")
    print("5. gTTS soundboard (ALPHA)")
    print("6. Exit")
    print(67 * "-")


loop = True
changelog_status = True
update_status = True
while loop:
  try:
    clear()
    if update_status == True:
        update_check()
        update_status = False
    time.sleep(2)
    if changelog_status == True:
        changelog_start()
        changelog_status = False
    print_menu()
    choice = input("Enter your choice [1-6]: ")
    choice = int(choice)

    if choice == 1:
        print("Speech Recognition has been selected")
        time.sleep(2)
        clear()
        gsr()
        clear()

    elif choice == 2:
        print("gTTS has been selected")
        time.sleep(2)
        clear()
        gotts()
        clear()
    elif choice == 3:
        clear()
        changelog()
        clear()
    elif choice == 4:
        clear()
        update_check()
    elif choice == 5:
        clear()
        audio_def()
        clear()
    elif choice == 6:
        clear()
        print("Goodbye :)")
        time.sleep(2)
        loop = False  # This will make the while loop to end as not value of loop is set to False
  except:
        # Any integer inputs other than values 1-5 we print an error message
        print("Wrong option selection, try again..")
        time.sleep(3)
        clear()