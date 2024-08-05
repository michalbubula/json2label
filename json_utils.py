import json
import numpy as np
import cv2
import os
from tqdm import tqdm

#dir_jsons_in = "/home/michalbubula/labelme/jsons"
#dir_labels_out = "/home/michalbubula/labelme/labels"

#ls_jsons = os.listdir(dir_jsons_in)

def json_converter(json_dir, png_out):
    f = open(json_dir)
    data = json.load(f)
    size = {
        "height": int(data["imageHeight"]),
        "width": int(data["imageWidth"])
    }
    image = np.zeros((size["height"], size["width"], 3), np.uint8)
    image[:, :] = (0, 0, 0) #background color
    colors = {
        "paragraph": (255, 0, 0),
        "header": (0, 255, 255),
        "pagenumber": (0, 255, 0),
        "dropcapital": (0, 0, 255)
    }
    
    for key in data["shapes"]:        
        points = np.array(key["points"], dtype=np.int32)
        if key['label'] == "paragraph":
            cv2.fillPoly(image, pts = [points], color = colors["paragraph"])
        elif key['label'] == "header":
            cv2.fillPoly(image, pts = [points], color = colors["header"])
        elif key['label'] == "pagenumber": 
            cv2.fillPoly(image, pts = [points], color = colors["pagenumber"])
        elif key['label'] == "dropcapital": 
            cv2.fillPoly(image, pts = [points], color = colors["dropcapital"])    
            
    json_tail = os.path.split(json_dir)
    json_name = json_tail[1].split('.')[0]
    png_name = os.path.join(png_out, json_name + ".png")
    cv2.imwrite(png_name, image)
  
"""  
ls_jsons = os.listdir(dir_jsons_in)
    
for ind in tqdm(ls_jsons):
    json_name = os.path.join(dir_jsons_in, ind)
    json_converter(json_name)
    
"""