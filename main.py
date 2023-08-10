import sys
import matplotlib.pyplot as plt


def check_arguments():
    if len(sys.argv) < 3:
        print(f"Too few arguments (2 required, {len(sys.argv)-1} provided)")
        return False


def get_arguments():
    try:
        n = len(sys.argv[1])
        chainrings = sys.argv[1][1:n-1].split(',')
        chainrings = [int(i) for i in chainrings]

        n = len(sys.argv[2])
        casette = sys.argv[2][1:n-1].split(',')
        casette = [int(i) for i in casette]

        return chainrings, casette

    except:
        return None

def calcuate_ratios(chainrings, casette_sprockets):
    result = []
    for chainring in chainrings:
        chainring_result = []
        for casette_sprocket in casette_sprockets:
            chainring_result.append(int(chainring)/int(casette_sprocket))

        result.append(chainring_result)
    return result

def visualize_results(ratios):
    for chainrings in ratios:
        x = [rear_gear for rear_gear in range(len(chainrings), 0, -1)]
        plt.scatter(x,chainrings)
    plt.show()


def main():
    
    chainrings, casette = get_arguments()


    results = calcuate_ratios(chainrings, casette)
    visualize_results(results)


if __name__ == "__main__":
    main()