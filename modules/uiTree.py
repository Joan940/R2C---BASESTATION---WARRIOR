# import pygame
# import modules.varGlobals as varGlobals
# from modules.customColors import customColors as cc

# screen = pygame.Surface.get_rect(varGlobals.screen)
# pygame.display.set_caption("Decision Tree UI")

# font = pygame.font.SysFont(None, 24)

# # Load data strategi
# strategi_data = {
#     "Attack": [
#         {"jarak_enemy": 200, "hasil": "passing ke robot 1"},
#         {"jarak_enemy": 200, "hasil": "passing ke robot 2"},
#         {"jarak_enemy": 200, "hasil": "menggiring bola"}
#     ],
#     "Defense": [
#         {"ball_distance": 10, "hasil": "bersiap menerima umpan"},
#         {"ball_distance": 7, "hasil": "menutup ruang lawan"},
#         {"ball_distance": 5, "hasil": "pressing lawan"}
#     ]
# }

# # Keputusan yang diambil
# selected_decision = "pass ke robot 1"

# def draw_tree(data, start_x, start_y, spacing_x, spacing_y):
#     categories = list(data.keys())
#     for i, category in enumerate(categories):
#         cat_x = start_x
#         cat_y = start_y + i * spacing_y
#         draw_text(category, cat_x - 20, cat_y)
        
#         for j, item in enumerate(data[category]):
#             node_x = start_x + spacing_x
#             node_y = start_y + i * spacing_y + (j - 1) * 70

#             if item["hasil"] == selected_decision:
#                 pygame.draw.line(varGlobals.screen, cc.BLACK, (cat_x + 40, cat_y), (node_x - 110, node_y))

#             draw_text(item["hasil"], node_x, node_y)



# def draw_text(text, x, y):
#     text_surface = font.render(text, True, cc.BLACK)
#     text_rect = text_surface.get_rect(center=(x, y))
#     varGlobals.screen.blit(text_surface, text_rect)

# def UI():
#     draw_tree(strategi_data, 200, 200, 300, 220)
#     pygame.display.flip()
        
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
