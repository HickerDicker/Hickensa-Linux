#!/bin/python
import os

CPU = int(input('what Cpu do you have 1.amd or 2.intel \n'))
if CPU==1:
    os.system("pacman -S amd-ucode")
if CPU==2:
    os.system("pacman -S intel-ucode")

Nvidia = input('do you have a NVIDIA GPU 1. yes 2. no \n')

if Nvidia==1:
    print('press y')
    os.system('pacman -S nvidia-dkms')

os.system('mkinitcpio -P')

os.system('echo "HickOS" >> /etc/hostname')

print('set up a root password')

os.system('passwd')

user = input('type in a username\n')

os.system('useradd -m -G wheel,users,audio,video' +" "+user)

print('set a password for your user')

os.system('passwd '+user)

os.system('curl -o /stuff/neofetch.sh https://hickos.hickdick.workers.dev/0:/neofetch.sh')

os.system('chmod 755 /stuff/neofetch.sh')

os.system('./stuff/neofetch.sh')

os.system('curl -o /stuff/os.sh https://hickos.hickdick.workers.dev/0:/os.sh')

os.system('chmod 755 /stuff/os.sh')

os.system('/stuff/os.sh')

os.system('grub-install --target=x86_64-efi --efi-directory=/boot --bootloader-id=GRUB --removable')

os.system('grub-mkconfig -o /boot/grub/grub.cfg')

os.system('curl -o /stuff/distributor.sh https://hickos.hickdick.workers.dev/0:/distributor.sh')

os.system('chmod 755 /stuff/distributor.sh')

os.system('/stuff/distributor.sh')

desktop = input('What desktop environment do you want (type in the package name from pacman like xfce4 gnome plasma-meta etc) you can also type in packages you may think you need here too so go ahead\n')

os.system("pacman -S "+desktop)

os.system("sed -i 's/# %wheel ALL=(ALL:ALL) ALL/ %wheel ALL=(ALL:ALL) ALL/g' /etc/sudoers")

Ram=int(input("how much ram do you have?\n"))

Device=int(input("Do you use a laptop 1.yes 2.no\n"))

if int(Ram)>=8:
    os.system("sysctl vm.swappiness=10")

if CPU==2 & Device==2:
    os.system("curl -o /stuff/grub1.sh https://hickos.hickdick.workers.dev/0:/grub1.sh")
    os.system("chmod 755 /stuff/grub1.sh")
    os.system("./stuff/grub1.sh")

if CPU==1 & Device==2:
    os.system("curl -o /stuff/grub2.sh https://hickos.hickdick.workers.dev/0:/grub2.sh")
    os.system("chmod 755 /stuff/grub2.sh")
    os.system("./stuff/grub2.sh")

if Device==1 & CPU==2:
    os.system("curl -o /stuff/grub3.sh https://hickos.hickdick.workers.dev/0:/grub3.sh")
    os.system("chmod 755 /stuff/grub3.sh")
    os.system("./stuff/grub3.sh")

if Device==1 & CPU==1:
    os.system("curl -o /stuff/grub4.sh https://hickos.hickdick.workers.dev/0:/grub4.sh")
    os.system("chmod 755 /stuff/grub4.sh")
    os.system("./stuff/grub4.sh")

os.system('grub-mkconfig -o /boot/grub/grub.cfg')

os.system('systemctl enable lightdm')

Network=int(input("Do you use wifi or not 1.yes 2.no"))

if Network==2:
    os.system('systemctl enable dhcpcd')
else:
    os.system('systemctl enable NetworkManager')

os.system('rm -rf /mnt/stuff')

print('you can now reboot as the installation is done no need to unmount anything :D')