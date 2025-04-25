from mcpi.minecraft import Minecraft
from mcpi import block
import time
import random

mc = Minecraft.create()

# Центр арены
x, y, z = mc.player.getTilePos()
arena_size = 1000
height = y - 3

mc.postToChat(" WELCOME TO THE LAVA CHALLENGE ")

# Цветные блоки для эффекта диско
colors = [block.WOOL.id + i for i in range(10)]

# Создание арены
for dx in range(arena_size):
    for dz in range(arena_size):
        color = random.choice(colors)
        mc.setBlock(x + dx, height, z + dz, color)

# Список безопасных блоков
safe_blocks = [(x + dx, z + dz) for dx in range(arena_size) for dz in range(arena_size)]

start_time = time.time()

while safe_blocks:
    time.sleep(0.000000000000001)  # быстро!

    # Выбор случайного блока
    bx, bz = random.choice(safe_blocks)

    # Мигающий эффект
    for _ in range(3):
        mc.setBlock(bx, height, bz, block.GLOWSTONE_BLOCK)
        time.sleep(0.01)
        mc.setBlock(bx, height, bz, block.OBSIDIAN)
        time.sleep(0.01)

    # Превращение в лаву
    mc.setBlock(bx, height, bz, block.LAVA)
    safe_blocks.remove((bx, bz))

    # Проверка падения игрока
    px, py, pz = mc.player.getTilePos()
    if py < height:
        mc.postToChat(" GAME OVER! ")
        break

    # Счётчик времени выживания
    elapsed = round(time.time() - start_time, 1)
    mc.postToChat(f"⏱ Time: {elapsed} seconds")

else:
    mc.postToChat(" YOU SURVIVED! LEGEND!")
    # Награда
    mc.setBlock(x + arena_size//2, y, z + arena_size//2, block.DIAMOND_BLOCK)
    mc.setBlock(x + arena_size//2, y+1, z + arena_size//2, block.TORCH)