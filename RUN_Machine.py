#Any input just moves the machine forward - as if a human were playing it.
#Except, it's not actually looking at YOUR input, but the training data's.

import os
import argparse
from SGWMachinePlay import SGW
from gym_sgw.envs.enums.Enums import MapProfiles

parser = argparse.ArgumentParser(description='CLI Argument Parser for Human Play.')
parser.add_argument('--agentfile', help='Agent file path and file name.', default='sgw_dqn_{real}_weights.h5f')  #DEFAULTS to this weights value
parser.add_argument('--outfile', help='Data logging file name.', default='data_log.json')
parser.add_argument('--creation', help='Allow creation of output file.', default=True, action='store_true')
# add new arguments

def validate_data(out_file, allow_creation=False):
    if allow_creation and not os.path.exists(out_file):
        f = open(out_file, 'w+')
        f.close()
    if not os.path.isfile(out_file):
        raise EnvironmentError('Bad filename provided in CLI arguments.')


if __name__ == '__main__':

    # Parse CLI Args
    args = parser.parse_args()
    os.system('mode con: cols=125 lines=62')
    validate_data(args.outfile, allow_creation=args.creation)

    # Let's you overwrite the default parts in "parser" section above
    agent_file = args.agentfile
    data_log_file = args.outfile
    # map_file = None  # 'gym_sgw/envs/maps/_SampleMap.xls'  # None will generate a random map, map files have top priority
    # map_file = 'gym_sgw/envs/maps/precursor/corridor.xls'
    # map_file = None  # 'gym_sgw/envs/maps/_SampleMap.xls'  # None will generate a random map, map files have top priority
    map_file = "training_maps"
    map_file = "custom_maps"
    max_energy = 50
    rand_prof = MapProfiles.trolley
    num_rows = 11
    num_cols = 11

    # Create and run game with those params
    sgw_env = SGW(
        agent_file=agent_file,
        data_log_file=data_log_file,
        map_file=map_file,
        max_energy=max_energy,
        rand_prof=rand_prof,
        num_rows=num_rows,
        num_cols=num_cols
    )
    sgw_env.run()
