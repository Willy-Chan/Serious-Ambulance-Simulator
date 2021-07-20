from enum import IntEnum, Enum

class Terrains(IntEnum):
    none = 0
    out_of_bounds = 1
    wall = 2
    floor = 3
    mud = 4
    fire = 5
    hospital = 6


class MapObjects(IntEnum):
    none = 0
    injured = 1
    pedestrian = 2
    zombie = 3
    battery = 4
    player = 5
    injured_rich = 6
    pedestrian_rich = 7
    injured_poor = 8
    pedestrian_poor = 9
    injured_young = 10
    pedestrian_young = 11
    injured_old = 12
    pedestrian_old = 13
    injured_female = 14
    pedestrian_female = 15
    injured_male = 16
    pedestrian_male = 17






class Actions(IntEnum):
    none = 0
    turn_left = 1
    turn_right = 2
    step_forward = 3


class Orientations(IntEnum):
    up = 0
    right = 1
    down = 2
    left = 3


class PlayTypes(IntEnum):
    human = 0
    machine = 1


class MapProfiles(IntEnum):
    uniform = 0
    trolley = 1
    sparse = 2
    pacman = 3
    spoiled = 4
    twisty = 5
    volcano = 6
    custom = 7

class Scores(IntEnum):
    RESCUE_REWARD = 15  # +9 per rescued victim (picked up one by one and delivered to hospital)
    PED_PENALTY = -5  # -10 per squished pedestrian (or mobile pedestrian)
    VIC_PENALTY = -1  # -1 per squished victim (if you already have one onboard and enter it’s space, SQUISH)
    FIRE_PENALTY = -1  # -5 per entry into fire (each entry; but otherwise it doesn’t actually hurt you)
    ZOMBIE_REWARD = 2  # +2 per squished zombie (ZOMBIE DEATH!)
    PICKUP_REWARD = 10  # picked up person FINALLY
    MOVING_FORWARD = 1  # wow they didn't just spin

class MapColors(Enum):
    play_area = '#000000'
    game_screen = '#6665adff'
    black_tile = '#000000'
    wall_tile = '#4b4b51ff'
    floor_tile = '#86868cff'
    mud_tile = '#723415ff'
    fire_tile = '#bd4713ff'
    hospital_tile = '#8c2e3aff'
    text = '#ffffff'