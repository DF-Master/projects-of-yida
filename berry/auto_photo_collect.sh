echo "start photo atuo collect"
while true
do
    set FILENAME (date +"%Y%m%d%H%M%S") 
    # only in fish shell
    fswebcam /dev/video0 --no-banner -r 1080x720 /root/logicphotos/$FILENAME.jpg
    scp /root/logicphotos/$FILENAME.jpg root@badapple.online:/root/yidanetdisk

    
done