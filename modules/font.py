##
# @file font.py
# @brief Modul untuk menampilkan teks pada layar Pygame menggunakan font kustom.
#
# Modul ini menyediakan fungsi `text_to_screen()` yang digunakan untuk menampilkan
# teks di layar simulasi robot sepak bola. Fungsi ini memuat font dari direktori
# spesifik dan mengatur warna, ukuran, serta posisi teks agar ditampilkan secara
# terpusat.
#
# @note Font default yang digunakan berada di dalam direktori assets lokal,
# dan diasumsikan tersedia saat modul dijalankan.

import pygame
from modules.customColors import customColors as cc

##
# @brief Menampilkan teks ke layar menggunakan font kustom dari file TTF.
#
# Fungsi ini merender teks menggunakan font Consolas dari path lokal.
# Teks akan ditampilkan terpusat di titik (x, y) pada layar.
#
# @param screen Objek surface Pygame tempat teks akan ditampilkan.
# @param text String atau angka yang akan ditampilkan.
# @param x Koordinat X posisi tengah teks.
# @param y Koordinat Y posisi tengah teks.
# @param size Ukuran font (default: 10).
# @param color Warna font (default: diambil dari colorlist berdasarkan teks).
# @param font_type Objek font alternatif (default: font dari file .ttf lokal).
# @return pygame.Rect Area tempat teks dirender.
#
# @note
# - Jika parameter `color` tidak diberikan, warna diambil dari dictionary `cc.colorlist`.
# - Jika `font_type` tidak diberikan, font default adalah "Consolas.ttf" dari folder lokal.

def text_to_screen(screen, text, x, y, size=10, color=None, font_type=None):
    #pygame.display.update()
    '''Uses the color argument to distinguish b/w an int or a string passed in the field'''
    if color == None: color = cc.colorlist[text]
    text = str(text)
    if font_type == None:
        font = pygame.font.SysFont('C:/Users/LENOVO/BASESTATION - R2C - WARRIOR (coba)/assets/Consolas.ttf', size, True)
    else:
        font = font_type
    text_width, text_height = font.size(text)
    text = font.render(text, True, color)
    tRect = screen.blit(text, (x - (text_width / 2), y - (text_height / 2)))
    # pygame.display.update()
    return tRect