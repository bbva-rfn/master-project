from joblib import Parallel, delayed


def update_default(node, g, mu, beta):
    q = 1
    for s, w in zip(node[3], node[4]):
        q = q * (1 - beta * w * g[s][1])
    p = node[1]
    node[2] = (1 - q) * (1 - p) + (1 - mu) * p + mu * (1 - q) * p

    if not (0 <= node[2] <= 1):
        node[2] = p


def iteration(mu):
    iterations = 100
    beta_array = np.around(np.arange(0, 1 + 0.01, 0.01), decimals=2)
    P = pd.DataFrame(columns=[str(x) for x in beta_array])

    for beta in beta_array:
        g = original_g.copy()
        for i in range(iterations):
            np.apply_along_axis(update_default, 1, g, *(g, mu, beta))
            g[:, 1] = g[:, 2]
            # RMSE fijo
            # politica de rewiring
        P[str(beta)] = g[:, 1]

    P.to_pickle('./results_SI/P_' + str(mu) + '.p')


if __name__ == '__main__':
    # mu_array = np.around(np.arange(0,1+0.01,0.01), decimals=2)
    mu_array = [0.0]
    njobs = 50

    Parallel(n_jobs=njobs)(delayed(iteration)(mu) for mu in mu_array)
