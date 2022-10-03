from winreg import *
import webbrowser
import pygame


pygame.mixer.init()


def linEng():
    pygame.mixer.music.load('_som/menu.wav')
    pygame.mixer.music.play(loops=0)
    keyVal = r'Software\Webzen\Mu\Config'
    try:
        key = OpenKey(HKEY_CURRENT_USER, keyVal, 0, KEY_ALL_ACCESS)
    except:
        key = CreateKey(HKEY_CURRENT_USER, keyVal)
    SetValueEx(key, "LangSelection", 0, REG_SZ, 'Eng')
    CloseKey(key)


def linPor():
    pygame.mixer.music.load('_som/menu.wav')
    pygame.mixer.music.play(loops=0)
    keyVal = r'Software\Webzen\Mu\Config'
    try:
        key = OpenKey(HKEY_CURRENT_USER, keyVal, 0, KEY_ALL_ACCESS)
    except:
        key = CreateKey(HKEY_CURRENT_USER, keyVal)
    SetValueEx(key, "LangSelection", 0, REG_SZ, 'Por')
    CloseKey(key)


def linSpn():
    pygame.mixer.music.load('_som/menu.wav')
    pygame.mixer.music.play(loops=0)
    keyVal = r'Software\Webzen\Mu\Config'
    try:
        key = OpenKey(HKEY_CURRENT_USER, keyVal, 0, KEY_ALL_ACCESS)
    except:
        key = CreateKey(HKEY_CURRENT_USER, keyVal)
    SetValueEx(key, "LangSelection", 0, REG_SZ, 'Spn')
    CloseKey(key)


def musicaON():
    pygame.mixer.music.load('_som/menu.wav')
    pygame.mixer.music.play(loops=0)
    keyVal = r'Software\Webzen\Mu\Config'
    try:
        key = OpenKey(HKEY_CURRENT_USER, keyVal, 0, KEY_ALL_ACCESS)
    except:
        key = CreateKey(HKEY_CURRENT_USER, keyVal)
    SetValueEx(key, "MusicOnOFF", 0, REG_DWORD, 1)
    CloseKey(key)


def musicaOFF():
    pygame.mixer.music.load('_som/cancel.wav')
    pygame.mixer.music.play(loops=0)
    keyVal = r'Software\Webzen\Mu\Config'
    try:
        key = OpenKey(HKEY_CURRENT_USER, keyVal, 0, KEY_ALL_ACCESS)
    except:
        key = CreateKey(HKEY_CURRENT_USER, keyVal)
    SetValueEx(key, "MusicOnOFF", 0, REG_DWORD, 0)
    CloseKey(key)


def sonOff():
    pygame.mixer.music.load('_som/cancel.wav')
    pygame.mixer.music.play(loops=0)
    keyVal = r'Software\Webzen\Mu\Config'
    try:
        key = OpenKey(HKEY_CURRENT_USER, keyVal, 0, KEY_ALL_ACCESS)
    except:
        key = CreateKey(HKEY_CURRENT_USER, keyVal)
    SetValueEx(key, "SoundOnOff", 0, REG_DWORD, 0)
    CloseKey(key)


def sonOn():
    pygame.mixer.music.load('_som/menu.wav')
    pygame.mixer.music.play(loops=0)
    keyVal = r'Software\Webzen\Mu\Config'
    try:
        key = OpenKey(HKEY_CURRENT_USER, keyVal, 0, KEY_ALL_ACCESS)
    except:
        key = CreateKey(HKEY_CURRENT_USER, keyVal)
    SetValueEx(key, "SoundOnOff", 0, REG_DWORD, 1)
    CloseKey(key)


def janelaOFF():
    pygame.mixer.music.load('_som/cancel.wav')
    pygame.mixer.music.play(loops=0)
    keyVal = r'Software\Webzen\Mu\Config'
    try:
        key = OpenKey(HKEY_CURRENT_USER, keyVal, 0, KEY_ALL_ACCESS)
    except:
        key = CreateKey(HKEY_CURRENT_USER, keyVal)
    SetValueEx(key, 'WindowMode', 0, REG_DWORD, 0)
    CloseKey(key)


def janelaON():
    pygame.mixer.music.load('_som/menu.wav')
    pygame.mixer.music.play(loops=0)
    keyVal = r'Software\Webzen\Mu\Config'
    try:
        key = OpenKey(HKEY_CURRENT_USER, keyVal, 0, KEY_ALL_ACCESS)
    except:
        key = CreateKey(HKEY_CURRENT_USER, keyVal)
    SetValueEx(key, "WindowMode", 0, REG_DWORD, 1)
    CloseKey(key)


def resolução00():
        keyVal = r'Software\Webzen\Mu\Config'
        try:
            key = OpenKey(HKEY_CURRENT_USER, keyVal, 0, KEY_ALL_ACCESS)
        except:
            key = CreateKey(HKEY_CURRENT_USER, keyVal)
        SetValueEx(key, "Resolution", 0, REG_DWORD, 0)
        CloseKey(key)


def resolução01():
    keyVal = r'Software\Webzen\Mu\Config'
    try:
        key = OpenKey(HKEY_CURRENT_USER, keyVal, 0, KEY_ALL_ACCESS)
    except:
        key = CreateKey(HKEY_CURRENT_USER, keyVal)
    SetValueEx(key, "Resolution", 0, REG_DWORD, 1)
    CloseKey(key)


def resolução02():
        keyVal = r'Software\Webzen\Mu\Config'
        try:
            key = OpenKey(HKEY_CURRENT_USER, keyVal, 0, KEY_ALL_ACCESS)
        except:
            key = CreateKey(HKEY_CURRENT_USER, keyVal)
        SetValueEx(key, "Resolution", 0, REG_DWORD, 2)
        CloseKey(key)


def resolução03():
    keyVal = r'Software\Webzen\Mu\Config'
    try:
        key = OpenKey(HKEY_CURRENT_USER, keyVal, 0, KEY_ALL_ACCESS)
    except:
        key = CreateKey(HKEY_CURRENT_USER, keyVal)
    SetValueEx(key, "Resolution", 0, REG_DWORD, 3)
    CloseKey(key)


def resolução04():
        keyVal = r'Software\Webzen\Mu\Config'
        try:
            key = OpenKey(HKEY_CURRENT_USER, keyVal, 0, KEY_ALL_ACCESS)
        except:
            key = CreateKey(HKEY_CURRENT_USER, keyVal)
        SetValueEx(key, "Resolution", 0, REG_DWORD, 4)
        CloseKey(key)


def resolução05():
        keyVal = r'Software\Webzen\Mu\Config'
        try:
            key = OpenKey(HKEY_CURRENT_USER, keyVal, 0, KEY_ALL_ACCESS)
        except:
            key = CreateKey(HKEY_CURRENT_USER, keyVal)
        SetValueEx(key, "Resolution", 0, REG_DWORD, 5)
        CloseKey(key)


def resolução06():
    keyVal = r'Software\Webzen\Mu\Config'
    try:
        key = OpenKey(HKEY_CURRENT_USER, keyVal, 0, KEY_ALL_ACCESS)
    except:
        key = CreateKey(HKEY_CURRENT_USER, keyVal)
    SetValueEx(key, "Resolution", 0, REG_DWORD, 6)
    CloseKey(key)


def resolução07():
        keyVal = r'Software\Webzen\Mu\Config'
        try:
            key = OpenKey(HKEY_CURRENT_USER, keyVal, 0, KEY_ALL_ACCESS)
        except:
            key = CreateKey(HKEY_CURRENT_USER, keyVal)
        SetValueEx(key, "Resolution", 0, REG_DWORD, 7)
        CloseKey(key)


def resolução08():
    keyVal = r'Software\Webzen\Mu\Config'
    try:
        key = OpenKey(HKEY_CURRENT_USER, keyVal, 0, KEY_ALL_ACCESS)
    except:
        key = CreateKey(HKEY_CURRENT_USER, keyVal)
    SetValueEx(key, "Resolution", 0, REG_DWORD, 8)
    CloseKey(key)


def site():
    pygame.mixer.music.load('_som/ok.wav')
    pygame.mixer.music.play(loops=0)
    with open('links.txt', 'r') as arquivo:
        endereços = arquivo.readlines()

    for linha in endereços:
        if 'SITE' in linha:
            dado = linha.split(',')
            dado[1] = dado[0].replace('SITE = ', '')
            webbrowser.open(dado[1])


def forum():
    pygame.mixer.music.load('_som/ok.wav')
    pygame.mixer.music.play(loops=0)
    with open('links.txt', 'r') as arquivo:
        endereços = arquivo.readlines()

    for linha in endereços:
        if 'FORUM' in linha:
            dado = linha.split(',')
            dado[1] = dado[0].replace('FORUM = ', '')
            webbrowser.open(dado[1])


def loja():
    pygame.mixer.music.load('_som/ok.wav')
    pygame.mixer.music.play(loops=0)
    with open('links.txt', 'r') as arquivo:
        endereços = arquivo.readlines()

    for linha in endereços:
        if 'SHOP' in linha:
            dado = linha.split(',')
            dado[1] = dado[0].replace('SHOP = ', '')
            webbrowser.open(dado[1])


def cadastro():
    pygame.mixer.music.load('_som/ok.wav')
    pygame.mixer.music.play(loops=0)
    with open('links.txt', 'r') as arquivo:
        endereços = arquivo.readlines()

    for linha in endereços:
        if 'CADASTRO' in linha:
            dado = linha.split(',')
            dado[1] = dado[0].replace('CADASTRO = ', '')
            webbrowser.open(dado[1])


def evento():
    pygame.mixer.music.load('_som/ok.wav')
    pygame.mixer.music.play(loops=0)
    with open('links.txt', 'r') as arquivo:
        endereços = arquivo.readlines()

    for linha in endereços:
        if 'EVENTO' in linha:
            dado = linha.split(',')
            dado[1] = dado[0].replace('EVENTO = ', '')
            webbrowser.open(dado[1])


def rank():
    pygame.mixer.music.load('_som/ok.wav')
    pygame.mixer.music.play(loops=0)
    with open('links.txt', 'r') as arquivo:
        endereços = arquivo.readlines()

    for linha in endereços:
        if 'RANKING' in linha:
            dado = linha.split(',')
            dado[1] = dado[0].replace('RANKING = ', '')
            webbrowser.open(dado[1])


def equipe():
    pygame.mixer.music.load('_som/ok.wav')
    pygame.mixer.music.play(loops=0)
    with open('links.txt', 'r') as arquivo:
        endereços = arquivo.readlines()

    for linha in endereços:
        if 'EQUIPE' in linha:
            dado = linha.split(',')
            dado[1] = dado[0].replace('EQUIPE = ', '')
            webbrowser.open(dado[1])



