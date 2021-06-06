echo "start photo atuo receive"
FILENAME=$(date +"%Y%m%d%H%M%S") 
while true
do
    NEW_FILE=$(ssh root@badapple.online "ls -tr /root/yidanetdisk/file_from_raspberryPi/ | tail -n 1")
    if [ $FILENAME = $NEW_FILE ] ; then
        echo the same
        return
    else
        FILENAME=$NEW_FILE
        scp root@badapple.online:/root/yidanetdisk/file_from_raspberryPi/$FILENAME /root/net_images/file_from_raspberryPi/
        python /root/Faster-R-CNN-with-model-pretrained-on-Visual-Genome/demo2.py --net res101 --dataset vg --load_dir /root/Faster-R-CNN-with-model-pretrained-on-Visual-Genome/data/pretrained_model \
        --image_output_folder /root/net_images/Animals_Images/ \
        --image_dir "/" --image_file /root/net_images/file_from_raspberryPi/$FILENAME
    fi    
done
