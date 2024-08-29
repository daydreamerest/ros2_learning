// rclcpp为头文件（hpp），可以引入rclcpp，再使用它进行初始化
#include "rclcpp/rclcpp.hpp"

int main(int argc,char** argv)
{
    rclcpp::init(argc,argv); // 初始化
    auto node = std::make_shared<rclcpp::Node>("cpp_node");// 创建节点
    RCLCPP_INFO(node->get_logger(),"你好C++节点！"); // 打印日志
    rclcpp::spin(node); // 运行循环
    rclcpp::shutdown(); // 关闭
    return 0;
}