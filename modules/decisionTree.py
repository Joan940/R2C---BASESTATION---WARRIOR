import json

with open("/media/joan/Windows-SSD/Users/LENOVO/BASESTATION - R2C - WARRIOR (coba)/modules/strategy.json", "r") as file:
    strategy_data = json.load(file)

def get_strategy(catch_ball):
    return "Attack" if catch_ball == 1 else "Defense"

def get_action(strategy, jarak_enemy=None, ball_distance=None, enemy1_value=None, status_robot=None):
    if strategy not in strategy_data["strategi"]:
        return "Strategi tidak ditemukan"

    for action in strategy_data["strategi"][strategy]:
        
        # Jika strategi Attack, gunakan jarak_actual untuk menentukan aksi
        if strategy == "Attack":
            if "jarak_enemy" in action:
                if jarak_enemy is not None and jarak_enemy <= action["jarak_enemy"]:
                    if action.get("umpan"):
                        return f"passing ke robot ({action['target_robot']})"
                    elif action.get("giring"):
                        return action["hasil"]
                elif jarak_enemy is not None and jarak_enemy > action["jarak_enemy"]:
                    if action.get("giring"):
                        return action["hasil"]

        # Jika strategi Defense, gunakan ball_distance dan enemy1_value
        elif strategy == "Defense":
            if "ball_distance" in action and "enemy1_value" in action:
                enemy_value_eval = abs(eval(action["enemy1_value"]) - enemy1_value)
                
                if (ball_distance is not None and ball_distance <= action["ball_distance"] and
                    enemy_value_eval <= 30):

                    if "status_robot" in action and action["status_robot"] == status_robot:
                        return action["hasil"]

    return "Tidak ada aksi yang cocok"

