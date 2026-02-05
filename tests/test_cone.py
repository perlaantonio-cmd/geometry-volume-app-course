import math
import pytest
from geometry.cone import volume_cone


def test_volume_cone_valid_inputs():
    """
    Test volume computation for valid cone dimensions.
    """
    base_radius, height = 3.0, 5.0
    expected = (1.0 / 3.0) * math.pi * (base_radius ** 2) * height
    assert volume_cone(base_radius, height) == pytest.approx(expected, rel=1e-6)


def test_volume_cone_negative_dimension():
    """
    Document current behaviour when a negative dimension is used.
    """
    base_radius, height = 3.0, -5.0
    expected = (1.0 / 3.0) * math.pi * (base_radius ** 2) * height
    assert volume_cone(base_radius, height) == pytest.approx(expected, rel=1e-6)


def test_volume_cone_float_tolerance():
    """
    Test volume computation using approximate comparison.
    """
    base_radius, height = 1.1, 2.2
    expected = (1.0 / 3.0) * math.pi * (base_radius ** 2) * height
    assert volume_cone(base_radius, height) == pytest.approx(expected, rel=1e-6)
