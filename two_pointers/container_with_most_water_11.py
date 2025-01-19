"""
Problem: Container With Most Water
"""
# Link: https://leetcode.com/problems/container-with-most-water/
# Difficulty: Medium
# Time complexity: O(n)
# Space complexity: O(1)


def max_area(height: list[int]) -> int:
    """
    Given n height of bars, find the container with the most water
    """
    p1 = 0
    p2 = len(height) - 1

    area = 0
    m_area = 0
    while p1 < p2:
        area = min(height[p1], height[p2]) * (p2 - p1)
        if height[p1] <= height[p2]:
            p1 += 1
        else:
            p2 -= 1
        m_area = max(area, m_area)

    return m_area
