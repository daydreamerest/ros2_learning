import rclpy
from rclpy.node import Node

def main():
    rclpy.init() # 初始化工作，分配资源
    node = Node('python_node')# 创建一个节点实例
    node.get_logger().info('你好 Python 节点！')# 节点获取日志管理.提示
    node.get_logger().warn('你好 Python 节点！')# 节点获取日志管理.提示
    rclpy.spin(node) # 运行节点（只要不退出和打断，就会阻塞）
    rclpy.shutdown() # 主动退出、被动退出时进行清理，增加程序健壮性

if __name__ == '__main__':
    main()
