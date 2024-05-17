# Football Analysis Using YOLO

## Overview

This project leverages the YOLO (You Only Look Once) object detection algorithm to analyze football matches. It includes various modules for estimating camera movement, assigning players and balls, estimating speed and distance, and transforming views. The primary goal is to provide insightful analysis through automated detection and tracking.

## Features

- **Camera Movement Estimation**: Determines the movement of the camera to stabilize the footage.
- **Player and Ball Assignment**: Identifies and assigns players and balls in the footage.
- **Speed and Distance Estimation**: Calculates the speed and distance covered by players.
- **Team Assignment**: Differentiates between teams.
- **View Transformation**: Adjusts the perspective of the footage for better analysis.
- **YOLO Inference**: Utilizes a pre-trained YOLO model for object detection.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/harrionparrix/football-analysis-using-YOLO.git
   cd football-analysis-using-YOLO
   ```
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Prepare your video data from any dataset.
2. Run the detection using training_yolo and save the best models in ./models
3. Run the main script to start the analysis:
   ```bash
   python main.py
   ```

## Training

To train the YOLO model, use the `training_yolo.ipynb` notebook:
1. Open the notebook in Jupyter.
2. Follow the steps to train the model with your dataset.

