import time

import numpy as np

from ssspy.linalg import cholesky2


def main():
    rng = np.random.default_rng(42)

    shape = (2, 2, 32)

    start = time.perf_counter()

    for _ in range(1000):
        x = rng.standard_normal(shape) + 1j * rng.standard_normal(shape)
        X = np.mean(x[:, :, np.newaxis, :] * x[:, np.newaxis, :, :].conj(), axis=-1)

        if False:
            _ = np.linalg.cholesky(X)
        else:
            _ = cholesky2(X)

    end = time.perf_counter()

    print(end - start)


if __name__ == "__main__":
    main()
