#!/usr/bin/env bash

if [ ! -d ~/.local/share/a_miscs/papirus-jetbrains-icons-fix ]; then
  mkdir -p ~/.local/share/a_miscs/papirus-jetbrains-icons-fix
  cp ./jb-icons-fix.py ~/.local/share/a_miscs/papirus-jetbrains-icons-fix/jb-icons-fix.py
  chmod +x ~/.local/share/a_miscs/papirus-jetbrains-icons-fix/jb-icons-fix.py

  crontab -l | {
  cat
  echo "* * * * * /bin/python3 ~/.local/share/a_miscs/papirus-jetbrains-icons-fix/jb-icons-fix.py"
  } | crontab -

  echo 'Cron has been installed!'
else
  echo 'Cron already installed!'
fi
