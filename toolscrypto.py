import os
import sys
import webbrowser
import requests
import re
import urllib.parse
import signal
import time
from concurrent.futures import ThreadPoolExecutor
from colorama import Fore, Style
from colorama import init
init(autoreset=True)
from tqdm import tqdm
from colorama import Back
from colorama import Fore

# Handler untuk menangkap Ctrl+C
def signal_handler(sig, frame):
    print('\n\033[35mStopping...\033[1;37m')
    sys.exit(0)
signal.signal(signal.SIGINT, signal_handler)
from colorama import Style
from colorama import Fore
from colorama import Back
from colorama import init
init(autoreset=True)
from tqdm import tqdm
from colorama import Back
from colorama import Fore

# Fungsi untuk membuat website
def create_website(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print(f"\033[1;32m[+] {url} is up\033[1;37m")
        else:
            print(f"\033[1;31m[-] {url} is down\033[1;37m")
    except requests.exceptions.RequestException:
        print(f"\033[1;31m[-] {url} is unreachable\033[1;37m")
    except Exception as e:
        print(f"\033[1;31m[-] Error: {str(e)}\033[1;37m")

        # fungsi yuntuk membuat header website
     


# mencari crypto bitcoiN
def search_crypto_bitcoin():
    url =  "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd"
    try:
        response = requests.get(url)
        data = response.json()
        price = data["bpi"]["USD"]["rate"]
        print(f"Bitcoin Price: {price} USD")
    except requests.exceptions.RequestException as e:
        print(f"Error fetching Bitcoin price: {e}")
    except KeyError as e:
        print(f"Error parsing Bitcoin price data: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    except KeyboardInterrupt:
        print("\nExiting...")
        sys.exit(0)
    except SystemExit:
        print("\nExiting...")
        sys.exit(0)
  # fungsi untuk mencari crypto ethereum
def search_crypto_ethereum():
    url = "https://api.coindesk.com/v1/bpi/currentprice/ETH.json"
    try:
        response = requests.get(url)
        data = response.json()
        price = data["bpi"]["USD"]["rate"]
        print(f"Ethereum Price: {price} USD")
    except requests.exceptions.RequestException as e:
        print(f"Error fetching Ethereum price: {e}")
    except KeyError as e:
        print(f"Error parsing Ethereum price data: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    except KeyboardInterrupt:
        print("\nExiting...")
        sys.exit(0)
    except SystemExit:
        print("\nExiting...")
        sys.exit(0)

# fungsi untuk mencari crypto dogecoin

def search_crypto_dogecoin():
    url = "https://api.coindesk.com/v1/bpi/currentprice/DOGE.json"
    try:
        response = requests.get(url)
        data = response.json()
        price = data["bpi"]["USD"]["rate"]
        print(f"Dogecoin Price: {price} USD")
    except requests.exceptions.RequestException as e:
        print(f"Error fetching Dogecoin price: {e}")
    except KeyError as e:
        print(f"Error parsing Dogecoin price data: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    except KeyboardInterrupt:
        print("\nExiting...")
        sys.exit(0)
    except SystemExit:
        print("\nExiting...")
        sys.exit(0)
# fungsi untuk mencari crypto litecoin

def search_crypto_litecoin():
    url = "https://api.coindesk.com/v1/bpi/currentprice/LTC.json"
    try:
        response = requests.get(url)
        data = response.json()
        price = data["bpi"]["USD"]["rate"]
        print(f"Litecoin Price: {price} USD")
    except requests.exceptions.RequestException as e:
        print(f"Error fetching Litecoin price: {e}")
    except KeyError as e:
        print(f"Error parsing Litecoin price data: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    except KeyboardInterrupt:
        print("\nExiting...")
        sys.exit(0)
    except SystemExit:
        print("\nExiting...")
        sys.exit(0)


def header():
    print(Fore.CYAN + Back.BLACK + Style.BRIGHT + """
    ██████╗ ██╗   ██╗███╗   ██╗███████╗███████╗██████╗
    ██╔═══██╗██║   ██║████╗  ██║██╔════╝██╔════╝██╔══██╗
    ██║   ██║██║   ██║██╔██╗ ██║█████╗  █████╗  ██████╔╝
    ██║▄▄ ██║██║   ██║██║╚██╗██║██╔══╝  ██╔══╝  ██╔═══╝
    ╚██████╔╝╚██████╔╝██║ ╚████║███████╗███████╗██║
     ╚═════╝  ╚═════╝ ╚═╝  ╚═══╝ ╚══════╝╚══════╝╚═╝

    """)
    # run crypto
def run_crypto():
    header()
    print(Fore.YELLOW + Back.BLACK + Style.BRIGHT + "Searching for crypto prices...\n")
    search_crypto_bitcoin()
    search_crypto_ethereum()
    search_crypto_dogecoin()
    search_crypto_litecoin()
    print(Fore.YELLOW + Back.BLACK + Style.BRIGHT + "\nCrypto search completed.")
    print(Fore.YELLOW + Back.BLACK + Style.BRIGHT + "Exiting...\n")
    time.sleep(2)
    sys.exit(0)
# fungsi untuk menampilkan menu

def menu():
    os.system('cls' if os.name == 'nt' else 'clear')
    header()
    print(Fore.YELLOW + Back.BLACK + Style.BRIGHT + "1. Search Crypto Prices")
    print(Fore.BLUE + Back.YELLOW + Style.BRIGHT + "2.mencari coin doge")
    print(Fore.YELLOW + Back.BLACK + Style.BRIGHT + "3. Exit")
    choice = input(Fore.YELLOW + Back.BLACK + Style.BRIGHT + "\nChoose an option: ")
    return choice
# fungsi untuk menampilkan menu utama
def main_menu():
    while True:
        choice = menu()
        if choice == '1':
            run_crypto()
        elif choice == '2':
            print(Fore.YELLOW + Back.BLACK + Style.BRIGHT + "run coin doge.\n")
            run_crypto()
        else:
            print(Fore.RED + Back.BLACK + Style.BRIGHT + "Invalid choice. Please try again.")
            time.sleep(2)
            os.system('cls' if os.name == 'nt' else 'clear')
            
# fungsi untuk menampilkan loading
def loading_animation():
    print(Fore.YELLOW + Back.BLACK + Style.BRIGHT + "Loading...")
    for _ in tqdm(range(10), desc="Loading", bar_format="{l_bar}{bar}| {n_fmt}/{total_fmt}"):
        time.sleep(0.5)
    print(Fore.YELLOW + Back.BLACK + Style.BRIGHT + "Loading complete.")
    time.sleep(2)
    os.system('cls' if os.name == 'nt' else 'clear')
# fungsi untuk menampilkan banner
def banner():
    print(Fore.CYAN + Back.BLACK + Style.BRIGHT + """
    ██████╗ ██╗   ██╗███╗   ██╗███████╗███████╗██████╗ 
    ██╔═══██╗██║   ██║████╗  ██║██╔════╝██╔════╝██╔══██╗
    ██║   ██║██║   ██║██╔██╗ ██║█████╗  █████╗  ██████╔╝
    ██║▄▄ ██║██║   ██║██║╚██╗██║██╔══╝  ██╔══╝  ██╔═══╝ 
    ╚██████╔╝╚██████╔╝██║ ╚████║███████╗███████╗██║     
     ╚═════╝  ╚═════╝ ╚═╝  ╚═══╝ ╚══════╝╚══════╝╚═╝     
    """)

# jalankan  semua fungsi
if __name__ == "__main__":
    banner()
    loading_animation()
    main_menu()
    # run_crypto()
    # loading_animation()
    # main_menu()
    # run_crypto()


    # loading_animation()
    # main_menu()
    # ru