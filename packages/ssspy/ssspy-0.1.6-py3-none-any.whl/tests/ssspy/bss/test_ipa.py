import numpy as np

from ssspy.bss._update_spatial_model import update_by_ipa


def main() -> None:
    n_sources, n_bins, n_frames = 3, 1, 100
    rng = np.random.default_rng(0)
    separated = rng.standard_normal((n_sources, n_bins, n_frames)) + 1j * rng.standard_normal(
        (n_sources, n_bins, n_frames)
    )  # (n_sources, n_bins, n_frames)
    weight = rng.uniform(0, 1, (n_sources, 1, n_frames))

    separated = update_by_ipa(separated, weight, flooring_fn=None)


if __name__ == "__main__":
    main()
