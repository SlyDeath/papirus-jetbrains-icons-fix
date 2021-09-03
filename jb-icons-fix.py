#!/usr/bin/python3

import os
import subprocess

programs = {
    'datagrip': 'datagrip',
    'PhpStorm': 'phpstorm',
    'PyCharm-P': 'pycharm',
    'RubyMine': 'rubymine',
    'WebStorm': 'webstorm',
    'CLion': 'clion',
    'Goland': 'goland',
    'IDEA-U': 'intellij-idea-ultimate',
    'Rider': 'rider'
}

apps_dir = '~/.local/share/JetBrains/Toolbox/apps'
icons_dir = '/usr/share/icons/Papirus-Dark/128x128/apps'

for program in programs:
    icon = programs[program]
    diff = subprocess.getoutput(f'[ -d {apps_dir}/{program} ] && cmp {apps_dir}/{program}/ch-0/.icon.svg {icons_dir}/{icon}.svg')

    if diff:
        os.system(f'cp -f {icons_dir}/{icon}.svg {apps_dir}/{program}/ch-0/.icon.svg')
        print(f'Icon for «{program}» has been replaced...\r')
