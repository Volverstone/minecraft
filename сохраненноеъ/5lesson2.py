from mcpi.minecraft import Minecraft

mc = Minecraft.create()
pos = mc.player.getTilePos()

# Вручную вызываем команду через соединение
mc.conn.send(f'runCommand summon minecraft:cow {pos.x + 1} {pos.y} {pos.z}')

mc.postToChat("Коровка появилась рядом 🐄")
