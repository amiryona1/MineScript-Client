from minescript import *

aimbot_enabled = False
auto_hit_enabled = False
scaffold_enabled = False
hit_dir_enabled = False
aim_assist_enabled = False


def on_key(event):
    global aimbot_enabled
    global auto_hit_enabled
    global scaffold_enabled
    global hit_dir_enabled
    global aim_assist_enabled

    # ignore typing in chat/gui
    if screen_name() is not None:
        return

    if event.action != 0:
        return

    if event.key == 71:
        aimbot_enabled = not aimbot_enabled
        echo("aimbot: " + str(aimbot_enabled))

    elif event.key == 86:
        auto_hit_enabled = not auto_hit_enabled
        echo("auto hit: " + str(auto_hit_enabled))

    elif event.key == 67:
        scaffold_enabled = not scaffold_enabled
        echo("Scafold: " + str(scaffold_enabled))

    elif event.key == 66:
        hit_dir_enabled = not hit_dir_enabled
        echo("Hit Dir: " + str(hit_dir_enabled))
    elif event.key == 82:
        aim_assist_enabled = not aim_assist_enabled
        echo("Aim Assist: " + str(aim_assist_enabled))


def init():
    add_event_listener("key", on_key)