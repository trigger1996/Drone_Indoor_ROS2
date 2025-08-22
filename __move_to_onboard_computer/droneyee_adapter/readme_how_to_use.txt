#
# serial port correponding to fcu is ttyS4
#
sudo chmod 777 /dev/ttyS0    # S0 not S4
                                # if you don't know which serial, then POWER UP the fcu, and cat /dev/ttyS0 | hexdump -C, if the header of the frame is 0xfd or 0xfe, then it is MAVLink


#
# start mavlink router
#
# cd /home/pi/mavrouter/usr/bin
cd droneyee_adapter/mavlink-router/mavlink-router/

#
# the IP of this computer (onboard) doesn't matter
# 192.168.151.168 is the IP of swarm computer
# ports are related to the swarm computer, /home/droneyee/droneyee_Optics/mav.conf
# we use drone 1 -- 9 for our uavs, ports: 15501 -- 15509
# 156xx is for backup
#
# WARNING: the ID in swarm computer is related to the UAV_ID param in FCU
# NOT the PORT!
# e.g., this is our uav 1 using port 15505 then the id in swarm computer is still 1, NOT 5
#       but in this case, the uav 1 will use the pose of rigibody of droneyee5, not droneyee1
#
./mavlink-routerd -e 192.168.151.168:15501 -e 192.168.151.168:15601 /dev/ttyS0:921600




















# HOW TO INSTALL
#
1. COPY the folder to onboard computer

2. I don't know, but this can be run from a arm board, e.g., raspberry pi, or a luban cat.
   Detailed installation process:
       cd ~/droneyee_adapter/mavlink-router/mavlink-router/
       chmod 777 autogen.sh 
       ./autogen.sh 
       chmod 777 configure
       ./configure CFLAGS='-g -O2' CXXFLAGS='-g -O2' --sysconfdir=/etc --localstatedir=/var --libdir=/usr/lib 
       make -j4
       sudo make install
       ## finally test if success
       cd ~/
       mavlink-routerd 


3. MODIFY this readme for specific drone ids: ./mavlink-routerd -e 192.168.151.168:1550x -e 192.168.151.168:1560x /dev/ttyS0:921600, or mavlink-routerd -e 192.168.151.168:1550x -e 192.168.151.168:1560x /dev/ttyS0:921600

4. connect the FCU with QGC, modifify drone ID: MAV_SYS_ID, which is identical to the number above, MAINTAIN MAV_COMP_ID = 1 UNchanged !

   e.g., for uav 3, MAV_SYS_ID = 3, ./mavlink-routerd -e 192.168.151.168:15503 -e 192.168.151.168:15603 /dev/ttyS0:921600

5. modify the other EKF parameters:
   EKF2_EV_CTRL         7
   EKF2_EV_DELAY        50ms
   EKF2_HGT_REF         Range sensor
   EKF2_OF_CTRL         Enabled
   EKF2_RNG_CTRL        Enabled