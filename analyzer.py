import numpy as np
import math

# ...existing code...

def angle_between_points(p1, p2):
    dx = p2[0] - p1[0]
    dy = p2[1] - p1[1]
    return math.degrees(math.atan2(dy, dx))


def club_plane_angle(shoulder_left, shoulder_right, club_point):
    # approximate club plane using shoulders line and club vector
    mid_shoulder = ((shoulder_left[0]+shoulder_right[0])/2, (shoulder_left[1]+shoulder_right[1])/2)
    shoulder_angle = angle_between_points(shoulder_left, shoulder_right)
    club_angle = angle_between_points(mid_shoulder, club_point)
    return abs((club_angle - shoulder_angle) + 360) % 180


def hip_shoulder_rotation(left_hip, right_hip, left_shoulder, right_shoulder):
    hip_angle = angle_between_points(left_hip, right_hip)
    shoulder_angle = angle_between_points(left_shoulder, right_shoulder)
    return abs((shoulder_angle - hip_angle) + 360) % 180


def estimate_club_speed(prev_club_point, club_point, fps):
    # simple pixel distance per second approximation
    dist = math.hypot(club_point[0]-prev_club_point[0], club_point[1]-prev_club_point[1])
    return dist * fps


if __name__ == '__main__':
    # simple self-test
    print(angle_between_points((0,0),(1,1)))
    print(club_plane_angle((0,0),(1,0),(2,1)))
