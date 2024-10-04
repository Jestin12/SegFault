# from setuptools import find_packages, setup

# package_name = 'turtlebot_test'

# setup(
#     name=package_name,
#     version='0.0.0',
#     packages=find_packages(exclude=['test']),
#     data_files=[
#         ('share/ament_index/resource_index/packages',
#             ['resource/' + package_name]),
#         ('share/' + package_name, ['package.xml']),
#     ],
#     install_requires=['setuptools'],
#     zip_safe=True,
#     maintainer='ubuntu',
#     maintainer_email='ubuntu@todo.todo',
#     description='TODO: Package description',
#     license='TODO: License declaration',
#     tests_require=['pytest'],
#     entry_points={
#         'console_scripts': [
#             'my_node = turtlebot_test.my_node:main'
#         ],
#     },
# )
from setuptools import find_packages, setup
import os
from glob import glob


package_name = 'turtlebot_test'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),(os.path.join('share', package_name, 'launch'), glob(os.path.join('launch', '*launch.[pxy][yma]*')))
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer="Ze'ev Krischer",
    maintainer_email='zeev.krischer@sydney.edu.au',
    description='Testing Turtlebot Functionality Package',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'my_node = turtlebot_test.my_node:main',
            'testMotor = turtlebot_test.testMotor:testMotor',
            'testLED = turtlebot_test.testLED:testLED',
            'testScan = turtlebot_test.testScan:testScan',
            'testCamera = turtlebot_test.testCamera:testCamera',
            'testScript = turtlebot_test.testScript:main'
        ],
    },
)
