from mcpi.minecraft import Minecraft
from mcpi import block
import random

mc = Minecraft.create()
mc.player.setTilePos(0, 10, 0)

# Очищаем территорию
for x in range(-10, 10):
    for y in range(0, 5):
        for z in range(-10, 10):
            mc.setBlock(x, y, z, block.AIR)

# Строим платформу
for x in range(-10, 10):
    for z in range(-10, 10):
        mc.setBlock(x, 0, z, block.GRASS)

items = []

for i in range(20):
    x = random.randint(-8, 8)
    z = random.randint(-8, 8)
    y = 1
    mc.setBlock(x, y, z, block.DIAMOND_BLOCK)
    items.append((x, y, z))


import time

collected = 0
start_time = time.time()

while time.time() - start_time < 60:
    pos = mc.player.getTilePos()
    for item in items:
        if abs(pos.x - item[0]) <= 1 and abs(pos.z - item[2]) <= 1:
            mc.setBlock(item[0], item[1], item[2], block.AIR)
            collected += 1
            mc.postToChat("Собрано: " + str(collected))
            items.remove(item)
            break
    time.sleep(0.5)

mc.postToChat("Игра окончена! Собрано предметов: " + str(collected))
