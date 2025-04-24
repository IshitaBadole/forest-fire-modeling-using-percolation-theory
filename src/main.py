from forest import Forest
import numpy as np
import matplotlib.pyplot as plt

def main():
    n_range = [2**i for i in range(3, 10)]
    p_range = [0.01*i for i in range(1, 100)]
    iterations = 100
    n_critical = 0.5

    history = np.zeros((len(n_range), len(p_range)))


    for n in n_range:
        print(f"n: {n}")
        for p in p_range:
            for i in range(iterations):
                forest = Forest(n, p, True)
                history[n_range.index(n)][p_range.index(p)] += np.mean([len(group) for group in forest.groups])
        
        history[n_range.index(n)] /= n*n
    
    history /= iterations


    
    # print(history.shape)
    np.save("history_diagonal2.npy", history)

    history = np.load("history_diagonal2.npy")

    table = {}
    for i in range(len(n_range)):
        
        table[n_range[i]] = 1-p_range[(min(range(len(history[i])), key=lambda j: abs(history[i,j]-0.5)))]

    print(table)
    # For history_diagonal => {8: 0.62, 16: 0.64, 32: 0.6699999999999999, 64: 0.72}
    # for history_diagonal2 => {8: 0.61, 16: 0.6499999999999999, 32: 0.6799999999999999, 64: 0.71, 128: 0.74, 256: 0.77, 512: 0.81}

    # print("Average number of groups for each n and p:")
    # for i, n in enumerate(n_range):
    #     for j, p in enumerate(p_range):
    #         print(f"n: {n}, p: {p}: {history[i][j]}")

    fig, ax = plt.subplots()
    for i, n in enumerate(n_range):
        ax.plot(p_range[::-1], history[i], label=f"n={n}")
    ax.set_xlabel("p")
    ax.set_ylabel("Average number of groups per grid area")
    ax.set_title("Average number of groups per grid area for different n and p")
    ax.legend()
    ax.grid(linestyle='--', alpha=0.5)
    ax.axhline(n_critical, linestyle='--', color='k')
    plt.savefig("average_groups_diagonal.png", dpi=300)
    plt.show()



if __name__=="__main__":
    main()