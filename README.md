# json2label

This program converts annotated ground truth of historical documents (Labelme JSON format) into labeled images (PNG format).

1. Installation:
`sh
pip install -r requirements.txt`

3. Usage:
`sh
python json2label.py labelme2png -dj "directory of GT JSON files" -do "directory where the output lables will be written in the png format"`
