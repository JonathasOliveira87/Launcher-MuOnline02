from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import subprocess
from config import *
import os
import requests
from zipfile import ZipFile



pygame.mixer.init()


def baixar_arquivo_txt(urll, enderecoo):
    # faz requisição ao servidor
    resposta_txt = requests.get(urll)
    if resposta_txt.status_code == requests.codes.OK:
        att = open(enderecoo, 'wb')
        att.write(resposta_txt.content)
        att.close()

    else:
        resposta_txt.raise_for_status()


with open('links.txt', 'r') as arquivo:
    endereços = arquivo.readlines()

for linha in endereços:
    if 'PASTA' in linha:
        meu_endereço_up = linha.split(',')
        meu_endereço_up[1] = meu_endereço_up[0].replace('PASTA = ', '')


        BASE_URLL = meu_endereço_up[1] + f'/update.txt'
        OUTPUT_DIRR = ''
        nome_arquivo_txt = os.path.join(OUTPUT_DIRR, 'update.txt')
        baixar_arquivo_txt(BASE_URLL, nome_arquivo_txt)


def jogar():
    global minha_versao, nova_versao
    with open('links.txt', 'r') as arquivo:
        endereços = arquivo.readlines()

    for linha in endereços:
        if 'VERSAO' in linha:
            minha_versao = linha.split(',')
            minha_versao[1] = minha_versao[0].replace('VERSAO = ', '')

    with open('update.txt', 'r') as versao:
        update = versao.readlines()

    for linha in update:
        if 'VERSAO' in linha:
            nova_versao = linha.split(',')
            nova_versao[1] = nova_versao[0].replace('VERSAO = ', '')


    if minha_versao == nova_versao:
        pygame.mixer.music.load('_som/LevelUp.wav')
        pygame.mixer.music.play()
        launcher.destroy()
        subprocess.call("main.exe", shell=True)

    else:
        bg_ld = Label(frame_cima, image=img_bg, bg='#2C3E50')
        bg_ld.place(x=600, y=20)

        def baixar_arquivo(url, endereco):
            # faz requisição ao servidor
            resposta = requests.get(url)
            if resposta.status_code == requests.codes.OK:
                with open(endereco, 'wb') as novo:
                    novo.write(resposta.content)
                print("Donwload finalizado. Salvo em: {}".format(endereco))
                # ler arquivo
                with ZipFile(f'update{i}.zip', 'r') as zip:
                    # extrair arquivo
                    zip.extractall()
                    zip.close()
                    # deletar arquivo
                    os.remove(f'update{i}.zip')

            else:
                pygame.mixer.music.load('_som/LevelUp.wav')
                pygame.mixer.music.play()
                launcher.destroy()
                subprocess.call("main.exe", shell=True)

        with open('links.txt', 'r') as arquivo:
            endereços = arquivo.readlines()

        for linha in endereços:
            if 'PASTA' in linha:
                meu_endereço_up = linha.split(',')
                meu_endereço_up[1] = meu_endereço_up[0].replace('PASTA = ', '')


                for i in range(1, 9999):
                    online = requests.get(meu_endereço_up[1] + f'/update{i}.zip')
                    if online.status_code == requests.codes.OK:
                        for i in range(1, 9999):
                            BASE_URL = meu_endereço_up[1] + f'/update{i}.zip'
                            OUTPUT_DIR = ''
                            nome_arquivo = os.path.join(OUTPUT_DIR, 'update{}.zip'.format(i))
                            baixar_arquivo(BASE_URL.format(i), nome_arquivo)


def nome():
    pygame.mixer.music.load('_som/ok.wav')
    pygame.mixer.music.play(loops=0)
    def salvarnome():
        keyVal = r'Software\Webzen\Mu\Config'
        try:
            key = OpenKey(HKEY_CURRENT_USER, keyVal, 0, KEY_ALL_ACCESS)
        except:
            key = CreateKey(HKEY_CURRENT_USER, keyVal)
        SetValueEx(key, "ID", 0, REG_SZ, e_nome.get())
        CloseKey(key)
        frame_nome.destroy()
        pygame.mixer.music.load('_som/ok.wav')
        pygame.mixer.music.play(loops=0)
    def cancelar():
        pygame.mixer.music.load('_som/cancel.wav')
        pygame.mixer.music.play(loops=0)
        frame_nome.destroy()
    frame_nome = Frame(launcher, width=280, height=50, bg='#1C2833')
    frame_nome.place(x=1000, y=20)

    e_nome = Entry(frame_nome, fg='#2E86C1', font='Arial 22 bold', relief=SOLID)
    e_nome.place(x=25, y=10, width=160, height=30)

    b_ok = Button(frame_nome, text='OK', fg='#fff', bg='#2E86C1', font='Arial 12 bold', relief=SOLID, command=salvarnome)
    b_ok.place(x=188, y=10, width=38, height=30)

    b_cancelar = Button(frame_nome, text='X', width=3, fg='#fff', bg='#FC0808', font='Arial 12 bold', relief=SOLID, command=cancelar)
    b_cancelar.place(x=228, y=10, height=30)


def config():
    pygame.mixer.music.load('_som/ok.wav')
    pygame.mixer.music.play(loops=0)
    def resolu():
        pygame.mixer.music.load('_som/ok.wav')
        pygame.mixer.music.play(loops=0)
        resolução = box_resolução.get()
        if resolução == '640x480':
            resolução00()
        elif resolução == '800x600':
            resolução01()
        elif resolução == '1024x768':
            resolução02()
        elif resolução == '1280x1024':
            resolução03()
        elif resolução == '1360x768':
            resolução04()
        elif resolução == '1440x900':
            resolução05()
        elif resolução == '1600x900':
            resolução06()
        elif resolução == '1680x1050':
            resolução07()
        elif resolução == '1920x1080':
            resolução08()
        else:
            pass

        frame_conf.destroy()

    frame_conf = Frame(frame_lado, width=225, height=630, bg='#1C2833')
    frame_conf.place(x=10, y=230)

    LabelFrame(frame_conf, text='Ativar e desativar o som!', font='Ivy 9 bold', fg='#fff', bg='#1C2833').place(width=200, height=120, x=15, y=10)
    Button(frame_conf, text='Som (ON)', font='Ivy 11 bold', width=35, height=2, fg='#fff', bg='#2E86C1', relief=SOLID, overrelief=RAISED, command=sonOn).place(width=180, height=30, x=25, y=48)
    Button(frame_conf, text='Som (OFF)', font='Ivy 11 bold', width=35, height=2, fg='#fff', bg='#FC0808', relief=SOLID, overrelief=RAISED, command=sonOff).place(width=180, height=30, x=25, y=83)

    LabelFrame(frame_conf, text='Ativar e desativar música!', font='Ivy 9 bold', fg='#fff', bg='#1C2833').place(width=200, height=120, x=15, y=140)
    Button(frame_conf, text='Música (ON)', font='Ivy 11 bold', width=35, height=2, fg='#fff', bg='#2E86C1', relief=SOLID, overrelief=RAISED, command=musicaON).place(width=180, height=30, x=25, y=178)
    Button(frame_conf, text='Música (OFF)', font='Ivy 11 bold', width=35, height=2, fg='#fff', bg='#FC0808', relief=SOLID, overrelief=RAISED, command=musicaOFF).place(width=180, height=30, x=25, y=213)

    LabelFrame(frame_conf, text='Ativar e desativar modo janela!', font='Ivy 9 bold', fg='#fff', bg='#1C2833').place(width=200, height=120, x=15, y=270)
    Button(frame_conf, text='Janela (ON)', font='Ivy 11 bold', width=35, height=2, fg='#fff', bg='#2E86C1', relief=SOLID, overrelief=RAISED, command=janelaON).place(width=180, height=30, x=25, y=308)
    Button(frame_conf, text='Janela (OFF)', font='Ivy 11 bold', width=35, height=2, fg='#fff', bg='#FC0808', relief=SOLID, overrelief=RAISED, command=janelaOFF).place(width=180, height=30, x=25, y=343)

    res = ['640x480', '800x600', '1024x768', '1280x1024', '1360x768', '1440x900', '1600x900', '1680x1050', '1920x1080']
    LabelFrame(frame_conf, text='Seletor de resoluções', font='Ivy 9 bold', fg='#fff', bg='#1C2833').place(width=200, height=100, x=15, y=400)
    box_resolução = ttk.Combobox(frame_conf, values=res, font=('Ivy 8 bold'), width=20)
    box_resolução.place(x=40, y=450)
    box_resolução.set('(⌐▀͡ ̯ʖ▀)=/̵͇̿̿/’̿’̿̿̿ ̿ ̿̿    ᕙ(▀̿ĺ̯▀̿ ̿)ᕗ')

    b_ok = Button(frame_conf, text='OK', width=15, fg='#fff', bg='#0BBA45', font='Arial 12 bold', relief=SOLID, command=resolu)
    b_ok.place(x=30, y=550, height=40)


launcher = Tk()
launcher.geometry('1320x850+150+35')
launcher.configure(background='#1C2833')
launcher.title('LauncherMuWF')
launcher.iconbitmap('_img/mu.ico')

pygame.mixer.music.load('_som/tema.wav')
pygame.mixer.music.play(loops=1)

# criando frames =======================================================================================================

frame_lado = Frame(launcher, bg='#1C2833', width=245, height=850, )
frame_lado.place(x=0, y=0)

frame_risco = Frame(launcher, bg='#2C3E50', width=180, height=1)
frame_risco.place(x=30, y=210)

frame_cima = Frame(launcher, bg='#1C2833', width=1075, height=83)
frame_cima.place(x=245, y=0)

frame_meio = Frame(launcher, bg='#fff', width=1075, height=767)
frame_meio.place(x=245, y=83)

# abrindo imagens ======================================================================================================

img_logo = Image.open('_img/logo.png')
img_logo = img_logo.resize((155, 60))
img_logo = ImageTk.PhotoImage(img_logo)

img_site = Image.open('_img/site.png')
img_site = img_site.resize((45, 45))
img_site = ImageTk.PhotoImage(img_site)

img_forum = Image.open('_img/forum.png')
img_forum = img_forum.resize((40, 40))
img_forum = ImageTk.PhotoImage(img_forum)

img_loja = Image.open('_img/loja.png')
img_loja = img_loja.resize((45, 45))
img_loja = ImageTk.PhotoImage(img_loja)

img_config = Image.open('_img/config.png')
img_config = img_config.resize((45, 45))
img_config = ImageTk.PhotoImage(img_config)

img_seta = Image.open('_img/setabaixo.png')
img_seta = img_seta.resize((40, 41))
img_seta = ImageTk.PhotoImage(img_seta)

img_bg = Image.open('_img/bg.png')
img_bg = img_bg.resize((1071, 763))
img_bg = ImageTk.PhotoImage(img_bg)

# abrindo backgraund ===================================================================================================

bg_img = Label(frame_meio, image=img_bg, bg='#2C3E50')
bg_img.place(x=0, y=0)

# criando label ========================================================================================================

Label(frame_cima, image=img_logo, bg='#1C2833').place(x=0, y=10)
Label(frame_cima, text='MuOnline PerfectZone', font=('Ivy 17 bold'), fg='#BDC3C7', bg='#1C2833').place(x=170, y=15)
Label(frame_cima, text='www.perfectzone.com.br', font=('Ivy 9 bold'), fg='#BDC3C7', bg='#1C2833').place(x=170, y=50)
Label(frame_cima, text='Idioma:', font=('Ivy 9 bold'), fg='#BDC3C7', bg='#1C2833').place(x=330, y=50)

# criando botões  ======================================================================================================


def selectidioma():
    idioma = b_idioma.get()
    if idioma == 'Por':
        linPor()
    elif idioma == 'Ing':
        linEng()
    elif idioma == 'Esp':
        linSpn()
    else:
        pygame.mixer.music.load('cancel.wav')
        pygame.mixer.music.play(loops=0)
        frame_erro = Frame(launcher, width=250, height=30, bg='#1C2833')
        frame_erro.place(x=620, y=48)
        Button(frame_erro, text='Erro, selecione um idioma', fg='#fff', bg='#FC0808', font='Arial 9 bold', relief=SOLID, command=frame_erro.destroy).place(x=0, y=0)


b_idioma = ttk.Combobox(frame_cima, values=['Por', 'Ing', 'Esp'], font=('Ivy 8 bold'), width=9)
b_idioma.place(x=380, y=50)
b_idioma.set('¯\_(ツ)_/¯')

Button(frame_lado, image=img_site, text='      Site', font=('Ivy 16 bold'), compound=LEFT, anchor=NW, width=200, fg='#BDC3C7', bg='#1C2833', relief=FLAT, command=site).place(x=20, y=30)

Button(frame_cima, text='OK', width=3, fg='#fff', bg='#0BBA45', font='Arial 13 bold', relief=SOLID, overrelief=RAISED,command=selectidioma).place(x=460, y=49, height=22)

Button(frame_lado, image=img_loja, text='      Loja', font=('Ivy 16 bold'), compound=LEFT, anchor=NW, width=200, fg='#BDC3C7', bg='#1C2833', relief=FLAT, command=loja).place(x=20, y=120)

Button(frame_lado, image=img_forum, text='      Forum', font=('Ivy 16 bold'), compound=LEFT, anchor=NW, width=200, fg='#BDC3C7', bg='#2C3E50', relief=FLAT, command=forum).place(x=20, y=250)

Button(frame_lado, image=img_config, text='   Configurações', font=('Ivy 11 bold'), compound=LEFT, anchor=NW, width=200, fg='#BDC3C7', bg='#1C2833', relief=FLAT, command=config).place(x=20, y=780)

Button(frame_cima, text='Play', font=('Ivy 17 bold'), width=14, fg='#fff', bg='#2E86C1', relief=SOLID, overrelief=RAISED, command=jogar).place(x=780, y=20)

Button(frame_cima, image=img_seta, fg='#fff', bg='#2E86C1', relief=SOLID, command=nome).place(x=985, y=20)

Button(frame_meio, text='CADASTRE-SE', font='Ivy 11 bold', width=35, height=2, fg='#fff', bg='#2E86C1', relief=SOLID, overrelief=RAISED, command=cadastro).place(x=670, y=20)

Button(frame_meio, text='EVENTOS', font='Ivy 11 bold', width=35, height=2, fg='#fff', bg='#2C3E50', relief=SOLID, overrelief=RAISED, command=evento).place(x=670, y=72)

Button(frame_meio, text='RANKING', font='Ivy 11 bold', width=35, height=2, fg='#fff', bg='#2C3E50', relief=SOLID, overrelief=RAISED, command=rank).place(x=670, y=124)

Button(frame_meio, text='STAFF', font='Ivy 11 bold', width=35, height=2, fg='#fff', bg='#2C3E50', relief=SOLID, overrelief=RAISED, command=equipe).place(x=670, y=176)


launcher.mainloop()
