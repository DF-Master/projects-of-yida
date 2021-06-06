echo "start photo atuo collect"
while true
do
    FILENAME=$(date +"%Y%m%d%H%M%S")
    fswebcam /dev/video0 --no-banner -r 960x720 /root/logicphotos/$FILENAME.jpg
    scp /root/logicphotos/$FILENAME.jpg root@badapple.online:/root/yidanetdisk/file_from_raspberryPi
    sleep 10
done