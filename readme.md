This is a tiny toy for `ros2 bag record`.

## Requirements

- flask
- ROS2

My test environment is:

- Ubuntu 22.04 (on x64 Hardware)
- ROS2 Humble
- flask installed by `apt install python3-flask`
- Firefox

## How to Use

1. `git clone` or just download this repository.
1. launch a terminal, **source ROS2 setup.bash** and navigate to the cloned directory
1. run `python app.py`
1. open `localhost:5000` with a browser

## Behind the scenes

Inside `app.py`, environmental variables of the terminal are taken over and `ros2 topic list` is called.
Then the topics are categorized by their top-level namespace (we assume Autoware.universe), like...

- control
    - /control/command/control_cmd
    - /control/command/emergency_cmd
    - /control/command/gear_cmd
    - /control/command/hazard_lights_cmd
    - ...
- perception
    - /perception/object_recognition/detection/centerpoint/objects
    - /perception/object_recognition/detection/centerpoint/validation/objects
    - /perception/object_recognition/detection/clustering/clusters
    - /perception/object_recognition/detection/clustering/concat_downsampled_pcl/input/twist
    - ...
- ...