import math
import pytest
from geometry.sphere import volume_sphere


def test_volume_sphere_valid_inputs():
    """
    Test volume computation for a valid sphere radius.
    """
    radius = 3.0
    expected = (4.0 / 3.0) * math.pi * (radius ** 3)
    assert volume_sphere(radius) == pytest.approx(expected, rel=1e-6)


def test_volume_sphere_negative_radius():
    """
    The implementation raises ValueError for negative radius.
    """
    radius = -3.0
    with pytest.raises(ValueError):
        volume_sphere(radius)


def test_volume_sphere_float_tolerance():
    """
    Test volume computation using approximate comparison.
    """
    radius = 1.1
    expected = (4.0 / 3.0) * math.pi * (radius ** 3)
    assert volume_sphere(radius) == pytest.approx(expected, rel=1e-6)
