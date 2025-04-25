
# Урок 2: Взаимодействие с Minecraft через Python
# Практические задания и мини-проект

from mcpi.minecraft import Minecraft
from mcpi import block
import time

mc = Minecraft.create()

# 1. Приветствие
mc.postToChat("Привет, Minecraft!")

# 2. Получение координат игрока
x, y, z = mc.player.getTilePos()
mc.postToChat(f"Ты находишься на координатах: {x}, {y}, {z}")

# 3. Установка блока под игроком
mc.setBlock(x, y - 1, z, block.GOLD_BLOCK)

# 4. Телепортация игрока
mc.player.setTilePos(x + 10, y + 5, z + 10)

# 5. Строим башню
x, y, z = mc.player.getTilePos()
for i in range(10):
    mc.setBlock(x, y + i, z, block.BRICK_BLOCK)

# 6. Строим "портал" из обсидиана
for dx in range(5):
    for dy in range(5):
        mc.setBlock(x + dx, y + dy, z, block.OBSIDIAN)

# 7. Строим пустой стеклянный куб 5x5x5
for dx in range(5):
    for dy in range(5):
        for dz in range(5):
            if dx in [0, 4] or dy in [0, 4] or dz in [0, 4]:
                mc.setBlock(x + dx, y + dy, z + dz, block.GLASS)

# 8. Сообщение при движении игрока
last_pos = mc.player.getTilePos()
start_time = time.time()
while time.time() - start_time < 10:  # Следим за движением 10 секунд
    pos = mc.player.getTilePos()
    if pos != last_pos:
        mc.postToChat(f"Ты шагнул! Новые координаты: {pos}")
        last_pos = pos
    time.sleep(0.2)

# 9. Финальный проект: Телепортационные прыжки с огненным следом
for i in range(10):
    x, y, z = mc.player.getTilePos()
    mc.setBlock(x, y - 1, z, block.LAVA)
    mc.postToChat("🔥 Телепортация!")
    mc.player.setTilePos(x + 5, y + 10, z + 5)
    time.sleep(1)
