#/bin/bash

mkdir /usr/share/asciiart

curl -o /usr/share/asciiart/neofetch https://hickos.hickdick.workers.dev/0:/neofetch

alias neofetch="neofetch --source /usr/share/asciiart/neofetch"

echo 'alias neofetch="neofetch --source /usr/share/asciiart/neofetch"' >> /etc/bash.bashrc
