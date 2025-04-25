from mcpi.minecraft import Minecraft
from mcpi import block
import math
import random
import time

mc = Minecraft.create()
x, y, z = mc.player.getTilePos()
mc.postToChat("🎯 Fly through the scattered RINGS!")

# Параметры
num_rings = 100
ring_radius = 8
ring_blocks = [
    block.GOLD_BLOCK.id,
    block.DIAMOND_BLOCK.id,
    block.LAPIS_LAZULI_BLOCK.id,
    block.IRON_BLOCK.id
]

def create_ring(cx, cy, cz, radius, facing='z', block_id=block.GOLD_BLOCK.id):
    for angle in range(0, 360, 6):
        rad = math.radians(angle)
        dx = int(radius * math.cos(rad))
        dy = int(radius * math.sin(rad))

        if facing == 'z':
            mc.setBlock(cx + dx, cy + dy, cz, block_id)
        elif facing == 'x':
            mc.setBlock(cx, cy + dy, cz + dx, block_id)

# Стартовая платформа
mc.setBlock(x, y, z, block.GLOWSTONE_BLOCK)
mc.player.setTilePos(x, y + 50, z)

# Генерация колец в разброс
for i in range(num_rings):
    offset_x = random.randint(-80, 80)
    offset_y = random.randint(40, 100)
    offset_z = random.randint(30, 160)

    ring_x = x + offset_x
    ring_y = y + offset_y
    ring_z = z + offset_z
    ring_dir = random.choice(['x', 'z'])
    ring_block = random.choice(ring_blocks)

    create_ring(ring_x, ring_y, ring_z, ring_radius, facing=ring_dir, block_id=ring_block)

mc.postToChat("🪂 Wings on! Fly through the scattered rings!")
