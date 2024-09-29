#!/bin/bash

/etc/init.d/postgresql start
/etc/init.d/apache2 start

source /usr/share/metasploit-framework/msfenv.sh

cd AutoSploit/
python autosploit.py
