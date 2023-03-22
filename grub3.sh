
#/bin/bash

sed -i 's/GRUB_CMDLINE_LINUX_DEFAULT="loglevel=3 quiet"/GRUB_CMDLINE_LINUX_DEFAULT="mitigations=off zswap.enabled=1 nowatchdog rhgb"/g' /etc/default/grub
