import requests

import json

import base64

import random

import time

endpoint = "http://tanglab.pku.edu.cn:8080/generate"

data = {
    "prompt":
    # "masterpiece, best quality, brown red hair,blue eyes,twin tails,holding cat",
    "masterpiece, best quality,1girl,apron,arm up,black dress,blue eyes,dress,frilled dress,hand up,indoors,long hair,looking at viewer,maid,maid apron,maid headdress,mop,petals,puffy short sleeves,puffy sleeves,short sleeves,silver hair,smile,solo,very long hair,white apron,wrist cuffs",
    "seed":
    random.randint(0, 2**32),
    "n_samples":
    1,
    "sampler":
    "ddim",
    "width":
    512,
    "height":
    768,
    "scale":
    11,
    "steps":
    28,
    "uc":
    "lowres, bad anatomy, bad hands, text, error, missing fingers, extra digit, fewer digits, cropped, worst quality, low quality, normal quality, jpeg artifacts, signature, watermark, username, blurry"
}

req = requests.post(endpoint, json=data).json()

output = req["output"]

for x in output:

    img = base64.b64decode(x)

    with open(
            "output-" + str(output.index(x)) +
            str(time.strftime("-%Y-%m-%d-%H%M%S", time.localtime())) + ".png",
            "wb") as f:

        f.write(img)
