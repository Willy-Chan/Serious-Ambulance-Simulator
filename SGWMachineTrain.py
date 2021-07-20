import os
import uuid
import gym

import gym_sgw  # Required, leave in
import pandas as pd
from gym_sgw.envs.enums.Enums import MapProfiles, PlayTypes
import tensorflow as ts  # Required, leave in
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Activation, Flatten
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.models import load_model
from rl.agents.dqn import DQNAgent
from rl.policy import EpsGreedyQPolicy
from rl.memory import SequentialMemory
import numpy as np



#load weights of model, set to None for default file
load_weights = 'sgw_dqn_{preprocessor}_weights.h5f'



class SGW:
    """
    RL Algorithm: DQN
    https://github.com/wau/keras-rl2
    Deep Q Learning (DQN) https://arxiv.org/abs/1312.5602, https://www.nature.com/articles/nature14236
    pip uninstall tensorflow
    pip install tensorflow keras keras-rl2
    """
    def __init__(self, model_filename='rl-agent-trolley', data_log_path='./logs', map_file=None,
                 max_turns=500, training_steps=10000,
                 max_energy=50, rand_prof=MapProfiles.trolley, num_rows=10, num_cols=10):
        # General
        self.env_name = 'SGW-v0'
        self.game_id = uuid.uuid4()

        self.map_file = map_file

        # Training specific
        self.model_filename = model_filename
        self.data_log_path = data_log_path
        self.allow_overwrite = True
        self.training_steps = training_steps
        self.test_cases = 1
        self._verbosity = 1
        self.max_turns = max_turns  # to prevent endless loops and games
        # Env details
        self.env = None
        self.max_energy = max_energy
        self.rand_prof = rand_prof
        self.num_rows = num_rows
        self.num_cols = num_cols
        self._setup()

    def _setup(self):
        # Game parameters
        self.env = gym.make(self.env_name)
        self.env.play_type = PlayTypes.machine  # Machine play game variant.
        self.env.render_mode = PlayTypes.machine  # Machine play game variant.
        self.env.max_energy = self.max_energy
        self.env.rand_profile = self.rand_prof
        self.env.num_rows = self.num_rows
        self.env.num_cols = self.num_cols


        self.env.map_file = self.map_file


        self.env.reset()
        # Report success
        print('Created new environment {0} with GameID: {1}'.format(self.env_name, self.game_id))

    def done(self):
        print('Training finished!')
        self._cleanup()

    def _cleanup(self):
        self.env.close()


    def run(self):
        print('Starting new game for training!')
        action_size = self.env.action_space.n
        state_shape = self.env.observation_space.shape
        print('Number of actions: {}'.format(action_size))
        print('Shape of state: {}'.format(state_shape))

        # Build the model
        model = ts.keras.models.Sequential()
        model.add(Flatten(input_shape=(1,) + state_shape))  # take state and flatten so each example is a 1d array
        model.add(Dense(500))  # More or less nodes or layers?
        model.add(Activation('relu'))  # why this?
        model.add(Dense(500))  # why not sparse?
        model.add(Activation('relu'))  # try sigmoid or others?
        model.add(Dense(action_size))  # force the output to be the same size as our action space
        model.add(Activation('linear'))  # try softsign or others?
        print(model.summary())  # give it a nice look :)



###########################     Set Load Weights
        if load_weights is not None:
            model.load_weights(load_weights)
        elif load_weights is None:
            model.load_weights('sgw_dqn_{}_weights.h5f'.format(self.model_filename))        #load weights of model

###########################
        # model.load_weights('sgw_dqn_{}_weights.h5f'.format(self.model_filename))        #load weights of model


        # Create agent and test
        memory = SequentialMemory(limit=10000, window_length=1)
        policy = EpsGreedyQPolicy()
        sgw_dqn = DQNAgent(model=model,             #Deep Q Reinforcement Learning Agent: can be replaced
                           policy=policy,
                           memory=memory,
                           nb_actions=action_size,
                           nb_steps_warmup=500,
                           target_model_update=1e-2,
                           enable_double_dqn=True,
                           enable_dueling_network=True,
                           # dueling_type='avg'  # what other options are there?
                           )
        sgw_dqn.compile(Adam(lr=1e-3), metrics=['mae'])             #Learns off of the "Mean Average Error"

        # Training - yes that's all there is to it.
        history_callback = sgw_dqn.fit(self.env,
                                       nb_steps=self.training_steps,
                                       verbose=self._verbosity,
                                       nb_max_episode_steps=self.max_turns,
                                       log_interval=int(self.training_steps / 100),
                                       )
        # Create a dataframe and output the per epoch data
        hist_df = pd.DataFrame(history_callback.history)
        hist_json_file = os.path.join(self.data_log_path, self.model_filename + '_training.json')
        hist_csv_file = os.path.join(self.data_log_path, self.model_filename + '_training.csv')
        with open(hist_json_file, mode='w+') as f_:
            hist_df.to_json(f_)
            f_.close()
        with open(hist_csv_file, mode='w') as f_:
            hist_df.to_csv(f_)
            f_.close()

        ############ Test whole "episodes" and single action
        self.env.render_mode = PlayTypes.machine
        sgw_dqn.test(self.env,                                                  #Actually tuns through your agent as many times as you say
                     nb_episodes=self.test_cases,
                     nb_max_episode_steps=self.max_turns
                     )

        # Testing an action (Step-by-step)
        self.env.reset()
        new_obs, t_score, t_game_over, t_info = self.env.step(self.env.action_space.sample())       #Gets a random sample
        print(t_info)
        selected_action = sgw_dqn.forward(observation=new_obs)      #Test new sample from agent
        pretty_action = self.env.decode_raw_action(self.env.encode_raw_action(selected_action))     #feed forward, instead of random
        print(pretty_action)

        # Save model
        if load_weights is None:
            sgw_dqn.save_weights('sgw_dqn_{}_weights.h5f'.format(self.model_filename), overwrite=self.allow_overwrite)
            sgw_dqn.load_weights('sgw_dqn_{}_weights.h5f'.format(self.model_filename))
        elif load_weights is not None:
            sgw_dqn.save_weights('sgw_dqn_{preprocessor}_weights.h5f', overwrite=self.allow_overwrite)
            sgw_dqn.load_weights('sgw_dqn_{preprocessor}_weights.h5f')


        self.done()
