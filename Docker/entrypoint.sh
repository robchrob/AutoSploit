#!/bin/bash

/etc/init.d/postgresql start
/etc/init.d/apache2 start

export PATH="/opt/metasploit-framework:$PATH"

cd AutoSploit/
python autosploit.py
