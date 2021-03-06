import argparse
import sys

from importlib import import_module

parser = argparse.ArgumentParser(description='Run game state space commands.')
parser.add_argument('command')
parser.add_argument('arguments')

if len(sys.argv) < 2:
    #print('usage: run.py command [argument ...]', file=sys.stderr)
    sys.stderr.write('usage: run.py command [argument ...]\n')
    sys.exit(1)

COMMANDS = {}
def load_command(name):
    COMMANDS[name] = getattr(import_module('command.{}'.format(name)), name)

load_command('newmodel')
load_command('generate')
load_command('replay')
load_command('arena')
load_command('optimize')
load_command('train')
load_command('loop')

command = sys.argv[1]
if command not in COMMANDS:
    #print('unknown command `{}`'.format(command), file=sys.stderr)
    sys.stderr.write('unknown command `{}`\n'.format(command))
    sys.exit(1)

# run
COMMANDS[command](sys.argv[2:])
