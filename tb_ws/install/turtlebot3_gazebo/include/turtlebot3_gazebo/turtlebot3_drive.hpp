// Copyright 2019 ROBOTIS CO., LTD.
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//     http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.
//
// Authors: Taehun Lim (Darby), Ryan Shim

#ifndef TURTLEBOT3_GAZEBO__TURTLEBOT3_DRIVE_HPP_
#define TURTLEBOT3_GAZEBO__TURTLEBOT3_DRIVE_HPP_

// Include header files
#include <geometry_msgs/msg/twist.hpp>
#include <nav_msgs/msg/odometry.hpp>
#include <rclcpp/rclcpp.hpp>
#include <sensor_msgs/msg/laser_scan.hpp>
#include <sensor_msgs/msg/compressed_image.hpp>
#include <sensor_msgs/msg/image.hpp>
#include <tf2/LinearMath/Matrix3x3.h>
#include <tf2/LinearMath/Quaternion.h>

//--- Initialise const expressions -------------------------------------------
// Angles 
constexpr double DEG2RAD = (M_PI / 180.0);
constexpr double RAD2DEG = (180.0 / M_PI);

// Camera directions
constexpr int CENTER = 0;
constexpr int LEFT = 1;
constexpr int RIGHT = 2;
constexpr int FRONT_LEFT = 3;
constexpr int FRONT_RIGHT = 4; 

// Turtlebot velocities
constexpr double LINEAR_VELOCITY = 0.4;
constexpr double TURNING_VELOCITY = 0.4;
constexpr double ANGULAR_VELOCITY_LEFT = 0.3;
constexpr double ANGULAR_VELOCITY_RIGHT = 0.3;
constexpr double REVERSE_VELOCITY = -0.3;

// Turtlebot drive directions 
constexpr int DRIVE_DIRECTION = 0;
constexpr int DRIVE_FORWARD = 1;
constexpr int DRIVE_RIGHT = 2;
constexpr int DRIVE_LEFT = 3;
constexpr int DRIVE_BACK = 4;
constexpr int DRIVE_STOP = 5;

// Camera RGB values
constexpr int RED = 0;
constexpr int GREEN = 1;
constexpr int BLUE = 2; 

//--- Turtlebot3Drive Node ----------------------------------------------------
class Turtlebot3Drive : public rclcpp::Node
{
public:
  // Constructor 
  Turtlebot3Drive();

  // Destructor 
  ~Turtlebot3Drive();

private:
  // ROS topic publishers
  rclcpp::Publisher<geometry_msgs::msg::Twist>::SharedPtr cmd_vel_pub_;

  // ROS topic subscribers
  rclcpp::Subscription<sensor_msgs::msg::LaserScan>::SharedPtr scan_sub_;
  rclcpp::Subscription<nav_msgs::msg::Odometry>::SharedPtr odom_sub_;
  rclcpp::Subscription<sensor_msgs::msg::Image>::SharedPtr cam_sub_;

  // Odometer Variables
  double robot_pose_= 0;                 // turtlebot position
  double prev_robot_pose_= 0;            // previous robot position
  double position[3] = {0.0, 0.0, 0.0};  // array to store turtlebot position

  const double check_left_dist = 3.2;     // threshold value for left wall
  const double check_forward_dist = 3.4;  // threshold value for forward obstacles
  const double check_side_dist = 3.2;     // threshold value to check indicating corner

  // Lidar Variables
  double scan_data_[5];     // array for LiDAR scanner data 

  // Camera Variables
  const int RedThresh = 20;   // red finish threshold 
  const int GreenThresh = 90; // green finish threshold 
  const int BlueTresh = 20;   // blue finish threshold 
  const int PixelThresh = 3;  // number of pixels needed to finish

  static const int NumPixels = 5; // number of pixels to check in image
  int PixelSelection[NumPixels] = {518400, 1036320, 1036800, 1037280, 1555200}; // location of pixels being checked in image
  double PixelData[NumPixels][3]; // array to store RGB values of the chosen pixel locations

  // Drive status
  uint8_t turtlebot3_state_num; // Tracks the current state of the Turtlebot
  const double escape_range_ = 30.0 * DEG2RAD;

  // ROS timer
  rclcpp::TimerBase::SharedPtr update_timer_; 

  // Callback function for the Tutrlebot
  void update_callback();

  // Update the Turtlebot velocity
  void update_cmd_vel(double linear, double angular);

  // Callback for the Lidar scanner
   // Takes inputs of a shared pointer to the laserscan message
  void scan_callback(const sensor_msgs::msg::LaserScan::SharedPtr msg);

  // Callback for the odometer 
  // Takes inputs of a shared pointer to the odometer message
  void odom_callback(const nav_msgs::msg::Odometry::SharedPtr msg);

  // Callback for the camera
  // Takes inputs of a shared pointer to the sensor_message
  void cam_callback(const sensor_msgs::msg::Image::SharedPtr msg);

  // Function to store the scanner data
  // Takes inputs of a shared pointer to the laserscan message, scan angle array, scan data and array size
  void store_scan_data(const sensor_msgs::msg::LaserScan::SharedPtr& msg, const uint16_t* scan_angle, double* scan_data, size_t size);
  
  // Function to end the turtlebot motion
  void stop_turtlebot();

  // Function to look for the green maze finish line
  void check_finish_line();

  // Function to turn left 
  // Takes input of the turtlebot drive state
  void turn_left(uint8_t &turtlebot3_state_num);

  // Function to right left 
  // Takes input of the turtlebot drive state
  void turn_right(uint8_t &turtlebot3_state_num);

  // Function to drive backwards 
  // Takes input of the turtlebot drive state
  void drive_back(uint8_t &turtlebot3_state_num);

  // Function to drive forward 
  // Takes input of the turtlebot drive state
  void drive_forward(uint8_t &turtlebot3_state_num);

  // Function to check drive direction
  bool check_drive_direction();

  // Function to turn get drive direction
  void get_drive_direction();
};

#endif  // TURTLEBOT3_GAZEBO__TURTLEBOT3_DRIVE_HPP_