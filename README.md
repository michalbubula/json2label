# json2label

This program converts annotated layout ground truth of historical documents (Labelme JSON format) into labeled images (PNG format).

1. Installation:

```
pip install -e .
```

2. Usage:

```
python json2label.py labelme2png  \
   -di  "directory of the GT JSON files"  \
   -do  "directory of the output PNG lables"  \
   -to  "output type. Just pass "3d" (encoded with RGB color for visibility) or "2d" (used for training a model)"
```
