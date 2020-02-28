from colorama import Fore as f


escolha: str = f.CYAN + "Escolha uma das opções:" + f.RESET

escolha_finalizar: str = \
    f.MAGENTA + "F " + f.RESET + \
    " — " + \
    f.GREEN + " Finalizar o programa." + f.RESET

escolha_pesquisar_mais: str = \
    f.MAGENTA + "P " + f.RESET + \
    " — " + \
    f.GREEN + " Pesquisar mais músicas." + f.RESET

escolha_pesquisar_outra: str = \
    f.MAGENTA + "E " + f.RESET + \
    " — " + \
    f.GREEN + " Escolher outra música para pesquisar." + f.RESET

escolha_numero: str = \
    f.MAGENTA + "Nº" + f.RESET + \
    " — " + \
    f.GREEN + "Selecionar música pelo número." + f.RESET

escolha_confirmar: str = \
    f.MAGENTA + "C " + f.RESET + \
    " — " + \
    f.GREEN + " Confirmar música." + f.RESET

escolha_voltar: str = \
    f.MAGENTA + "V " + f.RESET + \
    " — " + \
    f.GREEN + " Voltar." + f.RESET


qual: str = f.CYAN + "Qual música deseja baixar: " + f.RESET

lista_musica: str = f.CYAN + "Lista com todas as músicas:" + f.RESET

letra_musica: str = f.CYAN + "Letra da música:" + f.RESET

nenhuma_musica: str = f.CYAN + "Nenhuma música foi encontrada." + f.RESET

nova_musica: str = f.CYAN + "Escolhendo nova música..." + f.RESET

invalido: str = f.CYAN + \
    "O valor digitado não é válido, por favor tente novamente:" + f.RESET

fim: str = f.CYAN + "Programa finalizado com sucesso. Aperte ENTER para sair." + f.RESET


limite_excedido: str = f.RED + \
    "Limite de pesquisas excedido. Por favor tente novamente mais tarde. Aperte ENTER para sair." + f.RESET

mensagem_erro: str = f.RED + \
    "Um erro ocorreu e um log foi salvo. Aperte ENTER para sair" + f.RESET

ctrl_c: str = f.RED + \
    "Por favor não aperte Ctrl + C. Aperte ENTER para sair." + f.RESET

# Substitua pelo seu
user_agent: str = "Baixador de Letras - BOT v. 1.0"
