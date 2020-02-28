import os
import urllib
from sys import exit

from colorama import Style as s, init

import messages as msg
from functions import clear, delete_file, display_pages, log_error, search_pages

init()
os.system("title Baixador de Letras")
print(s.BRIGHT)

try:
    while True:
        # Iniciando variáveis
        search_size = 5
        music_list = []

        # Procurando no Google
        clear()
        print("\n" + msg.qual)
        mus = input("\n")

        if len(mus) == 0:
            clear()
            print("\n" + msg.invalido)
            continue

        try:
            search_pages(music_list, search_size, mus)
        except urllib.error.HTTPError as e:
            if e.code == 429:
                clear()
                print(f"\n{msg.limite_excedido}")
                input("\n")
                delete_file(".google-cookie")
                exit(0)
            else:
                raise e

        restart = False
        while not restart:

            if len(music_list) > 0:

                clear()

                display_pages(music_list)

                print(f"""
{msg.escolha}

{msg.escolha_numero}
{msg.escolha_finalizar}
{msg.escolha_pesquisar_mais}
{msg.escolha_pesquisar_outra}
"""
                      )
                choice = input()

                if choice == "P" or choice == "p":
                    search_pages(music_list, search_size, mus)
                    continue
                elif choice == "E" or choice == "e":
                    restart = True
                    continue
                elif choice == "F" or choice == "f":
                    delete_file(".google-cookie")
                    exit(0)
                else:
                    try:
                        index = int(choice)
                        if index < 1:
                            raise IndexError

                        music = music_list[index-1]

                        clear()

                        print(f"""
{msg.letra_musica}

{music_list[index-1]['lyrics']}"""
                              )

                        print(f"""
{msg.escolha}

{msg.escolha_confirmar}
{msg.escolha_finalizar}
{msg.escolha_voltar}
"""
                              )
                        choice2 = input()

                        if choice2 == "V" or choice2 == "v":
                            continue
                        elif choice2 == "F" or choice2 == "f":
                            delete_file(".google-cookie")
                            exit(0)
                        else:
                            music_filename = f"{music['title']} - {music['artist']}.txt"
                            fh = open(
                                music_filename, "w", encoding="utf-8"
                            )
                            fh.write(
                                f"{music['title']} - {music['artist']}\n\n{music['lyrics']}")
                            fh.close()

                        break
                    except (ValueError, IndexError):

                        clear()

                        print("\n" + msg.invalido)
                        continue

            else:
                print(f"""
{msg.escolha}
{msg.escolha_pesquisar_outra}
{msg.escolha_finalizar}
"""
                      )
                choice3 = input()

                if choice3 == "F" or choice3 == "f":
                    delete_file(".google-cookie")
                    exit(0)
                else:
                    restart = True
                    continue

        else:
            print(msg.nova_musica)
            continue

        clear()

        print("\n" + msg.fim)

        input("\n")

        os.startfile(music_filename)

        break
except Exception as e:
    log_error()

    clear()

    print("\n" + msg.mensagem_erro)
    input("\n")
except KeyboardInterrupt:
    clear()

    print("\n" + msg.ctrl_c)
    input("\n")
finally:
    clear()
    delete_file(".google-cookie")
