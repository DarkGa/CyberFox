echo launch preparation
apt update
apt install wget
apt install python
pip install SimpleQIWI
pip install vk_api
pip install colored
pip install requests
cd ../CyberFox/install
cp cf /data/data/com.termux/files/usr/bin
cd /data/data/com.termux/files/usr/bin
chmod +x cf
echo install complete!