# hector_slam_ros2
Hector SlamのROS2バージョン<br>
現在はGeotiffマップを作成するために使用する。

## 環境
- Ubuntu22.04
- ROS2 Humble

## install
```bash
cd ~/ros2_ws/src
git clone git@github.com:NuTech-R/hector_slam_ros2.git
cd hector_slam_ros2
sudo rosdep update
rosdep install -r -y -i --from-paths .
git submodule update --init
cd ~/ros2_ws
colcon build --symlink-install
```
## for qrcode: 
```bash
sudo apt install libzbar-dev
```

# Yolov5 object detection with openvino with GPU
why? <br>
https://learnopencv.com/running-openvino-models-on-intel-integrated-gpu<br>
world_infoのパッケージ内ではHazmatLabelの認識にopenvinoを使用する必要があります。インストール方法については下記を参考にしてインストールしてください。
## Install openvino 
```bash
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

# Demo
## Geotiffマップの作り方 (for RobocupRescue)
### slam_toolboxの起動
```bash
ros2 launch slam_toolbox online_async_launch.py 
```
### tag_detectors_launchの起動
QRコード・Hazmatラベル・ArucoMarker・AprilTag、Babyfaceを認識するノードを起動する為のLaunchファイルです。<br>
```bash
ros2 launch world_info tag_detectors_launch.py
```
#### Geotiffを任意のタイミングで保存したい時
```bash
ros2 run hector_geotiff geotiff_saver
```