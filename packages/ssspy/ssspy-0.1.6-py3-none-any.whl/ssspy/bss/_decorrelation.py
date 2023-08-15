import numpy as np


def decorrelate(input: np.ndarray) -> np.ndarray:
    U, _, V_Hermite = np.linalg.svd(input)
    output = U @ V_Hermite

    return output


def decorrelate_by_gram_schmidt(input: np.ndarray) -> np.ndarray:
    if src_idx > 0:
        W_n = W[:src_idx]  # (src_idx - 1, n_channels)
        scale = np.sum(W_n * w_n, axis=-1, keepdims=True)
        w_n = w_n - np.sum(scale * W_n, axis=0)
