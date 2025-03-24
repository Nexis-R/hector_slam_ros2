# hector_slam_ros2

See the ROS Wiki for documentation: http://wiki.ros.org/hector_slam
## install
```bash
cd ~/ros2_ws/src
git clone git@github.com:Nexis-R/hector_slam_ros2.git
cd hector_slam_ros2
sudo rosdep update
rosdep install -r -y -i --from-paths .
git submodule update --init
cd ~/ros2_ws
colcon build --symlink-install
```
## for qrcode: 
```
sudo apt install libzbar-dev
```

# Nodes and launch files
```
ros2 launch world_info tag_detectors_launch.py
```
## with slam_toolbox
```bash
 ros2 launch slam_toolbox online_async_launch.py 
```

```bash
ros2 run hector_geotiff geotiff_node
```

one time saving with slam toolbox
```bash
ros2 run hector_geotiff geotiff_saver
```

# Yolov5 object detection with openvino with GPU
why? https://learnopencv.com/running-openvino-models-on-intel-integrated-gpu
## Instructions
### To get intel integrated GPU to work
Follow https://dgpu-docs.intel.com/installation-guides/ubuntu/ubuntu-jammy-arc.html
### Install openvino 
```
cd
wget https://storage.openvinotoolkit.org/repositories/openvino/packages/2022.3/linux/l_openvino_toolkit_ubuntu20_2022.3.0.9052.9752fafe8eb_x86_64.tgz
tar -xvzf l_openvino_toolkit_ubuntu20_2022.3.0.9052.9752fafe8eb_x86_64.tgz
rm l_openvino_toolkit_ubuntu20_2022.3.0.9052.9752fafe8eb_x86_64.tgz
mv l_openvino_toolkit_ubuntu20_2022.3.0.9052.9752fafe8eb_x86_64 openvino2022.3
. ~/openvino2022.3/setupvars.sh
echo '
#OpenVINO
. ~/openvino2022.3/setupvars.sh > /dev/null' >> ~/.bashrc
```
