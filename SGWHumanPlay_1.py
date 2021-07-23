import json
import uuid
import gym
import gym_sgw  # Required, don't remove!
import pygame as pg
from gym_sgw.envs.enums.Enums import Actions, Terrains, PlayTypes, MapProfiles, MapColors, \
    wealth_structure_1, wealth_structure_2, age_structure_1, age_structure_2, gender_structure_1, gender_structure_2
from gym_sgw.envs.model.Grid import Grid
import random
####





class SGW:
    """
    Human play game variant.
    """
    # "Constructor"
    def __init__(self, data_log_file='data_log.json', max_energy=50, map_file=None,
                 rand_prof=MapProfiles.trolley, num_rows=25, num_cols=25):
        self.ENV_NAME = 'SGW-v0'
        self.DATA_LOG_FILE_NAME = data_log_file
        self.GAME_ID = uuid.uuid4()
        self.env = None
        self.current_action = Actions.none
        self.max_energy = max_energy
        self.map_file = map_file
        self.rand_prof = rand_prof  # generates a RANDOM of this type, IF no map-file specified
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.is_game_over = False
        self.turn = 0
        self.max_turn = 300  # to prevent endless loops and games
        self.cell_size = 30
        self.game_screen = None
        self.play_area = None
        self.reward = "0"
        self.myfont = None

        # Always do these actions upon start
        self._setup()

    def _setup(self):
        # Game parameters - changing all of the settings in the environment
        self.env = gym.make(self.ENV_NAME)
        self.env.play_type = PlayTypes.human  # We will get human states and observations back
        self.env.render_mode = PlayTypes.machine  # We'll draw these manually
        self.env.max_energy = self.max_energy
        self.env.map_file = self.map_file
        self.env.rand_profile = self.rand_prof
        self.env.num_rows = self.num_rows
        self.env.num_cols = self.num_cols
        self.env.reset()

        # Report success
        print('Created new environment {0} with GameID: {1}'.format(self.ENV_NAME, self.GAME_ID))

    def done(self):
        print("Episode finished after {} turns.".format(self.turn))
        pg.quit()
        self._cleanup()

    def _cleanup(self):
        self.env.close()


# Generate a bunch of unchanging dice
# for i in range(1, 13):
#     exec("dice" + str(i) + "=None")
    global dice1
    dice1 = random.randint(1, 4)
    global dice2
    dice2 = random.randint(1, 4)
    global dice3
    dice3 = random.randint(1, 4)
    global dice4
    dice4 = random.randint(1, 4)
    global dice5
    dice5 = random.randint(1, 4)
    global dice6
    dice6 = random.randint(1, 4)
    global dice7
    dice7 = random.randint(1, 4)
    global dice8
    dice8 = random.randint(1, 4)
    global dice9
    dice9 = random.randint(1, 4)
    global dice10
    dice10 = random.randint(1, 4)
    global dice11
    dice11 = random.randint(1, 4)
    global dice12
    dice12 = random.randint(1, 4)
    global dice13
    dice13 = random.randint(1, 4)



    def _draw_screen(self):
        # Update the screen with the new observation, use the grid object directly
        # Populate each cell




        for r_ in range(self.env.grid.rows):
            for c_ in range(self.env.grid.cols):
                cell = self.env.grid.grid[r_][c_]

                if cell.terrain == Terrains.none:
                    # Tile = pg.transform.scale(pg.image.load('Images/none.png').convert(), (32, 32))
                    Tile = pg.image.load('Images/none.png').convert_alpha()
                elif cell.terrain == Terrains.out_of_bounds:
                    cell_color = pg.color.Color(MapColors.black_tile.value)
                    Tile = pg.image.load('Images/none.png').convert_alpha()
                elif cell.terrain == Terrains.wall:
                    cell_color = pg.color.Color(MapColors.wall_tile.value)
                    Tile = pg.image.load('Images/Tiles/iso_wall.png').convert_alpha()   #convert_alpha is what makes the transparency work
                elif cell.terrain == Terrains.floor:
                    cell_color = pg.color.Color(MapColors.floor_tile.value)
                    Tile = pg.image.load('Images/Tiles/iso_floor.png').convert_alpha()
                elif cell.terrain == Terrains.mud:
                    cell_color = pg.color.Color(MapColors.mud_tile.value)
                    Tile = pg.image.load('Images/Tiles/iso_mud.png').convert_alpha()
                elif cell.terrain == Terrains.fire:
                    cell_color = pg.color.Color(MapColors.fire_tile.value)
                    Tile = pg.image.load('Images/Tiles/iso_lava.png').convert_alpha()
                elif cell.terrain == Terrains.hospital:
                    cell_color = pg.color.Color(MapColors.hospital_tile.value)
                    Tile = None
                    Tile_hos = pg.image.load('Images/Tiles/iso_hos.png').convert_alpha()
                else:
                    raise ValueError('Invalid cell terrain while rendering game image.')

                # Render Tiles
                # x = c_ * self.cell_size
                # y = r_ * self.cell_size


                if Tile:
                    self.game_screen.blit(Tile, (700 + r_*51 - c_*51, 100 + r_ * 24 + c_ * 24))     #wonky offsets are what cause the isometric effect
                elif Tile_hos:
                    self.game_screen.blit(Tile_hos, (700 + r_ * 51 - c_ * 51, 70 + r_ * 24 + c_ * 24))
                else:
                    raise ValueError('fix your tile rendering, you bum.')





                # Draw the rectangle with the right color for the terrains
                # rect is play area, color, and (left point, top point, width, height)
                # DEBUG ISOMETRY
                pg.draw.rect(self.play_area, cell_color, (c_ * self.cell_size, r_ * self.cell_size,
                                                          self.cell_size, self.cell_size))
                self.game_screen.blit(self.play_area, self.play_area.get_rect())


                # Add in the cell value string
                pg.font.init()
                cell_font = pg.font.SysFont(pg.font.get_default_font(), 20)
                cell_val = self.env.grid.get_human_cell_value(r_, c_)
                self.myfont = pg.font.SysFont('Comic Sans MS', 30)
                # cell_val = '{},{}'.format(r_, c_)

                player = None
                agent = None
                att = None

                UI_Helper = pg.image.load('Images/UI/Helper.png').convert_alpha()
                self.game_screen.blit(UI_Helper, (750, 600))


                pop1, pop2 = 51, 51
                alpha, beta = 48, 90



                if cell_val == '^':
                    player = pg.transform.scale(pg.image.load('Images/player_default/iso_up.png').convert_alpha(), (pop1, pop2))
                    #self.game_screen.blit(player, (c_ * self.cell_size, r_ * self.cell_size))
                elif cell_val == 'v':
                    player = pg.transform.scale(pg.image.load('Images/player_default/iso_down.png').convert_alpha(), (pop1, pop2))
                    #self.game_screen.blit(player, (c_ * self.cell_size, r_ * self.cell_size))
                elif cell_val == '<':
                    player = pg.transform.scale(pg.image.load('Images/player_default/iso_left.png').convert_alpha(), (pop2, pop1))
                    #self.game_screen.blit(player, (c_ * self.cell_size, r_ * self.cell_size))
                elif cell_val == '>':
                    player = pg.transform.scale(pg.image.load('Images/player_default/iso_right.png').convert_alpha(), (pop2, pop1))
                    #self.game_screen.blit(player, (c_ * self.cell_size, r_ * self.cell_size))

                elif cell_val == 'Z':
                    agent = pg.transform.scale(pg.image.load('Images/agents/Zombie1.png').convert_alpha(), (pop2//2, pop1))
                elif cell_val == 'B':
                    agent = pg.transform.scale(pg.image.load('Images/agents/battery.png').convert_alpha(), (pop2, pop1))
                elif cell_val == 'I':
                    agent = pg.transform.scale(pg.image.load('Images/agents/Injury_default.png').convert_alpha(), (pop2, pop1))
                elif cell_val == 'P':
                    agent = pg.transform.scale(pg.image.load('Images/agents/Pedestrian.png').convert_alpha(), (pop2, pop1))
                elif cell_val == 'IR':
                    if dice1 == 1:
                        att = pg.transform.scale(
                            pg.image.load('Images/agents/injured/Rich_old_male_injured.png').convert_alpha(),
                            (alpha, beta))
                    elif dice1 == 2:
                        att = pg.transform.scale(
                            pg.image.load('Images/agents/injured/Rich_old_female_injured.png').convert_alpha(),
                            (alpha, beta))
                    elif dice1 == 3:
                        att = pg.transform.scale(
                            pg.image.load('Images/agents/injured/Rich_young_female_injured.png').convert_alpha(),
                            (alpha, beta))
                    elif dice1 == 4:
                        att = pg.transform.scale(
                            pg.image.load('Images/agents/injured/Rich_young_female_injured.png').convert_alpha(),
                            (alpha, beta))
                elif cell_val == 'PR':
                    if dice2 == 1:
                        att = pg.transform.scale(pg.image.load('Images/agents/pedestrian/Rich_old_male_pedestrian.png').convert_alpha(), (alpha, beta))
                    elif dice2 == 2:
                        att = pg.transform.scale(pg.image.load('Images/agents/pedestrian/Rich_old_female_pedestrian.png').convert_alpha(), (alpha, beta))
                    elif dice2 == 3:
                        att = pg.transform.scale(pg.image.load('Images/agents/pedestrian/Rich_young_male_pedestrian.png').convert_alpha(), (alpha, beta))
                    elif dice2 == 4:
                        att = pg.transform.scale(pg.image.load('Images/agents/pedestrian/Rich_young_female_pedestrian.png').convert_alpha(), (alpha, beta))
                elif cell_val == 'PP':
                    if dice3 == 1:
                        att = pg.transform.scale(pg.image.load('Images/agents/pedestrian/Poor_old_male_pedestrian.png').convert_alpha(), (alpha, beta))
                    elif dice3 == 2:
                        att = pg.transform.scale(pg.image.load('Images/agents/pedestrian/Poor_old_female_pedestrian.png').convert_alpha(), (alpha, beta))
                    elif dice3 == 3:
                        att = pg.transform.scale(pg.image.load('Images/agents/pedestrian/Poor_young_male_pedestrian.png').convert_alpha(), (alpha, beta))
                    elif dice3 == 4:
                        att = pg.transform.scale(pg.image.load('Images/agents/pedestrian/Poor_young_female_pedestrian.png').convert_alpha(), (alpha, beta))
                elif cell_val == 'IP':
                    if dice4 == 1:
                        att = pg.transform.scale(pg.image.load('Images/agents/injured/Poor_old_male_injured.png').convert_alpha(), (alpha, beta))
                    elif dice4 == 2:
                        att = pg.transform.scale(pg.image.load('Images/agents/injured/Poor_old_female_injured.png').convert_alpha(), (alpha, beta))
                    elif dice4 == 3:
                        att = pg.transform.scale(pg.image.load('Images/agents/injured/Poor_young_male_injured.png').convert_alpha(), (alpha, beta))
                    elif dice4 == 4:
                        att = pg.transform.scale(pg.image.load('Images/agents/injured/Poor_young_female_injured.png').convert_alpha(), (alpha, beta))
                elif cell_val == 'IY':
                    if dice5 == 1:
                        att = pg.transform.scale(pg.image.load('Images/agents/injured/Rich_young_male_injured.png').convert_alpha(), (alpha, beta))
                    elif dice5 == 2:
                        att = pg.transform.scale(pg.image.load('Images/agents/injured/Poor_young_male_injured.png').convert_alpha(), (alpha, beta))
                    elif dice5 == 3:
                        att = pg.transform.scale(pg.image.load('Images/agents/injured/Rich_young_female_injured.png').convert_alpha(), (alpha, beta))
                    elif dice5 == 4:
                        att = pg.transform.scale(pg.image.load('Images/agents/injured/Poor_young_female_injured.png').convert_alpha(), (alpha, beta))
                elif cell_val == 'PY':
                    if dice6 == 1:
                        att = pg.transform.scale(pg.image.load('Images/agents/pedestrian/Poor_young_male_pedestrian.png').convert_alpha(), (alpha, beta))
                    elif dice6 == 2:
                        att = pg.transform.scale(pg.image.load('Images/agents/pedestrian/Rich_young_male_pedestrian.png').convert_alpha(), (alpha, beta))
                    elif dice6 == 3:
                        att = pg.transform.scale(pg.image.load('Images/agents/pedestrian/Rich_young_female_pedestrian.png').convert_alpha(), (alpha, beta))
                    elif dice6 == 4:
                        att = pg.transform.scale(pg.image.load('Images/agents/pedestrian/Poor_young_female_pedestrian.png').convert_alpha(), (alpha, beta))
                elif cell_val == 'IO':
                    if dice7 == 1:
                        att = pg.transform.scale(pg.image.load('Images/agents/injured/Rich_old_male_injured.png').convert_alpha(), (alpha, beta))
                    elif dice7 == 2:
                        att = pg.transform.scale(pg.image.load('Images/agents/injured/Rich_old_female_injured.png').convert_alpha(), (alpha, beta))
                    elif dice7 == 3:
                        att = pg.transform.scale(pg.image.load('Images/agents/injured/Poor_old_male_injured.png').convert_alpha(), (alpha, beta))
                    elif dice7 == 4:
                        att = pg.transform.scale(pg.image.load('Images/agents/injured/Poor_old_female_injured.png').convert_alpha(), (alpha, beta))
                elif cell_val == 'PO':
                    if dice8 == 1:
                        att = pg.transform.scale(pg.image.load('Images/agents/pedestrian/Rich_old_male_pedestrian.png').convert_alpha(), (alpha, beta))
                    elif dice8 == 2:
                        att = pg.transform.scale(pg.image.load('Images/agents/pedestrian/Rich_old_female_pedestrian.png').convert_alpha(), (alpha, beta))
                    elif dice8 == 3:
                        att = pg.transform.scale(pg.image.load('Images/agents/pedestrian/Poor_old_male_pedestrian.png').convert_alpha(), (alpha, beta))
                    elif dice8 == 4:
                        att = pg.transform.scale(pg.image.load('Images/agents/pedestrian/Poor_old_female_pedestrian.png').convert_alpha(), (alpha, beta))
                elif cell_val == 'IF':
                    att = pg.transform.scale(pg.image.load('Images/agents/injured/Rich_young_female_injured.png').convert_alpha(), (alpha, beta))
                elif cell_val == 'PF':
                    att = pg.transform.scale(pg.image.load('Images/agents/pedestrian/Rich_young_female_pedestrian.png').convert_alpha(), (alpha, beta))
                elif cell_val == 'IM':
                    att = pg.transform.scale(pg.image.load('Images/agents/injured/Rich_young_male_injured.png').convert_alpha(), (alpha, beta))
                elif cell_val == 'PM':
                    att = pg.transform.scale(pg.image.load('Images/agents/pedestrian/Rich_young_male_pedestrian.png').convert_alpha(), (alpha, beta))


                #Render player with injured person graphics
                elif cell_val == '^I' or cell_val == '^IR' or cell_val == '^PR' or cell_val == '^IP' or cell_val == '^IY' or cell_val == '^PY' or cell_val == '^IO' or cell_val == '^PO' or cell_val == '^IF' or cell_val == '^PF' or cell_val == '^IM' or cell_val == '^PM':
                    player = pg.transform.scale(pg.image.load('Images/savers/iso_up1.png').convert_alpha(), (pop1, pop2))
                    #self.game_screen.blit(player, (c_ * self.cell_size, r_ * self.cell_size))
                elif cell_val == 'vI' or cell_val == 'vIR' or cell_val == 'vPR' or cell_val == 'vIP' or cell_val == 'vIY' or cell_val == 'vPY' or cell_val == 'vIO' or cell_val == 'vPO' or cell_val == 'vIF' or cell_val == 'vPF' or cell_val == 'vIM' or cell_val == 'vPM':
                    player = pg.transform.scale(pg.image.load('Images/savers/iso_down1.png').convert_alpha(), (pop1, pop2))
                    #self.game_screen.blit(player, (c_ * self.cell_size, r_ * self.cell_size))
                elif cell_val == '<I' or cell_val == '<IR' or cell_val == '<PR' or cell_val == '<IP' or cell_val == '<IY' or cell_val == '<PY' or cell_val == '<IO' or cell_val == '<PO' or cell_val == '<IF' or cell_val == '<PF' or cell_val == '<IM' or cell_val == '<PM':
                    player = pg.transform.scale(pg.image.load('Images/savers/iso_left1.png').convert_alpha(), (pop2, pop1))
                    #self.game_screen.blit(player, (c_ * self.cell_size, r_ * self.cell_size))
                elif cell_val == '>I' or cell_val == '>IR' or cell_val == '>PR' or cell_val == '>IP' or cell_val == '>IY' or cell_val == '>PY' or cell_val == '>IO' or cell_val == '>PO' or cell_val == '>IF' or cell_val == '>PF' or cell_val == '>IM' or cell_val == '>PM':
                    player = pg.transform.scale(pg.image.load('Images/savers/iso_right1.png').convert_alpha(), (pop2, pop1))
                    #self.game_screen.blit(player, (c_ * self.cell_size, r_ * self.cell_size))


                text_surf = cell_font.render(cell_val, True, pg.color.Color(MapColors.text.value))
                self.play_area.blit(text_surf, ((c_ * self.cell_size) + self.cell_size // 2,
                                                (r_ * self.cell_size) + self.cell_size // 2))
                self.game_screen.blit(text_surf, ((c_ * self.cell_size) + self.cell_size // 2,
                                                (r_ * self.cell_size) + self.cell_size // 2))


                # Player Isometric Rendering
                if player is not None:
                    self.game_screen.blit(player, (724 + r_*51 - c_*51, 94 + r_ * 24 + c_ * 24))
                # Agent Isometric Rendering
                elif agent is not None:
                    self.game_screen.blit(agent, (724 + r_*51 - c_*51, 94 + r_ * 24 + c_ * 24))
                elif att is not None:
                    self.game_screen.blit(att, (730 + r_ * 51 - c_ * 51, 50 + r_ * 24 + c_ * 24))

                textsurface = self.myfont.render(self.reward, False, (255, 255, 255))
                self.game_screen.blit(textsurface, (600, 600))

        pg.display.update()

    def run(self):

        print('Starting new game with human play!')
        # Set up pygame loop for game, capture actions, and redraw the screen on action
        self.env.reset()
        self.env.render_mode = PlayTypes.machine  # We'll draw the screen manually and not render each turn
        pg.init()
        #self.game_screen = pg.display.set_mode((1000, 800))

        self.game_screen = pg.display.set_mode((1500, 800))

        # caption and icon
        pg.display.set_caption('SGW {}'.format(Grid.tag))
        icon = pg.image.load('Images/icon.jpg')
        pg.display.set_icon(icon)


        self.play_area = pg.Surface((self.env.grid.rows * self.cell_size, self.env.grid.cols * self.cell_size))
        #self.play_area.fill(pg.color.Color(MapColors.play_area.value))
        #self.game_screen.fill(pg.color.Color(MapColors.game_screen.value))
        self._draw_screen()
        #the battery doesnt appear until one key is pressed. why?
        #battery = pg.transform.scale(pg.image.load('Images/UI/fullbattery.png').convert_alpha(), (200,100))
        #self.game_screen.blit(battery, (1200, 10))
        #####   make a total energy rn variable, and show a different value battery every time it changes >10%
        #####
        #####
        #####

        # Main game loop, capture window events, actions, and redraw the screen with updates until game over
        game_exit = False
        energyvar = self.env.max_energy
        while not game_exit:
            for event in pg.event.get():

                # Exit game upon window close
                if event.type == pg.QUIT:
                    game_exit = True
                    self.done()

                if self.turn < self.max_turn and not self.is_game_over:

                    # Execute main turn logic
                    # Start by getting the action, only process a turn if there is an actual action
                    # Catch the player inputs, capture key stroke
                    action = None
                    if event.type == pg.KEYDOWN:
                        if event.key == pg.K_ESCAPE:
                            game_exit = True
                            pg.quit()
                            self.done()
                        if event.key in [pg.K_w, pg.K_SPACE, pg.K_UP, pg.K_3]:
                            action = Actions.step_forward
                        if event.key in [pg.K_a, pg.K_LEFT, pg.K_1]:
                            action = Actions.turn_left
                            # action = Actions.turn_right  # changed to accomadate isometric
                        if event.key in [pg.K_d, pg.K_RIGHT, pg.K_2]:
                            action = Actions.turn_right
                            # action = Actions.turn_left  # changed to accomadate isometric
                        if event.key in [pg.K_s, pg.K_DOWN, pg.K_0]:
                            action = Actions.none



                    if action is not None:
                        if action in [Actions.step_forward, Actions.turn_right, Actions.turn_left, Actions.none]:
                            # We have a valid action, so let's process it and update the screen
                            encoded_action = self.env.encode_raw_action(action)  # Ensures clean action
                            action_decoded = self.env.decode_raw_action(encoded_action)

                            # Take a step, print the status, render the new state
                            ######## this hasn't taken batteries into account ^^
                            battery = None
                            energyvar -= 1
                            self.game_screen.fill((0, 0, 0))
                            if energyvar<=self.env.max_energy and energyvar>(self.env.max_energy*0.9):

                                battery = pg.transform.scale(pg.image.load('Images/UI/100per.png').convert_alpha(), (200,100))
                                self.game_screen.blit(battery, (1200, 10))
                            if energyvar<=(self.env.max_energy*0.9) and energyvar>(self.env.max_energy*0.8):

                                battery = pg.transform.scale(pg.image.load('Images/UI/90per.png').convert_alpha(), (200,100))
                                self.game_screen.blit(battery, (1200, 10))
                            if energyvar<=(self.env.max_energy*0.8) and energyvar>(self.env.max_energy*0.7):

                                battery = pg.transform.scale(pg.image.load('Images/UI/80per.png').convert_alpha(), (200,100))
                                self.game_screen.blit(battery, (1200, 10))
                            if energyvar<=(self.env.max_energy*0.7) and energyvar>(self.env.max_energy*0.6):

                                battery = pg.transform.scale(pg.image.load('Images/UI/70per.png').convert_alpha(), (200,100))
                                self.game_screen.blit(battery, (1200, 10))
                            if energyvar<=(self.env.max_energy*0.6) and energyvar>(self.env.max_energy*0.5):

                                battery = pg.transform.scale(pg.image.load('Images/UI/60per.png').convert_alpha(), (200,100))
                                self.game_screen.blit(battery, (1200, 10))
                            if energyvar<=(self.env.max_energy*0.5) and energyvar>(self.env.max_energy*0.4):

                                battery = pg.transform.scale(pg.image.load('Images/UI/50per.png').convert_alpha(), (200,100))
                                self.game_screen.blit(battery, (1200, 10))
                            if energyvar<=(self.env.max_energy*0.4) and energyvar>(self.env.max_energy*0.3):

                                battery = pg.transform.scale(pg.image.load('Images/UI/40per.png').convert_alpha(), (200,100))
                                self.game_screen.blit(battery, (1200, 10))
                            if energyvar<=(self.env.max_energy*0.3) and energyvar>(self.env.max_energy*0.2):

                                battery = pg.transform.scale(pg.image.load('Images/UI/30per.png').convert_alpha(), (200,100))
                                self.game_screen.blit(battery, (1200, 10))
                            if energyvar<=(self.env.max_energy*0.2) and energyvar>(self.env.max_energy*0.1):

                                battery = pg.transform.scale(pg.image.load('Images/UI/20per.png').convert_alpha(), (200,100))
                                self.game_screen.blit(battery, (1200, 10))
                            if energyvar<=(self.env.max_energy*0.1) and energyvar>(self.env.max_energy*0.0):

                                battery = pg.transform.scale(pg.image.load('Images/UI/10per.png').convert_alpha(), (200,100))
                                self.game_screen.blit(battery, (1200, 10))
                            if energyvar==0:
                                battery = pg.transform.scale(pg.image.load('Images/UI/0per.png').convert_alpha(), (200,100))
                                self.game_screen.blit(battery, (1200, 10))


                            if battery is not None:
                                self.game_screen.blit(battery, (1200, 10))
                            observation, reward, done, info = self.env.step(encoded_action)
                            self.env.pp_info()
                            self.is_game_over = done

                            self.reward = str(reward)

                            # Write action and stuff out to disk. Writes data to a dictionary. DATA LOGGING:
                            data_to_log = {
                                'game_id': str(self.GAME_ID),
                                'map_type': str(Grid.tag),
                                'turn': self.turn,
                                'raw_action': action,
                                'action': action_decoded,
                                'reward': reward,
                                'game_done': done,
                                'game_info': {k.replace('.', '_'): v for (k, v) in info.items()},
                                'raw_state': observation
                            }
                            #this is where we need to update the battery sprite depending on the energy variable

                            #print(self.env.pp_info())
                            #self.env.energy_info()
                            #battery = pg.transform.scale(pg.image.load('Images/UI/<%>.png').convert_alpha(), (200,100))
                            #self.game_screen.blit(battery, (1200, 10))
                            with open(self.DATA_LOG_FILE_NAME, 'a') as f_:
                                f_.write(json.dumps(data_to_log) + '\n')
                                f_.close()

                            # Tick up turn
                            self.turn += 1
                            if self.is_game_over:
                                game_exit = True
                                self.done()

                            # Draw the screen
                            if not self.is_game_over:
                                self._draw_screen()

                else:
                    # Else end the game
                    game_exit = True
                    self.done()

        pg.quit()
