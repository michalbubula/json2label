import click
import json
from json_utils import *
from tqdm import tqdm

@click.group()
def main():
    pass

@main.command()
@click.option(
    "--dir_json",
    "-dj",
    help="directory of GT JSON files",
    type=click.Path(exists=True, file_okay=False),
)

@click.option(
    "--dir_out_labels",
    "-do",
    help="directory where the output lables will be written in the png format.",
    type=click.Path(exists=True, file_okay=False),
)

@click.option(
    "--type_output",
    "-to",
    help="this defines if the output should be 3d (encoded with RGB color for visibility) or 2d (used for training a model). Just pass '2d' or '3d'.",
)


def labelme2png(dir_json, dir_out_labels, type_output):
    ls_jsons = os.listdir(dir_json)
    
    for ind in tqdm(ls_jsons):
        json_name = os.path.join(dir_json, ind)
        json_converter(json_name, dir_out_labels, type_output)
    
    
if __name__ == "__main__":
    main()
