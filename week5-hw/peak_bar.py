#!/usr/bin/env python3

import matplotlib.pyplot as plt
import sys
import bdg_loader

H3K27acD0 = bdg_loader.load_data(sys.argv[1])
H3K27acD2 = bdg_loader.load_data(sys.argv[2])
Klf4 = bdg_loader.load_data(sys.argv[3])
Sox2 = bdg_loader.load_data(sys.argv[4])

fig, axs = plt.subplots(4)
axs[0].bar(x=H3K27acD0['X'], height=H3K27acD0['Y'], width=100)
axs[0].set_title("H3K27acD0")
axs[1].bar(x=H3K27acD2['X'], height=H3K27acD2['Y'], width=100)
axs[1].set_title("H3K27acD2")
axs[2].bar(x=Klf4['X'], height=Klf4['Y'], width=100)
axs[3].bar(x=Sox2['X'], height=Sox2['Y'], width=100)
axs[3].set_title("Sox2")
plt.tight_layout()
plt.show()
