#!/bin/python
import os

print('Hello and welcome to the Hickensa Linux installer and please read the prompts given as if you dont the installer may not end up working if there are any issues contact me on discord https://discord.gg/aXm6mwchfp')

os.system('lsblk')

disk = input('What partiton would you like to install HickOS on? make sure you make a swap partition and make all partitions in this order 1.efi 2.swap (make sure it is 2x your ram) 3.root \n')

os.system('cgdisk /dev/' + disk)

substring="nvme"

if substring in disk:
    os.system('mkfs.ext4 /dev/' + disk + "p3")
    os.system('mkswap /dev/' + disk + "p2")
    os.system('mkfs.vfat -F32 /dev/' + disk + "p1")
    os.system('swapon /dev/' + disk + "p2")
    os.system('mount /dev/' + disk + 'p3 /mnt')
    os.system('mkdir -p /mnt/boot')
    os.system('mount /dev/' + disk + "p1 /mnt/boot")
    os.system('mkdir /mnt/stuff')
else:
    os.system('mkfs.ext4 /dev/'+disk + "3")
    os.system('mkswap /dev/'+disk + "2")
    os.system('mkfs.vfat -F32 /dev/'+disk + "1")
    os.system('swapon /dev/'+disk + "2")
    os.system('mount /dev/'+disk + '3 /mnt')
    os.system('mkdir -p /mnt/boot')
    os.system('mount /dev/'+disk + "1 /mnt/boot")
    os.system('mkdir /mnt/stuff')

os.system('pacstrap -K /mnt base base-devel linux-zen linux-zen-headers linux-firmware vim dhcpcd efibootmgr grub lightdm lightdm-gtk-greeter nano vim vi flatpak git neofetch networkmanager pipewire pipewire-pulse pipewire-jack pipewire-alsa alsa-utils wireplumber firefox')

os.system('genfstab -U /mnt >> /mnt/etc/fstab')

os.system('curl -o /mnt/stuff/chroot.py https://hickos.hickdick.workers.dev/0:/chroot.py')

os.system('chmod 755 /mnt/stuff/chroot.py')

os.system('arch-chroot /mnt /stuff/chroot.py')