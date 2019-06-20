echo launch preparation
apt update > install.log
apt install wget > install.log
apt install python > install.log
pip install SimpleQIWI > lib.log
pip install vk_api > lib.log
pip install colored > lib.log
pip install requests lib.log
cd ../CyberFox/install
cp cf /data/data/com.termux/files/usr/bin
cd /data/data/com.termux/files/usr/bin
chmod +x cf
clear
echo install complete!