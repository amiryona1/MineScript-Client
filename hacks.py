from system.pyj.minescript import *
import minescript
import inputs
import math
Minecraft = JavaClass("net.minecraft.client.Minecraft")
BlockPos = JavaClass(
    "net.minecraft.core.BlockPos"
)

Vec3 = JavaClass(
    "net.minecraft.world.phys.Vec3"
)

BlockHitResult = JavaClass(
    "net.minecraft.world.phys.BlockHitResult"
)

Direction = JavaClass(
    "net.minecraft.core.Direction"
)

InteractionHand = JavaClass(
    "net.minecraft.world.InteractionHand"
)

UseItemPacket = JavaClass(
    "net.minecraft.network.protocol.game.ServerboundUseItemOnPacket"
)

SwingPacket = JavaClass(
    "net.minecraft.network.protocol.game.ServerboundSwingPacket"
)
def aimbot():
    if not inputs.aimbot_enabled:
        return

    try:
        players = minescript.get_players()

        mx, my, mz = minescript.player_position()

        closest = None
        closest_distance = 9999

        for p in players:
            x, y, z = p.position

            distance = math.sqrt(
                (x - mx) ** 2 +
                (y - my) ** 2 +
                (z - mz) ** 2
            )

            if distance < 0.1:
                continue

            if distance < closest_distance and distance <= 4:
                closest_distance = distance
                closest = p

        if closest:
            x, y, z = closest.position

            minescript.player_look_at(x, y + 1.62, z)

    except Exception as e:
        minescript.echo(str(e))



flip_back_ticks = 0
old_yaw = 0


random_offset = 0

def hit_dir():
    if not inputs.hit_dir_enabled:
        return

    global flip_back_ticks
    global old_yaw
    global random_offset

    yaw, pitch = minescript.player_orientation()

    if flip_back_ticks > 0:

        flip_back_ticks -= 1

        if flip_back_ticks == 0:

            minescript.player_set_orientation(
                old_yaw,
                pitch
            )

        return

    if not mc.options.keyAttack.isDown():
        return

    entity = minescript.player_get_targeted_entity(4)

    if not entity:
        return

    old_yaw = yaw

    random_offset += 1

    offset = 11.3

    if random_offset % 2 == 0:
        offset += 1.7

    if random_offset % 3 == 0:
        offset -= 0.9

    if random_offset % 5 == 0:
        offset += 0.4

    minescript.player_set_orientation(
        yaw + offset,
        pitch
    )

    flip_back_ticks = 1

click_cooldown = 0
click_stage = 0


def auto_hit():
    global click_cooldown
    global click_stage

    if not inputs.auto_hit_enabled:
        return

    if click_cooldown > 0:
        click_cooldown -= 1
        return

    entity = minescript.player_get_targeted_entity(4)

    if not entity:
        return

    if entity.type != "entity.minecraft.player":
        return

    if inputs.hit_dir_enabled:
        hit_dir()
    minescript.player_press_attack(True)
    minescript.player_press_attack(False)

    click_stage += 1

    if click_stage % 13 == 0:
        click_cooldown = 6

    elif click_stage % 9 == 0:
        click_cooldown = 4

    elif click_stage % 5 == 0:
        click_cooldown = 3

    else:
        click_cooldown = 2


bridge_yaw = None
is_sneaking = False


RotPacket = JavaClass(
    "net.minecraft.network.protocol.game.ServerboundMovePlayerPacket$Rot"
)

mc = Minecraft.getInstance()

place_ticks = 0
sequence = 0




def scaffold():
    global bridge_yaw
    global is_sneaking

    if not inputs.scaffold_enabled:

        bridge_yaw = None
        is_sneaking = False

        return

    yaw, pitch = minescript.player_orientation()

    if bridge_yaw is None:
        bridge_yaw = round(yaw / 90) * 90

    minescript.player_set_orientation(
        yaw,
        80.5
    )

    px, py, pz = minescript.player_position()

    fx = px - int(px)
    fz = pz - int(pz)

    near_edge = False
    safe = False

    if bridge_yaw == 0:
        near_edge = fz < 0.12
        safe = fz > 0.30

    elif bridge_yaw == 180 or bridge_yaw == -180:
        near_edge = fz > 0.88
        safe = fz < 0.70

    elif bridge_yaw == 90:
        near_edge = fx < 0.12
        safe = fx > 0.30

    elif bridge_yaw == -90:
        near_edge = fx > 0.88
        safe = fx < 0.70


    is_sneaking = near_edge and not safe

    minescript.press_key_bind(
        "key.sneak",
        is_sneaking
    )

    if minescript.get_block(
        int(px),
        int(py - 1.01),
        int(pz)
    ) != "minecraft:air":
        return

    minescript.player_press_use(True)
    minescript.player_press_use(False)


assist_strength = 1.0
offset = 0

def aim_assist():
    global offset

    if not inputs.aim_assist_enabled:
        return

    offset += 1

    players = minescript.get_players()

    px, py, pz = minescript.player_position()

    closest = None
    closest_distance = 9999

    for p in players:
        x, y, z = p.position

        distance = (
                (x - px) * (x - px) +
                (y - py) * (y - py) +
                (z - pz) * (z - pz)
        )

        if distance < closest_distance and distance > 0.01 and distance <= 10:
            closest = p
            closest_distance = distance

    if not closest:
        return

    x, y, z = closest.position

    current_yaw, current_pitch = minescript.player_orientation()

    if offset % 2 == 0:
        x += 0.14
    elif offset % 3 == 0:
        x -= 0.11

    if offset % 5 == 0:
        y += 1.72
    elif offset % 7 == 0:
        y += 1.28
    else:
        y += 1.5

    minescript.player_look_at(x, y, z)

    target_yaw, target_pitch = minescript.player_orientation()

    minescript.player_set_orientation(current_yaw, current_pitch)

    yaw_diff = target_yaw - current_yaw

    if yaw_diff > 180:
        yaw_diff -= 360
    elif yaw_diff < -180:
        yaw_diff += 360

    pitch_diff = target_pitch - current_pitch

    if abs(yaw_diff) > 90:
        return

    if abs(yaw_diff) < 1.2:
        return

    strength = assist_strength

    if abs(yaw_diff) > 25:
        strength = 0.32

    elif abs(yaw_diff) > 10:
        strength = 0.24

    else:
        strength = 0.14

    yaw = current_yaw + yaw_diff * strength

    pitch = current_pitch

    if offset % 4 == 0:
        pitch += 0.7
    elif offset % 6 == 0:
        pitch -= 0.5
    elif offset % 9 == 0:
        pitch += 0.3

    if offset % 13 == 0:
        return

    minescript.player_set_orientation(yaw, pitch)
