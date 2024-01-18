# Project Title

License Plate Detection Feature

## Description


## Installation

Before any installations are made, ensure you have the following models with you:

1. yolov8: For more about this, go to [ultralytics.com](https://docs.ultralytics.com/models/yolov8/)
2. Custom trained model for license plate detection: (Watch this [video](https://youtu.be/LNwODJXcvt4) to learn to train your own model)
   Once obtained, add the models to the `models` folder in the root directory of this project.

Create a virtual environment and activate it.
`python -m venv env` where env is the name of the virtual environment.

`venv\Scripts\activate` (Windows)

`source venv/bin/activate` (Linux)

To install the dependencies, run the following command:
`pip install -r requirements.txt`

Ensure to also clone the SORT real time tracking repository from [here](https://github.com/abewley/sort) and add it to the root directory of this project.

## Usage

To run the program, run the following command:
`python app.py`

The config.yaml file contains the configurations used when training the custom model.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

[]: # (MIT)
