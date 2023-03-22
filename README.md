# Hickensa-Linux
Hickensa Linux is a linux distro based on arch linux it is an automated installer that installs arch as I would normally including all of the gaming tweaks I run for increased performance in the games I play on a daily basis these may also increase system responsiveness decrease frame times and increase frame rate by a long shot 

by the way to run the installer go to the terminal and type in ./main.py if you use wifi I recommend you first run nmtui and connect to your wifi 

The stuff I do is most effective on intel but they also have an effect on amd cpus 

Lets start with vm.swappiness which I am not sure applies when done in chroot but I will still talk about it here 

Vm swappiness represents the percentage of the free memory before activating swap by default it is set to 60 which is just outrageous on newer systems and it usually provides a performance boost on systems with greater or equal to 8gb of ram hence why the installer asks you to type in your ram amount setting it to 10 improves performance by a lot (I think you can tell why)

Now lets jump into a intel specific change 

mitigations=off this turns off meltdown and spectre protection it makes A HUGE performance boost on intel and basically nothing on amd 

The rest also work on amd systems

zswap.enabled=1 this enables zswap it improves performance in the case of this distro maybe not by a lot since vm swappiness but eh a performance boost is still better than nothing

nowatchdog can improve boot times (a lot cause on a vm while testing having a lot of stuff opened the thing booted up in less than 2 seconds I had pycharm discord steam 17 tabs of thunar like thats crazy)

Now this one is only applied for desktop users since on laptops it would cause temperature hell can be enabled if your laptop has really good cooling manually by adding it to /etc/default/grub GRUB_CMDLINE_LINUX_DEFAULT’s quotes

processor.ignore_ppc=1 this tells linux to ignore the bios set cpu frequency limit 

It also uses the zen kernel by default which is known for performance and latency improvements 
