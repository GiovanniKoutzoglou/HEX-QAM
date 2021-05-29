
class R_8HQAM:
    def __init__(x_int, np, plt,hasNoise):
        num_symbols=250
        def first_and_fourth_quarters():
            x1_degrees = x_int * 360 / 1.0
            x1_radians = x1_degrees * np.pi / 180.0  # sin() and cos() takes in radians
            x1_symbols = np.cos(x1_radians) + 1j * np.sin(x1_radians)
            x12_symbols = x1_symbols + 1 + 1j * np.sqrt(3)
            x13_symbols = x1_symbols + 1 - 1j * np.sqrt(3)
            x14_symbols = x1_symbols - 1 + 1j * np.sqrt(3)
            x15_symbols = x1_symbols - 1 - 1j * np.sqrt(3)
            A = [x1_symbols, x12_symbols, x13_symbols, x14_symbols, x15_symbols]

            plt.plot(np.real(A), np.imag(A), 'ko')
            if(hasNoise):
                generateNoise(np,num_symbols,A,plt)

        def second_and_third_quarters():
            x2_degrees = x_int * 360 / 1.0 + 180
            x2_radians = x2_degrees * np.pi / 180.0  # sin() and cos() takes in radians
            x2_symbols = np.cos(x2_radians)
            x22_symbols = x2_symbols - 1 + 1j * np.sqrt(3)
            x23_symbols = x2_symbols - 1 - 1j * np.sqrt(3)
            A = [x2_symbols, x22_symbols, x23_symbols]

            plt.plot(np.real(A), np.imag(A), 'ko')

            if(hasNoise):
                generateNoise(np,num_symbols,A,plt)

        # Here we print the 8-ary HQAM constellation

        first_and_fourth_quarters()
        second_and_third_quarters()

        plt.title("Regular 8-ary HQAM")
        plt.xlabel("Quadrature")
        plt.ylabel("In-phase")
        plt.gca().set_aspect('equal', adjustable='box')
        plt.grid(True)
        plt.show()


def generateNoise(np, num_symbols, A, plt):
    n = (np.random.randn(num_symbols) + 0.5j * np.random.randn(num_symbols)) / np.sqrt(2)
    noise_power = 0.05
    r = A + n * np.sqrt(noise_power)
    plt.plot(np.real(r), np.imag(r), 'ko')

