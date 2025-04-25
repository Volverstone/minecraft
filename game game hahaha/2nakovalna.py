from mcpi.minecraft import Minecraft
from mcpi import block
import time
import random

mc = Minecraft.create()

x, y, z = mc.player.getTilePos()
size = 50
mc.postToChat("DODGE THE ANVILS!")

# Пол из цветного бетона
colors = [251 + i * 256 for i in range(16)]  # Цветной бетон
for dx in range(size):
    for dz in range(size):
        color = random.choice(colors)
        mc.setBlock(x + dx, y - 1, z + dz, color)

start_time = time.time()
duration = 100  # секунд

def drop_anvil(bx, bz):
    height = 15
    for i in range(height, 0, -1):
        mc.setBlock(bx, y + i, bz, 145)  # наковальня
        time.sleep(0.0001)
        if i != 1:
            mc.setBlock(bx, y + i, bz, block.AIR)
    # В конце — наковальня остаётся лежать на земле

while time.time() - start_time < duration:
    time.sleep(0.3)
    bx = x + random.randint(0, size - 1)
    bz = z + random.randint(0, size - 1)

    # Визуальное предупреждение
    mc.setBlock(bx, y + 1, bz, block.GLASS)
    time.sleep(0.3)
    mc.setBlock(bx, y + 1, bz, block.AIR)

    drop_anvil(bx, bz)

    # Проверка попадания по игроку
    px, py, pz = mc.player.getTilePos()
    if abs(px - bx) <= 1 and abs(pz - bz) <= 1 and py == y:
        mc.postToChat("☠ You got HIT by the anvil!")
        break

    mc.postToChat(f"Time: {round(time.time() - start_time, 1)}s")

else:
    mc.postToChat(" You survived the ANVIL STORM!")
    mc.setBlock(x + size // 2, y, z + size // 2, block.DIAMOND_BLOCK)
