echo "test start"
FILENAME=$(ssh root@badapple.online "ls -tr /root/yidanetdisk/file_from_raspberryPi/ | tail -n 1")

NEW_FILE=$(ssh root@badapple.online "ls -tr /root/yidanetdisk/file_from_raspberryPi/ | tail -n 1")
if [ $FILENAME = $NEW_FILE ] ; then
    echo the same
    return
else
    echo not the same
fi    

