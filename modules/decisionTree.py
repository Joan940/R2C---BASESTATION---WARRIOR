import json

with open("/media/joan/Windows-SSD/Users/LENOVO/BASESTATION/modules/strategy.json", "r") as file:
    strategy_data = json.load(file)

def get_strategy(catch_ball1, catch_ball2):
    return "Attack" if catch_ball1 == 1 or catch_ball2 == 1 else "Defense"

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

