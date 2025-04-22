from forest import Forest
import numpy as np
import matplotlib.pyplot as plt

def main():
    n_range = [2**i for i in range(3, 8)]
    p_range = [0.01*i for i in range(1, 100)]
    iterations = 100

    history = np.zeros((len(n_range), len(p_range)))


    for n in n_range:
        print(f"n: {n}")
        for p in p_range:
            for i in range(iterations):
                forest = Forest(n, p)
                # print(f"n: {n}, p: {p}")
                # print(f"Number of groups: {len(forest.groups)}")
                # print("")
                history[n_range.index(n)][p_range.index(p)] += np.mean([len(group) for group in forest.groups])
        
        history[n_range.index(n)] /= n*n
    
    history /= iterations


    
    print(history.shape)

    # print("Average number of groups for each n and p:")
    # for i, n in enumerate(n_range):
    #     for j, p in enumerate(p_range):
    #         print(f"n: {n}, p: {p}: {history[i][j]}")

    fig, ax = plt.subplots()
    # bp = ax.boxplot(history.T, positions=np.log2(n_range), widths=0.5)
    for i, n in enumerate(n_range):
        ax.plot(p_range, history[i], label=f"n={n}", marker='o')
    ax.set_xlabel("p")
    plt.show()


if __name__=="__main__":
    main()