#!/usr/bin/env python3

from launch import LaunchDescription
from launch_ros.actions import Node, ComposableNodeContainer
from launch_ros.descriptions import ComposableNode


def generate_launch_description():
    container = ComposableNodeContainer(
            name='tag_detectors_container',
            namespace='',
            package='rclcpp_components',
            executable='component_container',
            composable_node_descriptions=[
                # ComposableNode(
                #     package='world_info',
                #     plugin='world_info::DetectAruco',
                #     name='aruco_node',
                #     parameters=[{'aruco_square_length': 0.3}],
                #     remappings=[('/image_rect', '/color/image_raw')],
                # ),
                ComposableNode(
                    package='world_info',
                    plugin='world_info::DetectQR',
                    name='qr_node',
                    parameters=[{'qr_square_length': 0.04}],
                    remappings=[('/image_rect', '/camera/camera/color/image_raw')],
                ),
                # ComposableNode(
                #     package='world_info',
                #     plugin='world_info::DetectHazmatSeg',
                #     name='hazmat_node',
                #     parameters=[{'hazmat_confidence_threshold': 0.9},
                #                 {'inference_mode': "CPU"}],
                #     remappings=[('/image_rect', '/camera/camera/color/image_raw')],
                # ),
                # ComposableNode(
                #     package='world_info',
                #     plugin='world_info::DetectBabyface',
                #     name='babyface_node',
                #     parameters=[{'babyface_confidence_threshold': 0.9},
                #                 {'inference_mode': "CPU"}],
                #     remappings=[('/image_rect', '/camera/camera/color/image_raw')],
                # ),
            ],
            output='both',
    )

    world_info_node = Node(
        package='world_info',
        executable='world_info',
        output='both',
    )

    geotiff_node_slam_toolbox = Node(
        package='hector_geotiff',
        executable='geotiff_node_slam_toolbox',
        output='both',
    )

    return LaunchDescription([container, world_info_node])
