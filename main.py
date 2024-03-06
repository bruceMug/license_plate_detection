import video_details as vd
import app as app_run
from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter
import os
import warnings
warnings.simplefilter("ignore")


def parse_arguments():
    # Parse command line arguments
    parser = ArgumentParser(formatter_class=ArgumentDefaultsHelpFormatter)
    parser.add_argument("-v", "--source", required=True,
                        help="Path to the input video file")
    parser.add_argument("-o", "--dest", default="./processed_video",
                        help="Output path for processed videos")
    args = vars(parser.parse_args())

    # Check if the source video file exists
    if not os.path.isfile(args['source']):
        raise FileNotFoundError(
            f"The specified source video file '{args['source']}' does not exist.")

    # Check if the destination directory exists, create it if not
    os.makedirs(args['dest'], exist_ok=True)

    # Check if the source video file has a valid extension
    valid_video_extensions = ['.mp4', '.avi', '.mkv', '.mov']
    source_extension = os.path.splitext(args['source'])[1].lower()

    if source_extension not in valid_video_extensions:
        raise ValueError(
            f"The source video file must have one of the following extensions: {', '.join(valid_video_extensions)}")

    return args


if __name__ == "__main__":
    args = parse_arguments()

    # get all video details
    vd.get_video_details(args['source'])

    try:
        app_run.main(args['source'], args['dest'])
    except:
        print('Did nothing.')
        pass
    print('Processing video completed.')
