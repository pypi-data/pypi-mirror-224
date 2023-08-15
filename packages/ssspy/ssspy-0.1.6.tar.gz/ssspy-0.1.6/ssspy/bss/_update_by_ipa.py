# Demixing filter updates
def update_by_ipa(
    demix_filter: np.ndarray,
    weighted_covariance: np.ndarray,
    flooring_fn: Optional[Callable[[np.ndarray], np.ndarray]] = functools.partial(
        max_flooring, eps=EPS
    ),
    overwrite: bool = True,
) -> np.ndarray:
    r"""Update estimated spectrogram by iterative projection with adjustment (IPA).

    Args:
        demix_filter (numpy.ndarray):
            Demixing filters to be updated.
            The shape is (n_bins, n_sources, n_channels).
        weighted_covariance (numpy.ndarray):
            Weighted covariance matrix.
            The shape is (n_bins, n_sources, n_channels, n_channels).
        flooring_fn (callable, optional):
            A flooring function for numerical stability.
            This function is expected to return the same shape tensor as the input.
            If you explicitly set ``flooring_fn=None``,
            the identity function (``lambda x: x``) is used.
            Default: ``functools.partial(max_flooring, eps=1e-10)``.
        overwrite (bool):
            Overwrite ``demix_filter`` if ``overwrite=True``.
            Default: ``True``.

    Returns:
        numpy.ndarray of updated demixing filters of shape (n_sources, n_bins, n_frames).

    """
    if flooring_fn is None:
        flooring_fn = identity

    if overwrite:
        W = demix_filter
    else:
        W = demix_filter.copy()

    U = weighted_covariance

    n_bins, n_sources, n_channels = W.shape

    E = np.eye(n_sources, n_channels)

    for source_idx in range(n_sources):
        W_Hermite = W.transpose(0, 2, 1).conj()
        E_n_left, e_n, E_n_right = np.split(E, [source_idx, source_idx + 1], axis=-1)
        E_n = np.concatenate([E_n_left, E_n_right], axis=-1)
        U_tilde = W[:, np.newaxis, :, :] @ U @ W_Hermite[:, np.newaxis, :, :]
        U_tilde_n = U_tilde[:, source_idx, :, :]
        U_tilde_n = to_psd(U_tilde_n, axis1=-2, axis2=-1, flooring_fn=flooring_fn)
        U_tilde_n_inverse = np.linalg.inv(U_tilde_n)
        a_n = U_tilde[:, :, source_idx, source_idx]
        a_n = np.real(a_n)
        a_n = a_n @ E_n
        b_n = np.diagonal(U_tilde[:, :, source_idx, :], axis1=-2, axis2=-1)
        b_n = b_n @ E_n
        d_n = E_n.transpose(1, 0) @ U_tilde_n_inverse.conj()
        C_n = d_n @ E_n
        d_n = d_n[:, :, source_idx]

        Cd_n = np.linalg.solve(C_n, d_n)
        dCd_n = np.sum(d_n.conj() * Cd_n, axis=-1)
        dCd_n = np.real(dCd_n)
        eUe_n = U_tilde_n_inverse[:, source_idx, source_idx]
        eUe_n = np.real(eUe_n)
        z_n = eUe_n - dCd_n

        a_sqrt_n = np.sqrt(a_n)
        aa_n = a_sqrt_n[:, :, np.newaxis] * a_sqrt_n[:, np.newaxis, :]
        H_n = C_n / aa_n
        v_n = -b_n / a_sqrt_n - a_sqrt_n * Cd_n

        y_n = lqpqm2(
            H_n,
            v_n,
            z_n,
            flooring_fn=flooring_fn,
            singular_fn=lambda x: x < flooring_fn(0),
        )

        q_n = y_n / a_sqrt_n - b_n / a_n

        Eq_n = q_n.conj() @ E_n.transpose(1, 0)
        q_tilde_n = e_n.transpose(1, 0) - Eq_n

        Uq_n = np.linalg.solve(U_tilde_n, q_tilde_n)
        qUq_n = np.sum(q_tilde_n.conj() * Uq_n, axis=-1, keepdims=True)

        qUq_n = np.real(qUq_n)
        qUq_n = np.maximum(qUq_n, 0)
        denom = np.sqrt(qUq_n)
        denom = flooring_fn(denom)
        u_n = Uq_n / denom

        T_n = np.eye(n_sources, dtype=np.complex128)
        T_n = np.tile(T_n, reps=(n_bins, 1, 1))
        T_n[:, :, source_idx] = Eq_n
        T_n[:, source_idx, :] = u_n.conj()
        W[:] = T_n @ W

    return W
