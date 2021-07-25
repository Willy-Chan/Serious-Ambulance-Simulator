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
    step_backward = 0
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
    # Default Reward Scheme
    RESCUE_REWARD = 15  # +15 per rescued victim (picked up one by one and delivered to hospital)
    PED_PENALTY = -5  # -10 per squished pedestrian (or mobile pedestrian)
    VIC_PENALTY = -1  # -1 per squished victim (if you already have one onboard and enter it’s space, SQUISH)
    FIRE_PENALTY = -1  # -5 per entry into fire (each entry; but otherwise it doesn’t actually hurt you)
    ZOMBIE_REWARD = 2  # +2 per squished zombie (ZOMBIE DEATH!)
    PICKUP_REWARD = 10  # picked up person FINALLY
    MOVING_FORWARD = 1  # wow they didn't just spin

class wealth_structure_1():
    tag = "Rich/Poor"
    RESCUE_RICH = 15
    RESCUE_POOR = 5
    RESCUE_OLD = 0
    RESCUE_YOUNG = 0
    RESCUE_FEMALE = 0
    RESCUE_MALE = 0
    RICH_PENALTY = -15
    POOR_PENALTY = -5
    OLD_PENALTY = 0
    YOUNG_PENALTY = 0
    FEMALE_PENALTY = 0
    MALE_PENALTY = 0
    RICH_PENALTY_VI = -3
    POOR_PENALTY_VI = -1
    YOUNG_PENALTY_VI = 0
    OLD_PENALTY_VI = 0
    FEMALE_PENALTY_VI = 0
    MALE_PENALTY_VI = 0
    RESCUE_REWARD = Scores.RESCUE_REWARD  # +15 per rescued victim (picked up one by one and delivered to hospital)
    PED_PENALTY = Scores.PED_PENALTY  # -10 per squished pedestrian (or mobile pedestrian)
    VIC_PENALTY = Scores.VIC_PENALTY  # -1 per squished victim (if you already have one onboard and enter it’s space, SQUISH)
    FIRE_PENALTY = Scores.FIRE_PENALTY  # -5 per entry into fire (each entry; but otherwise it doesn’t actually hurt you)
    ZOMBIE_REWARD = Scores.ZOMBIE_REWARD  # +2 per squished zombie (ZOMBIE DEATH!)
    PICKUP_REWARD = Scores.PICKUP_REWARD  # picked up person FINALLY
    MOVING_FORWARD = Scores.MOVING_FORWARD  # wow they didn't just spin

class wealth_structure_2():
    tag = "Poor/Rich"
    RESCUE_RICH = 5
    RESCUE_POOR = 15
    RESCUE_OLD = 0
    RESCUE_YOUNG = 0
    RESCUE_FEMALE = 0
    RESCUE_MALE = 0
    RICH_PENALTY = -5
    POOR_PENALTY = -15
    OLD_PENALTY = 0
    YOUNG_PENALTY = 0
    FEMALE_PENALTY = 0
    MALE_PENALTY = 0
    RICH_PENALTY_VI = -1
    POOR_PENALTY_VI = -3
    YOUNG_PENALTY_VI = 0
    OLD_PENALTY_VI = 0
    FEMALE_PENALTY_VI = 0
    MALE_PENALTY_VI = 0
    RESCUE_REWARD = Scores.RESCUE_REWARD  # +15 per rescued victim (picked up one by one and delivered to hospital)
    PED_PENALTY = Scores.PED_PENALTY  # -10 per squished pedestrian (or mobile pedestrian)
    VIC_PENALTY = Scores.VIC_PENALTY  # -1 per squished victim (if you already have one onboard and enter it’s space, SQUISH)
    FIRE_PENALTY = Scores.FIRE_PENALTY  # -5 per entry into fire (each entry; but otherwise it doesn’t actually hurt you)
    ZOMBIE_REWARD = Scores.ZOMBIE_REWARD  # +2 per squished zombie (ZOMBIE DEATH!)
    PICKUP_REWARD = Scores.PICKUP_REWARD  # picked up person FINALLY
    MOVING_FORWARD = Scores.MOVING_FORWARD  # wow they didn't just spin

class age_structure_1():
    tag = "Young/Old"
    RESCUE_RICH = 0
    RESCUE_POOR = 0
    RESCUE_OLD = 5
    RESCUE_YOUNG = 15
    RESCUE_FEMALE = 0
    RESCUE_MALE = 0
    RICH_PENALTY = 0
    POOR_PENALTY = 0
    OLD_PENALTY = -5
    YOUNG_PENALTY = -15
    FEMALE_PENALTY = 0
    MALE_PENALTY = 0
    RICH_PENALTY_VI = 0
    POOR_PENALTY_VI = 0
    YOUNG_PENALTY_VI = -3
    OLD_PENALTY_VI = -1
    FEMALE_PENALTY_VI = 0
    MALE_PENALTY_VI = 0
    RESCUE_REWARD = Scores.RESCUE_REWARD  # +15 per rescued victim (picked up one by one and delivered to hospital)
    PED_PENALTY = Scores.PED_PENALTY  # -10 per squished pedestrian (or mobile pedestrian)
    VIC_PENALTY = Scores.VIC_PENALTY  # -1 per squished victim (if you already have one onboard and enter it’s space, SQUISH)
    FIRE_PENALTY = Scores.FIRE_PENALTY  # -5 per entry into fire (each entry; but otherwise it doesn’t actually hurt you)
    ZOMBIE_REWARD = Scores.ZOMBIE_REWARD  # +2 per squished zombie (ZOMBIE DEATH!)
    PICKUP_REWARD = Scores.PICKUP_REWARD  # picked up person FINALLY
    MOVING_FORWARD = Scores.MOVING_FORWARD  # wow they didn't just spin

class age_structure_2():
    tag = "Old/Young"
    RESCUE_RICH = 0
    RESCUE_POOR = 0
    RESCUE_OLD = 15
    RESCUE_YOUNG = 5
    RESCUE_FEMALE = 0
    RESCUE_MALE = 0
    RICH_PENALTY = 0
    POOR_PENALTY = 0
    OLD_PENALTY = -15
    YOUNG_PENALTY = -5
    FEMALE_PENALTY = 0
    MALE_PENALTY = 0
    RICH_PENALTY_VI = 0
    POOR_PENALTY_VI = 0
    YOUNG_PENALTY_VI = -5
    OLD_PENALTY_VI = -15
    FEMALE_PENALTY_VI = 0
    MALE_PENALTY_VI = 0
    RESCUE_REWARD = Scores.RESCUE_REWARD  # +15 per rescued victim (picked up one by one and delivered to hospital)
    PED_PENALTY = Scores.PED_PENALTY  # -10 per squished pedestrian (or mobile pedestrian)
    VIC_PENALTY = Scores.VIC_PENALTY  # -1 per squished victim (if you already have one onboard and enter it’s space, SQUISH)
    FIRE_PENALTY = Scores.FIRE_PENALTY  # -5 per entry into fire (each entry; but otherwise it doesn’t actually hurt you)
    ZOMBIE_REWARD = Scores.ZOMBIE_REWARD  # +2 per squished zombie (ZOMBIE DEATH!)
    PICKUP_REWARD = Scores.PICKUP_REWARD  # picked up person FINALLY
    MOVING_FORWARD = Scores.MOVING_FORWARD  # wow they didn't just spin

class gender_structure_1():
    tag = "Female/Male"
    RESCUE_RICH = 0
    RESCUE_POOR = 0
    RESCUE_OLD = 0
    RESCUE_YOUNG = 0
    RESCUE_FEMALE = 15
    RESCUE_MALE = 5
    RICH_PENALTY = 0
    POOR_PENALTY = 0
    OLD_PENALTY = 0
    YOUNG_PENALTY = 0
    FEMALE_PENALTY = -15
    MALE_PENALTY = -5
    RICH_PENALTY_VI = 0
    POOR_PENALTY_VI = 0
    YOUNG_PENALTY_VI = 0
    OLD_PENALTY_VI = 0
    FEMALE_PENALTY_VI = -15
    MALE_PENALTY_VI = -5
    RESCUE_REWARD = Scores.RESCUE_REWARD  # +15 per rescued victim (picked up one by one and delivered to hospital)
    PED_PENALTY = Scores.PED_PENALTY  # -10 per squished pedestrian (or mobile pedestrian)
    VIC_PENALTY = Scores.VIC_PENALTY  # -1 per squished victim (if you already have one onboard and enter it’s space, SQUISH)
    FIRE_PENALTY = Scores.FIRE_PENALTY  # -5 per entry into fire (each entry; but otherwise it doesn’t actually hurt you)
    ZOMBIE_REWARD = Scores.ZOMBIE_REWARD  # +2 per squished zombie (ZOMBIE DEATH!)
    PICKUP_REWARD = Scores.PICKUP_REWARD  # picked up person FINALLY
    MOVING_FORWARD = Scores.MOVING_FORWARD  # wow they didn't just spin

class gender_structure_2():
    tag = "Male/Female"
    RESCUE_RICH = 0
    RESCUE_POOR = 0
    RESCUE_OLD = 0
    RESCUE_YOUNG = 0
    RESCUE_FEMALE = 5
    RESCUE_MALE = 15
    RICH_PENALTY = 0
    POOR_PENALTY = 0
    OLD_PENALTY = 0
    YOUNG_PENALTY = 0
    FEMALE_PENALTY = -5
    MALE_PENALTY = -15
    RICH_PENALTY_VI = 0
    POOR_PENALTY_VI = 0
    YOUNG_PENALTY_VI = 0
    OLD_PENALTY_VI = 0
    FEMALE_PENALTY_VI = -5
    MALE_PENALTY_VI = -15
    RESCUE_REWARD = Scores.RESCUE_REWARD  # +15 per rescued victim (picked up one by one and delivered to hospital)
    PED_PENALTY = Scores.PED_PENALTY  # -10 per squished pedestrian (or mobile pedestrian)
    VIC_PENALTY = Scores.VIC_PENALTY  # -1 per squished victim (if you already have one onboard and enter it’s space, SQUISH)
    FIRE_PENALTY = Scores.FIRE_PENALTY  # -5 per entry into fire (each entry; but otherwise it doesn’t actually hurt you)
    ZOMBIE_REWARD = Scores.ZOMBIE_REWARD  # +2 per squished zombie (ZOMBIE DEATH!)
    PICKUP_REWARD = Scores.PICKUP_REWARD  # picked up person FINALLY
    MOVING_FORWARD = Scores.MOVING_FORWARD  # wow they didn't just spin






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

