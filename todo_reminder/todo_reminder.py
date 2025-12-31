#!/usr/bin/python3
# SPDX-FileCopyrightText: 2025 Kazuki Fujita
# SPDX-License-Identifier: BSD-3-Clause

import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from threading import Timer

class TodoReminderNode(Node):
    def __init__(self):
        super().__init__('todo_reminder')
        self.sub = self.create_subscription(String, '/todo_add', self.add_callback, 10)
        self.pub = self.create_publisher(String, '/todo_alert', 10)

    def add_callback(self, msg: String):
        self.get_logger().info(f'TODO received: "{msg.data}", alert in 5s')
        Timer(5.0, self.publish_alert, args=[msg.data]).start()

    def publish_alert(self, text):
        alert_msg = String()
        alert_msg.data = f'ALERT: {text}'
        self.pub.publish(alert_msg)
        self.get_logger().info(f'Published alert: "{alert_msg.data}"')

def main():
    rclpy.init()
    node = TodoReminderNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

