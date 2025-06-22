from numpy import array, allclose
from tools.geometry.shapes_1d import CreateLoopXYParallel, CreateCoilXYParallel

def test_CreateLoopXYParallel_centered():
    loop = CreateLoopXYParallel(1.0, 4, z=2.0)
    expected = array([[1.0, 0.0, 2.0], [0.0, 1.0, 2.0], [-1.0, 0.0, 2.0], [0.0, -1.0, 2.0]])
    assert loop.shape == (4, 3)
    assert allclose(loop, expected, atol=1e-6)

def test_CreateCoilXYParallel_centered():
    coil = CreateCoilXYParallel(radius=1.0, sample_points=4, z0=0.0, length=1.0, turns=3)
    assert coil.shape == (12, 3)  # 3 turns × 4 points

    # Extract z-values of each loop and check they are centered around z=0
    zs = coil[:, 2].reshape(3, 4)
    z_means = zs[:, 0]  # Each loop has constant z
    expected_zs = array([-0.5, 0.0, 0.5])
    assert allclose(z_means, expected_zs, atol=1e-6)
