#!/usr/bin/env python3

import rospy
import actionlib
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal

def navigate_to_goal(x, y, z, w):
    # Initialize the ROS node
    rospy.init_node('navigate_to_goal_move_base_client')

    # Create a SimpleActionClient for the move_base action
    client = actionlib.SimpleActionClient('move_base', MoveBaseAction)
    client.wait_for_server()

    # Create a MoveBaseGoal message
    goal = MoveBaseGoal()
    goal.target_pose.header.frame_id = "map"
    goal.target_pose.header.stamp = rospy.Time.now()

    # Set the goal position and orientation
    goal.target_pose.pose.position.x = x
    goal.target_pose.pose.position.y = y
    goal.target_pose.pose.orientation.z = z
    goal.target_pose.pose.orientation.w = w

    # Send the goal to the action server
    client.send_goal(goal)

    # Wait for the result (optional)
    client.wait_for_result()

    # Check the result
    if client.get_state() == actionlib.GoalStatus.SUCCEEDED:
        rospy.loginfo("Navigation successful!")
    else:
        rospy.logerr("Navigation failed!")

if __name__ == '__main__':
    try:
        # Set the goal position and orientation
        x = 1.2
        y = 2.1
        z = 0.0
        w = 1.0

        # Call the navigate_to_goal function
        navigate_to_goal(x, y, z, w)
    except rospy.ROSInterruptException:
        pass