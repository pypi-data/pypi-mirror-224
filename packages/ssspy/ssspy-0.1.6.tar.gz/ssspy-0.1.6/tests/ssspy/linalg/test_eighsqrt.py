import numpy as np
import pytest

from ssspy.linalg import eigh

parameters_sources = [2, 5]
parameters_channels = [4, 3]
parameters_frames = [32, 16]
parameters_is_complex = [True, False]


@pytest.mark.parametrize("n_sources", parameters_sources)
@pytest.mark.parametrize("n_channels", parameters_channels)
@pytest.mark.parametrize("n_frames", parameters_frames)
@pytest.mark.parametrize("is_complex", parameters_is_complex)
def test_generalized_eigh(n_sources: int, n_channels: int, n_frames: int, is_complex: bool):
    np.random.seed(111)

    shape = (n_sources, n_channels, n_frames)

    if is_complex:
        a = np.random.randn(*shape) + 1j * np.random.randn(*shape)
        b = np.random.randn(*shape) + 1j * np.random.randn(*shape)
        A = np.mean(a[:, :, np.newaxis, :] * a[:, np.newaxis, :, :].conj(), axis=-1)
        B = np.mean(b[:, :, np.newaxis, :] * b[:, np.newaxis, :, :].conj(), axis=-1)
    else:
        a = np.random.randn(*shape)
        b = np.random.randn(*shape)
        A = np.mean(a[:, :, np.newaxis, :] * a[:, np.newaxis, :, :], axis=-1)
        B = np.mean(b[:, :, np.newaxis, :] * b[:, np.newaxis, :, :], axis=-1)

    lamb, Z = eigh(A, B)

    Lamb = lamb[..., np.newaxis] * np.eye(n_channels)
    BA = np.linalg.inv(B) @ A
    ZLZ = Z @ Lamb @ np.linalg.inv(Z)

    assert np.allclose(BA, ZLZ)
