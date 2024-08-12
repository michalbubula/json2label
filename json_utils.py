import json
import numpy as np
import cv2
import os
from tqdm import tqdm


def json_converter(json_dir, png_out, type_out):
    f = open(json_dir)
    data = json.load(f)
    size = {
        "height": int(data["imageHeight"]),
        "width": int(data["imageWidth"])
    }
    image = np.zeros((size["height"], size["width"], 3), np.uint8)
    image[:, :] = (0, 0, 0) #background color
    color2d = (1,1,1)
    color3d = {
        "paragraph": (255, 0, 0),
        "header": (0, 255, 255),
        "pagenumber": (0, 255, 0),
        "dropcapital": (0, 0, 255)
    }
    
    for key in data["shapes"]:        
        points = np.array(key["points"], dtype=np.int32)
        
        if key['label'] == "paragraph":
            if type_out == "3d":
                cv2.fillPoly(image, pts = [points], color = color3d["paragraph"])
            elif type_out == "2d":
                cv2.fillPoly(image, pts = [points], color = color2d)
                
        if key['label'] == "header":
            if type_out == "3d":
                cv2.fillPoly(image, pts = [points], color = color3d["header"])
            elif type_out == "2d":
                cv2.fillPoly(image, pts = [points], color = color2d)
                
        if key['label'] == "pagenumber": 
            if type_out == "3d":
                cv2.fillPoly(image, pts = [points], color = color3d["pagenumber"])
            elif type_out == "2d":
                cv2.fillPoly(image, pts = [points], color = color2d)
                
        if key['label'] == "dropcapital": 
            if type_out == "3d":
                cv2.fillPoly(image, pts = [points], color = color3d["dropcapital"])    
            elif type_out == "2d":
                cv2.fillPoly(image, pts = [points], color = color2d)
            
    json_tail = os.path.split(json_dir)
    json_name = json_tail[1].split('.')[0]
    png_name = os.path.join(png_out, json_name + ".png")
    cv2.imwrite(png_name, image)
