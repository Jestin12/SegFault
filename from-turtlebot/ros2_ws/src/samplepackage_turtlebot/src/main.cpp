// Minimal example for getting a new turtlebot project started
// Not good coding style, this is intended to get you started

// Original written by Tara Bartlett, 2019
// Updated 2020 Donald Dansereau
// Updated for ROS2 2024 Jack Naylor

#include "rclcpp/rclcpp.hpp"
#include <iostream>
#include <string>
#include <vector>
#include <sensor_msgs/msg/laser_scan.h>
#include <geometry_msgs/msg/twist.hpp>

// declare a publisher and subscriber
// note this example uses global variables and functions, these should really be encapsulated,
// e.g. by building all of this into a class
using namespace std::chrono_literals;

class SampleTurtlebotNode : public rclcpp::Node
{
public:
    SampleTurtlebotNode() : Node("sample_turtlebot_node")
    {
        pub_vel_ = this->create_publisher<geometry_msgs::msg::Twist>("/cmd_vel", 10);
        sub_laser_ = this->create_subscription<sensor_msgs::msg::LaserScan>("/scan", 1000, std::bind(&SampleTurtlebotNode::LaserCallback, this, std::placeholders::_1));

        timer_ = this->create_wall_timer(30ms, std::bind(&SampleTurtlebotNode::timer_callback, this));
    }

private:
    void PublishVelocity(const std::vector<float> &lin_vel, const std::vector<float> &ang_vel)
    {
        auto msg = geometry_msgs::msg::Twist();

        msg.linear.x = lin_vel[0];
        msg.linear.y = lin_vel[1];
        msg.linear.z = lin_vel[2];

        msg.angular.x = ang_vel[0];
        msg.angular.y = ang_vel[1];
        msg.angular.z = ang_vel[2];

        pub_vel_->publish(msg);
    }

    void LaserCallback(const sensor_msgs::msg::LaserScan::SharedPtr msg)
    {
        // Accessing LaserScan message members
        float min_angle = msg->angle_min;
    }

    void timer_callback()
    {
        // Initialise velocity vectors
        std::vector<float> lin_vel(3, 0);
        std::vector<float> ang_vel(3, 0);
        lin_vel[0] = 1; // Go forwards

        // Publish the velocity
        PublishVelocity(lin_vel, ang_vel);
    }

    rclcpp::Publisher<geometry_msgs::msg::Twist>::SharedPtr pub_vel_;
    rclcpp::Subscription<sensor_msgs::msg::LaserScan>::SharedPtr sub_laser_;
    rclcpp::TimerBase::SharedPtr timer_;
};

int main(int argc, char **argv)
{
    rclcpp::init(argc, argv);
    auto node = std::make_shared<SampleTurtlebotNode>();
    rclcpp::spin(node);
    rclcpp::shutdown();
    return 0;
}