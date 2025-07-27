##
# @file decisionTree.py
# @brief Modul untuk memilih strategi dan aksi berdasarkan kondisi permainan sepak bola robot.
#
# Modul ini membaca file JSON eksternal (`strategy.json`) yang berisi definisi strategi dan aksi,
# lalu menentukan strategi utama (Attack/Defense) dan aksi yang sesuai tergantung kondisi lapangan.
#
# Digunakan oleh modul utama simulasi untuk memutuskan aksi robot berdasarkan:
# - Siapa yang memegang bola
# - Jarak ke musuh
# - Status robot dan bola

import json

##
# @var strategy_data
# @brief Struktur data hasil pembacaan file JSON `strategy.json`.
#
# Berisi semua strategi dan aksi yang didefinisikan dalam bentuk dictionary.
# Dibaca sekali saat modul dijalankan menggunakan `json.load()`.

with open("/media/joan/Windows-SSD/Users/LENOVO/BASESTATION/modules/strategy.json", "r") as file:
    strategy_data = json.load(file)

##
# @brief Menentukan strategi utama yang digunakan (Attack atau Defense).
#
# Strategi akan ditentukan berdasarkan status kepemilikan bola oleh dua robot.
# Jika salah satu robot memegang bola (`catch_ball1` atau `catch_ball2` bernilai 1),
# maka strategi adalah "Attack". Jika tidak, maka "Defense".
#
# @param catch_ball1 Status robot 1 memegang bola (1 = ya, 0 = tidak).
# @param catch_ball2 Status robot 2 memegang bola (1 = ya, 0 = tidak).
# @return String strategi yang dipilih: "Attack" atau "Defense".

def get_strategy(catch_ball1, catch_ball2):
    return "Attack" if catch_ball1 == 1 or catch_ball2 == 1 else "Defense"

##
# @brief Menentukan aksi yang dilakukan berdasarkan strategi dan parameter kondisi lapangan.
#
# Fungsi ini membaca strategi dari `strategy_data` dan mencocokkannya dengan kondisi saat ini.
# Cocokkan terhadap jarak ke musuh, status penguasaan bola, dan kondisi lainnya.
#
# Strategi yang didukung: "Attack" dan "Defense"
#
# @param strategy String nama strategi ("Attack" atau "Defense").
# @param jarak_enemy1 Jarak robot ke musuh 1 (opsional).
# @param jarak_enemy2 Jarak robot ke musuh 2 (opsional).
# @param ball_distance Jarak ke bola (opsional, tidak digunakan di versi ini).
# @param enemy1_value Nilai musuh 1 (opsional, tidak digunakan di versi ini).
# @param status_robot Status tambahan robot (opsional, tidak digunakan di versi ini).
# @param catch_ball1 Status robot 1 memegang bola (1 = ya, 0 = tidak).
# @param catch_ball2 Status robot 2 memegang bola (1 = ya, 0 = tidak).
#
# @return String aksi yang direkomendasikan, misalnya:
# - "passing ke robot (2)"
# - "robot (1) menggiring bola"
# - "robot (0) kejar bola"
# - "robot (1) ikuti musuh"
# - atau "Tidak ada aksi yang cocok" jika kondisi tidak terpenuhi.
#
# @retval "Strategi tidak ditemukan" jika strategi tidak ada dalam `strategy_data`.
#
# @note Parameter `ball_distance`, `enemy1_value`, dan `status_robot` disediakan untuk perluasan tetapi belum digunakan secara aktif.

def get_action(strategy, jarak_enemy1=None, jarak_enemy2=None, ball_distance=None, enemy1_value=None, status_robot=None, catch_ball1=None, catch_ball2=None):
    if strategy not in strategy_data["strategi"]:
        return "Strategi tidak ditemukan"

    for action in strategy_data["strategi"][strategy]:

        # ATTACK
        if strategy == "Attack":
            if catch_ball1 == 1:
                if "jarak_enemy1" in action:
                    if jarak_enemy1 is not None and jarak_enemy1 <= action["jarak_enemy1"]:
                        if action.get("umpan"):
                            return f"passing ke robot ({action['target_robot']})"
                        elif action.get("giring"):
                            return action["hasil"]
                    elif jarak_enemy1 is not None and jarak_enemy1 > action["jarak_enemy1"]:
                        if action.get("giring"):
                            return f"robot ({action['target_robot']}) menggiring bola"
            elif catch_ball2 == 1:
                if "jarak_enemy2" in action:
                    if jarak_enemy2 is not None and jarak_enemy2 <= action["jarak_enemy2"]:
                        if action.get("umpan"):
                            return f"passing ke robot ({action['target_robot']})"
                        elif action.get("giring"):
                            return action["hasil"]
                    elif jarak_enemy2 is not None and jarak_enemy2 > action["jarak_enemy2"]:
                        if action.get("giring"):
                            return f"robot ({action['target_robot']}) menggiring bola"

        # DEFENSE
        elif strategy == "Defense":
            if "jarak_enemy1" in action:
                if jarak_enemy1 is not None and jarak_enemy1 > action["jarak_enemy1"]:
                    if action.get("kejar_bola"):
                        return f"robot ({action['target_robot']}) kejar bola"
                    elif action.get("ikuti_musuh"):
                        return action["hasil"]
                elif jarak_enemy1 is not None and jarak_enemy1 <= action["jarak_enemy1"]:
                    if action.get("ikuti_musuh"):
                        return f"robot ({action['target_robot']}) ikuti musuh"
            elif "jarak_enemy2" in action:
                if jarak_enemy2 is not None and jarak_enemy2 > action["jarak_enemy2"]:
                    if action.get("kejar_bola"):
                        return f"robot ({action['target_robot']}) kejar bola"
                    elif action.get("ikuti_musuh"):
                        return action["hasil"]

    return "Tidak ada aksi yang cocok"

