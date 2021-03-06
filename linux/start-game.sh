#!/bin/sh
cd ../

# Get the user input:
read -p "Username: " ttaUsername
read -p "Gameserver (DEFAULT:  167.114.28.238): " TTA_GAMESERVER
TTA_GAMESERVER=${TTA_GAMESERVER:-"167.114.28.238"}

# Export the environment variables:
export ttaUsername=$ttaUsername
export ttaPassword="password"
export TTA_PLAYCOOKIE=$ttaUsername
export TTA_GAMESERVER="127.0.0.1"

echo "==============================="
echo "Starting Toontown Project Altis..."
echo "Username: $ttaUsername"
echo "Gameserver: $TTA_GAMESERVER"
echo "==============================="

/usr/bin/python2 -m toontown.toonbase.ClientStart