#!bin/sh
cd /home/cat/mavrouter/usr/bin
sudo ./mavlink-routerd -e 192.168.151.168:15501 -e 192.168.151.168:15601 /dev/ttyS0:115200
#sudo ./mavlink-routerd -e 192.168.151.100:18550 -e 127.0.0.1:13250 /dev/ttyS0:115200
#sudo ./mavlink-routerd -e 192.168.122.173:18550 -e 127.0.0.1:13250 /dev/ttyACM0:115200

