"""
Test file for Lab10_zfarah_1.py
Author: Zakarie Farah
Purpose: Test the fix_rotation() function using pytest.
"""

import pytest
from Lab10_zfarah_1 import fix_rotation
from pathlib import Path

# Example of using pathlib to get project root (good practice)
this_file = Path(__file__)
project_root = this_file.parent.resolve()

def test_under_360():
    assert fix_rotation(100) == 100

def test_over_360():
    assert fix_rotation(460) == 100
    assert fix_rotation(820) == 100

def test_negative():
    assert fix_rotation(-100) == 260
    assert fix_rotation(-460) == 260
    assert fix_rotation(-820) == 260

def test_invalid_input():
    with pytest.raises(TypeError):
        fix_rotation("abc")
