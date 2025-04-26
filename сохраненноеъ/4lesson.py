from mcpi.minecraft import Minecraft
import time
from mcpi import block
mc = Minecraft.create()


# x, y, z = mc.player.getTilePos()
# for dx in range(5):
#     for dy in range(5):
#         for dz in range(5):
#             if dx in [0, 4] or dy in [0, 4] or dz in [0, 4]:
#                 mc.setBlock(x + dx, y + dy, z + dz, block.GLASS)
# for i in range(10):
#     x, y, z = mc.player.getTilePos()
#     mc.setBlock(x, y - 1, z, block.LAVA)
#     mc.postToChat("🔥 Телепортация!")
#     mc.player.setTilePos(x + 5, y + 10, z + 5)
#     time.sleep(1)

#
#
# pos = mc.player.getTilePos()
# mc.postToChat(f"My position: {pos}")
#
# last_pos = mc.player.getTilePos()
# start_time = time.time()
# while time.time() - start_time < 10:  # Следим за движением 10 секунд
#     pos = mc.player.getTilePos()
#     if pos != last_pos:
#         mc.postToChat(f"new pos: {pos}")
#         last_pos = pos
#     time.sleep(0.000000000000000000001)
#
#
#
# from time import sleep
#
# x, y, z = mc.player.getTilePos()
# mc.postToChat("Jumping in 3 seconds...")
# sleep(3)
# mc.player.setTilePos(x, y + 10, z)


# Поставим деревянную дверь
x, y, z = mc.player.getTilePos()
# # mc.setBlock(x + 1, y, z, block.DOOR_IRON)
#
#
# # Ставим лампу
# lamp_x, lamp_y, lamp_z = x + 3, y, z
# mc.setBlock(lamp_x, lamp_y, lamp_z, block.GLOWSTONE_BLOCK.id)
#
# # Проверяем положение игрока
# while True:
#     pos = mc.player.getTilePos()
#     if pos.x == lamp_x and pos.z == lamp_z:
#         mc.postToChat("Lamp ON!")
#         break

mc = Minecraft.create()

# Координаты двери
# x, y, z = mc.player.getTilePos()
# door_x, door_y, door_z = x + 5, y, z
#
# # Поставим стенку (например, из камня)
# mc.setBlock(door_x, door_y, door_z, block.STONE.id)
#
# while True:
#     pos = mc.player.getTilePos()
#     if abs(pos.x - door_x) < 2 and abs(pos.z - door_z) < 2:
#         mc.setBlocks(door_x, door_y, door_z,door_x, door_y+1, door_z, block.AIR.id)  # Убираем стену
#         mc.postToChat("Door opened!")
#     else:
#         mc.setBlocks(door_x, door_y, door_z,door_x, door_y+1, door_z, block.STONE.id)  # Ставим стену обратно
#     time.sleep(0.5)

from mcpi.minecraft import Minecraft
from mcpi import block
import time

mc = Minecraft.create()

# Центр двери
x, y, z = mc.player.getTilePos()
door_x, door_y, door_z = x + 5, y, z

# Размер стены
width = 10
height = 10

# Ставим стену
for dx in range(width):
    for dy in range(height):
        mc.setBlock(door_x + dx, door_y + dy, door_z, block.STONE.id)

while True:
    pos = mc.player.getTilePos()
    if abs(pos.x - door_x) < 5 and abs(pos.z - door_z) < 5:
        # Убираем стену
        for dx in range(width):
            for dy in range(height):
                mc.setBlock(door_x + dx, door_y + dy, door_z, block.AIR.id)
        mc.postToChat("Big Door opened!")
    else:
        # Восстанавливаем стену
        for dx in range(width):
            for dy in range(height):
                mc.setBlock(door_x + dx, door_y + dy, door_z, block.STONE.id)
    time.sleep(0.5)

# Координаты TNT
x, y, z = mc.player.getTilePos()
tnt_x, tnt_y, tnt_z = x + 5, y, z

# Ставим TNT
mc.setBlock(tnt_x, tnt_y, tnt_z, block.TNT.id, 1)  # 1 — активированное TNT

while True:
    pos = mc.player.getTilePos()
    if abs(pos.x - tnt_x) < 2 and abs(pos.z - tnt_z) < 2:
        mc.postToChat("Boom!")
        mc.setBlock(tnt_x, tnt_y, tnt_z, block.AIR.id)  # удаляем TNT
        mc.setBlock(tnt_x, tnt_y, tnt_z, block.TNT.id, 1)  # снова активируем
        break
    time.sleep(0.5)


from mcpi.minecraft import Minecraft
from mcpi import block
import time

mc = Minecraft.create()

# Координаты лампы
x, y, z = mc.player.getTilePos()
lamp_x, lamp_y, lamp_z = x + 3, y, z

# Ставим блок земли на место лампы
mc.setBlock(lamp_x, lamp_y, lamp_z, block.DIRT.id)

while True:
    pos = mc.player.getTilePos()
    if abs(pos.x - lamp_x) < 2 and abs(pos.z - lamp_z) < 2:
        mc.setBlock(lamp_x, lamp_y, lamp_z, block.GLOWSTONE_BLOCK.id)  # Лампа загорается
        mc.postToChat("Light ON!")
    else:
        mc.setBlock(lamp_x, lamp_y, lamp_z, block.DIRT.id)  # Лампа выключается
    time.sleep(0.5)