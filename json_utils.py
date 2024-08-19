import json  
import numpy as np  
import cv2  
import os  
from tqdm import tqdm

def json_converter(json_dir, png_out, type_out):
    colors = {
        "2d": {
            "paragraph": (1, 1, 1),
            "header": (2, 2, 2),
            "pagenumber": (3, 3, 3),
            "dropcapital": (4, 4, 4),
            "footnote": (5, 5, 5),
            "footnote-continued": (6, 6, 6),
            "endnote": (7, 7, 7),
            "signature-mark": (8, 8, 8),
            "catch-word": (9, 9, 9),
            "marginalia": (10, 10, 10),
            "TOC-entry": (11, 11, 11),
            "floating": (12, 12, 12),
            "imageregion": (13, 13, 13),
            "separatorregion": (14, 14, 14),
            "graphicregion": (15, 15, 15),
            "tableregion": (16, 16, 16)
        },
        "3d": {
            "paragraph": (255, 0, 0),
            "header": (0, 255, 255),
            "pagenumber": (0, 255, 0),
            "dropcapital": (0, 0, 255),
            "footnote": (125, 0, 0),
            "footnote-continued": (125, 125, 0),
            "endnote": (125, 125, 75),
            "signature-mark": (125, 125, 125),
            "catch-word": (0, 125, 0),
            "marginalia": (0, 0, 125),
            "TOC-entry": (0, 125, 125),
            "floating": (125, 0, 125),
            "imageregion": (255, 0, 255),
            "separatorregion": (255, 125, 0),
            "graphicregion": (255, 0, 125),
            "tableregion": (255, 125, 125)
        }
    }
    
    with open(json_dir) as f:
        data = json.load(f)
        size = {
            "height": int(data["imageHeight"]),
            "width": int(data["imageWidth"])
        }
        # Initialize a black background image
        image = np.zeros((size["height"], size["width"], 3), np.uint8)
        
        for key in data["shapes"]:
            points = np.array(key["points"], dtype=np.int32)
            
            # Get the label and check if it exists in colors  
            label = key["label"]
            if label in colors[type_out.lower()]:  # Check for 2d or 3d  
                cv2.fillPoly(image, pts=[points], color=colors[type_out.lower()][label])  # Draw the filled polygon

        # Save the output image  
        json_tail = os.path.split(json_dir)
        json_name = json_tail[1].split(".")[0]
        png_name = os.path.join(png_out, json_name + ".png")
        cv2.imwrite(png_name, image)
        