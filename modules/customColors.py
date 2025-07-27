##
# @file customColors.py
# @brief Modul definisi warna dan utilitas teks untuk simulasi robot sepak bola.
#
# Modul ini mendefinisikan berbagai warna RGB yang digunakan dalam antarmuka grafis Pygame,
# terutama untuk pewarnaan elemen-elemen visual seperti robot, garis, dan tampilan informasi.
#
# Selain itu, terdapat fungsi `text_to_screen()` untuk menampilkan teks ke layar dengan
# penyesuaian font, warna, dan posisi.
#

from pygame.font import SysFont

##
# @class customColors
# @brief Kelas berisi definisi warna-warna RGB kustom untuk GUI simulator.
#
# Kelas ini berisi konstan warna dalam format RGB dan dictionary warna bernomor
# untuk keperluan pewarnaan elemen visual.

class customColors:
    BLACK = (0, 0, 0)
    WHITE = (245, 245, 245)
    NAVY_BLUE = (1, 63, 86)
    PERU = (205, 133, 63)
    CRIMSON = (220, 20, 60)
    GOLD = (255, 255, 0)
    ARMOUR = (250, 235, 236)
    RED = (255, 0, 0)
    INDIAN_RED = (205, 92, 92)
    DARK_SALMON = (233, 150, 122)
    GRAY = (128, 128, 128)
    EMERALD = (63, 205, 133)
    WATTLE = (205, 204, 63)
    MAHOGANY = (205, 63, 64)
    PAPAYAWHIP = (255, 247, 234)
    PAPAYAWHIP2 = (127, 119, 106)
    PALE_ROSE = (236, 217, 226)
    AFGAN_TAN = (139, 90, 39)
    ENDEAVOUR = (39, 90, 139)
    REGAL_BLUE = (24, 68, 107)
    GRASS_GREEN = (37, 111, 25)
    TURQUOISE = (83, 217, 216)
    BROWN = (85, 44, 0)
    PERSIMMON = (239, 99, 2)
    PURPLE = (58, 30, 225)
    SCOOTER = (41, 136, 150)
    BLUE_STONE = (30, 91, 102)
    WATER_BLUE = (30, 61, 181)
    SKY_BLUE = (127, 170, 255)
    SEAL_BROWN = (69, 10, 10)
    DIRT_BROWN = (145, 91, 39)
    MYRTLE = (25, 54, 12)
    AXOLOTL = (108, 126, 100)
    RAINEE = (180, 189, 176)
    NANDOR = (91, 98, 91)
    FTEK = (209, 107, 2)
    FTEK2 = (150, 77, 2)

    COLORKEY = (255, 0, 255)  # RGB MAGENTA COLOR FOR COLORKEYING

    ##
    # @var colorlist
    # @brief Dictionary pemetaan angka ke warna untuk elemen teks/visual.
    colorlist = {  # Colors for numbers in order
        1: WHITE,
        2: PURPLE,
        3: GOLD,
        4: RAINEE,
        5: TURQUOISE,
        6: PALE_ROSE,
        7: GRAY,
        8: BLACK,
        9: FTEK,
        10: FTEK2,
    }

##
# @brief Menampilkan teks ke layar dengan posisi dan warna yang disesuaikan.
#
# Fungsi ini akan merender teks pada layar menggunakan font Consolas secara default,
# dengan ukuran dan warna tertentu, serta terpusat pada koordinat (x, y).
#
# @param screen Surface layar tujuan.
# @param text Teks atau angka yang akan ditampilkan.
# @param x Posisi X dari pusat teks.
# @param y Posisi Y dari pusat teks.
# @param size Ukuran font (default: 10).
# @param color Warna teks (default: berdasarkan angka di colorlist).
# @param font_type Font alternatif (default: Consolas).
# @return Rect objek area yang digunakan oleh teks.

def text_to_screen(screen, text, x, y, size=10, color=None, font_type=None):
    #pygame.display.update()
    '''Uses the color argument to distinguish b/w an int or a string passed in the field'''
    if color == None: color = customColors.colorlist[text]
    text = str(text)
    if font_type == None:
        font = SysFont('consolas', size, True)
    else:
        font = font_type
    text_width, text_height = font.size(text)
    text = font.render(text, True, color)
    tRect = screen.blit(text, (x - (text_width / 2), y - (text_height / 2)))
    #pygame.display.update()
    return tRect