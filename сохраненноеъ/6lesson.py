# Поговорите с детьми о:
#
# Что такое переменные? (пример: score = 0)
#
# Что такое список? (пример: visited_blocks = [])
#
# Зачем сохранять данные? (Чтобы продолжать игру позже, сделать "очки", уровни, прогресс.)
#
# Что такое файл? Как сохранить туда информацию? (Текст, числа, списки...)
#
from mcpi.minecraft import Minecraft
# mc = Minecraft.create()

# Проверяем блок под игроком: если золото — даём очки
# 1. Переменная: система очков
# Пример: сохраняем очки
# 🧪 Основной блок (1 час 10 минут)
# ✅ Пример 1: Работа с переменной и сохранение в файл
# score = 25
#
# # Сохраняем в файл
# with open("score.txt", "w") as file:
#     file.write(str(score))
#
# print("Очки сохранены.")


# # Загружаем очки
# with open("score.txt", "r") as file:
#     score = int(file.read())
#
# print("Загруженные очки:", score)

#
#
# # ✅ Пример 2: Работа со списком координат
#
# # Пример: список блоков, которые посетил игрок
# visited = [(341, 2123, -22243), (124, 4215, 236)]
#
# # Сохраняем построчно
# with open("visited.txt", "w") as file:
#     for x, y, z in visited:
#         file.write(f"{x},{y},{z}\n")
#
# print("Координаты сохранены.")
#
# Загружаем список координат
# visited = []
#
# with open("visited.txt", "r") as file:
#     for line in file:
#         x, y, z = map(int, line.strip().split(","))
#         visited.append((x, y, z))
#
# print("Загруженные координаты:", visited)


#
# import time
#
# mc = Minecraft.create()
#
# score = 0
#
# while True:
#     pos = mc.player.getTilePos()
#     block_below = mc.getBlock(pos.x, pos.y - 1, pos.z)
#
#     if block_below == 41:  # золото
#         score += 10
#         mc.postToChat(f"U at gold! score: {score}")
#         time.sleep(1)

from mcpi.minecraft import Minecraft
from mcpi import block
from decouple import config
import time
import os
import random

# === Настройки из .env ===
ARENA_SIZE = config("ARENA_SIZE", cast=int)
GROUND_Y = config("GROUND_Y", cast=int)
NUM_GOLD_BLOCKS = config("NUM_GOLD_BLOCKS", cast=int)
SCORE_PER_BLOCK = config("SCORE_PER_BLOCK", cast=int)
TOTAL_SCORE = NUM_GOLD_BLOCKS * SCORE_PER_BLOCK

SCORE_FILE = "gold_score.txt"
FOUND_FILE = "gold_found.txt"

# === Подключение к Minecraft ===
mc = Minecraft.create()

# === Получение позиции игрока ===
player_pos = mc.player.getTilePos()
base_x = player_pos.x
base_y = GROUND_Y
base_z = player_pos.z

# === Постройка арены ===
mc.setBlocks(base_x - 1, base_y, base_z - 1,
             base_x + ARENA_SIZE, base_y + 5, base_z + ARENA_SIZE,
             block.AIR.id)  # Очистка

mc.setBlocks(base_x, base_y - 1, base_z,
             base_x + ARENA_SIZE - 1, base_y - 1, base_z + ARENA_SIZE - 1,
             block.GRASS.id)  # Пол

# === Размещение золотых блоков под землёй ===
gold_blocks = []
used_coords = set()

while len(gold_blocks) < NUM_GOLD_BLOCKS:
    x = random.randint(base_x, base_x + ARENA_SIZE - 1)
    z = random.randint(base_z, base_z + ARENA_SIZE - 1)
    if (x, z) not in used_coords:
        used_coords.add((x, z))
        y = base_y - 2
        mc.setBlock(x, y, z, block.GOLD_BLOCK.id)
        gold_blocks.append((x, y, z))

# === Загрузка сохранённого счёта ===
if os.path.exists(SCORE_FILE):
    with open(SCORE_FILE, "r") as f:
        score = int(f.read())
else:
    score = 0

# === Загрузка найденных блоков ===
found_blocks = []
if os.path.exists(FOUND_FILE):
    with open(FOUND_FILE, "r") as f:
        for line in f:
            x, y, z = map(int, line.strip().split(","))
            found_blocks.append((x, y, z))

# === Старт игры ===
mc.postToChat("Арена готова! Найди все золотые блоки.")
mc.postToChat(f"Текущие очки: {score}")

while score < TOTAL_SCORE:
    pos = mc.player.getTilePos()
    block_below = mc.getBlock(pos.x, pos.y - 1, pos.z)
    check_pos = (pos.x, pos.y - 2, pos.z)  # Координаты блока под землёй

    if block_below == block.GRASS.id and check_pos in gold_blocks and check_pos not in found_blocks:
        found_blocks.append(check_pos)
        score += SCORE_PER_BLOCK
        mc.postToChat(f"Золото найдено! Очки: {score}")

        # Сохраняем очки
        with open(SCORE_FILE, "w") as f:
            f.write(str(score))

        # Сохраняем найденные блоки
        with open(FOUND_FILE, "w") as f:
            for x, y, z in found_blocks:
                f.write(f"{x},{y},{z}\n")

        time.sleep(1)

mc.postToChat("Ты победил! Все блоки найдены!")
