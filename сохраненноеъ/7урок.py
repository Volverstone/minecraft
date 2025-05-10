from mcpi.minecraft import Minecraft
from mcpi import block
import time

mc = Minecraft.create()

###########REACTION OF BLOCK###############
mc.postToChat("Ударь по блоку, чтобы получить сюрприз!")

while True:
    hits = mc.events.pollBlockHits()
    for hit in hits:
        pos = hit.pos
        mc.postToChat("Ты ударил блок на " + str(pos))
        mc.setBlock(pos.x, pos.y + 1, pos.z, block.GOLD_BLOCK)
    time.sleep(0.1)
import time

teleport_pos = mc.player.getTilePos()
mc.setBlock(teleport_pos.x + 1, teleport_pos.y, teleport_pos.z, block.DIAMOND_BLOCK)

mc.postToChat("Встань на алмазный блок для телепортации!")

while True:
    pos = mc.player.getTilePos()
    block_below = mc.getBlock(pos.x, pos.y - 1, pos.z)
    if block_below == block.DIAMOND_BLOCK.id:
        mc.postToChat("Телепорт!")
        mc.player.setTilePos(teleport_pos.x, teleport_pos.y + 10, teleport_pos.z)
        time.sleep(1)
    time.sleep(0.1)


#######################OPEN THE DOOR#####################

secret_x, secret_y, secret_z = mc.player.getTilePos()
mc.setBlock(secret_x, secret_y, secret_z, block.WOOD)
mc.postToChat("Ударь по деревянному блоку, чтобы открыть дверь!")

door_open = False

while True:
    hits = mc.events.pollBlockHits()
    for hit in hits:
        if hit.pos.x == secret_x and hit.pos.y == secret_y and hit.pos.z == secret_z:
            if not door_open:
                mc.setBlock(secret_x + 1, secret_y, secret_z, block.AIR)
                mc.postToChat("Дверь открыта!")
                door_open = True
            else:
                mc.setBlock(secret_x + 1, secret_y, secret_z, block.STONE)
                mc.postToChat("Дверь закрыта!")
                door_open = False
    time.sleep(0.1)
###############TELEPOT##########################


import time

teleport_pos = mc.player.getTilePos()
mc.setBlock(teleport_pos.x + 1, teleport_pos.y, teleport_pos.z, block.DIAMOND_BLOCK)

mc.postToChat("Встань на алмазный блок для телепортации!")

while True:
    pos = mc.player.getTilePos()
    block_below = mc.getBlock(pos.x, pos.y - 1, pos.z)
    if block_below == block.DIAMOND_BLOCK.id:
        mc.postToChat("Телепорт!")
        mc.player.setTilePos(teleport_pos.x, teleport_pos.y + 10, teleport_pos.z)
        time.sleep(1)
    time.sleep(0.1)




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

mc = Minecraft.create()

# === Получение позиции игрока ===
player_pos = mc.player.getTilePos()
base_x = player_pos.x
base_y = GROUND_Y
base_z = player_pos.z

# === Постройка арены ===
mc.setBlocks(base_x - 1, base_y, base_z - 1,
             base_x + ARENA_SIZE, base_y + 5, base_z + ARENA_SIZE,
             block.AIR.id)

mc.setBlocks(base_x, base_y - 1, base_z,
             base_x + ARENA_SIZE - 1, base_y - 1, base_z + ARENA_SIZE - 1,
             block.GRASS.id)

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

# === Дверь рядом со стартовой точкой ===
secret_x = base_x - 2
secret_y = base_y
secret_z = base_z
mc.setBlock(secret_x, secret_y, secret_z, block.STONE)  # "дверь"
door_open = False

# === Загрузка найденных блоков ===
found_blocks = []
if os.path.exists(FOUND_FILE):
    with open(FOUND_FILE, "r") as f:
        for line in f:
            x, y, z = map(int, line.strip().split(","))
            found_blocks.append((x, y, z))

mc.postToChat("Арена готова! Найди и ударь золотые блоки!")

# === Главный игровой цикл ===
while score < TOTAL_SCORE:
    pos = mc.player.getTilePos()

    # Проверка блока под ногами
    check_pos = (pos.x, pos.y - 2, pos.z)
    block_below = mc.getBlock(pos.x, pos.y - 1, pos.z)

    # Если найден новый блок
    if block_below == block.GRASS.id and check_pos in gold_blocks and check_pos not in found_blocks:
        found_blocks.append(check_pos)
        score += SCORE_PER_BLOCK
        mc.postToChat(f"Золото найдено! Очки: {score}")

        with open(SCORE_FILE, "w") as f:
            f.write(str(score))

        with open(FOUND_FILE, "w") as f:
            for x, y, z in found_blocks:
                f.write(f"{x},{y},{z}\n")

        time.sleep(1)










    # === Обработка ударов ===
    hits = mc.events.pollBlockHits()
    for hit in hits:
        hit_pos = (hit.pos.x, hit.pos.y, hit.pos.z)

        if hit_pos in found_blocks:
            # Удар по найденному золотому блоку
            if not door_open:
                mc.setBlock(secret_x, secret_y, secret_z, block.AIR)
                mc.postToChat("Дверь открыта!")
                door_open = True
            else:
                mc.setBlock(secret_x, secret_y, secret_z, block.STONE)
                mc.postToChat("Дверь закрыта!")
                door_open = False

    time.sleep(0.1)

mc.postToChat("Ты победил! Все блоки найдены!")
