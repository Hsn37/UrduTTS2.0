#!/bin/bash
if [ ! -d "tacotron" ]; then
	git clone https://github.com/Usama0121/tacotron.git
fi

if [ ! -d "tvenv" ]; then
	virtualenv --system-site-packages -p python3.6 tvenv
fi
