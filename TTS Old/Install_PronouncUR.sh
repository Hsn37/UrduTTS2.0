#!/bin/bash
if [ ! -d "PronouncUR" ]; then
	git clone https://github.com/Usama0121/PronouncUR.git
fi

if [ ! -d "pvenv" ]; then
	virtualenv --system-site-packages -p python3.6 pvenv
fi
source pvenv/bin/activate
cd PronouncUR
pip install -r requirements.txt
deactivate
