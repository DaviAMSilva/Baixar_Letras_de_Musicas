import os
import time
import traceback

import requests
from bs4 import BeautifulSoup
from googlesearch import search

import messages as msg

from colorama import Fore as f


search_offset = 0


def clear():
    """Clears the console
    """
    os.system('cls')


def display_pages(musics: list):
    """Prints a list with all saved musics

    Arguments:
        musics {list}
    """
    if len(musics) > 0:
        print("\n" + msg.lista_musica + "\n")
    for i in range(len(musics)):
        print(
            f"{f.MAGENTA}{i + 1}{f.RESET}  —  {f.GREEN}{musics[i]['title']}{f.RESET} por {f.YELLOW}{musics[i]['artist']}{f.RESET}"
        )


def search_pages(music_list: list, search_size: int, mus: str):
    """Search for pages of musics in Google

    Arguments:
        music_list {list}
        search_size {int}
        mus {str}
    """
    global search_offset

    searchStr = "site:letras.mus.br " + mus
    results = search(
        searchStr, tld="com.br", num=search_size, start=search_offset, stop=search_size, pause=1, user_agent=msg.user_agent, lang="pt-BR"
    )
    search_offset += search_size

    found_any = False
    for url in results:
        if url.count("/") != 5 or url.find("blog") != -1 or url.find("traducao") != -1:
            continue

        site = requests.get(url, headers={
            "User-Agent": msg.user_agent, "From": "daviamsilva@hotmail.com"
        })
        soup = BeautifulSoup(site.content, 'html.parser')

        lyrics_soup = soup.select_one(".cnt-letra")

        if lyrics_soup:
            lyrics_list = lyrics_soup.find_all("p")
        else:
            continue

        lyrics = ""
        for l in lyrics_list:
            lyrics += l.getText(strip=True, separator='\n') + "\n\n"

        music_list.append(
            {
                "artist": soup.select_one(".cnt-head_title>h2>a").getText(strip=True),
                "title": soup.select_one(".cnt-head_title>h1").getText(strip=True),
                "lyrics": lyrics[:-2]
                # "soup": soup,
                # "url": url
            }
        )
        found_any = True

    if not found_any:
        # FIXME

        clear()

        print("\n" + msg.nenhuma_musica)


def delete_file(fileStr: str = ".google-cookie"):
    if os.path.exists(fileStr):
        os.remove(fileStr)


def log_error():
    fl = open("Erros - Baixador de Letras.log", mode="a")
    fl.write(
        f"\n{time.strftime('%d/%m/%Y, %H:%M:%S', time.localtime())}\n{traceback.format_exc()}\n==========\n")
    fl.close()
