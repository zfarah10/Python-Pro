"""
Program Name: Lab10_zfarah_1.py
Author: Zakarie Farah
Purpose: Adjust rotation degrees to remove extra full spins
Date: 07/05/25
"""

def fix_rotation(degrees: float) -> float:
    """
    Adjusts rotation degrees to eliminate full 360-degree rotations.

    Args:
        degrees (float): The degree value to adjust.

    Returns:
        float: The adjusted degree within the 0 to 360 range.

    Raises:
        TypeError: If the input is not a number.
    """
    if not isinstance(degrees, (int, float)):
        raise TypeError("Input must be a number.")
    
    result = degrees % 360
    if result < 0:
        result += 360
    return result