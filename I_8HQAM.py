class I_8HQAM:
    def __init__(x_int, np, plt,hasNoise):
        num_sumbols=250
        def first_and_fourth_quarters():
            x1_degrees = x_int * 360 / 1.0 + 90
            x1_radians = x1_degrees * np.pi / 180.0  # sin() and cos() takes in radians
            x1_symbols = np.cos(x1_radians) + 1j * np.sin(x1_radians) * np.sqrt(3) / 4.0
            x12_symbols = x1_symbols + 2
            x13_symbols = x1_symbols - 2
            x14_symbols = x1_symbols + 1 + 1j * np.sqrt(3)
            x15_symbols = x1_symbols - 1 + 1j * np.sqrt(3)
            x16_symbols = x1_symbols - 1 - 1j * np.sqrt(3)
            x17_symbols = x1_symbols + 1 - 1j * np.sqrt(3)
            x18_symbols = x1_symbols - 1j * 2 * np.sqrt(3)
            A = [x1_symbols, x12_symbols, x13_symbols, x14_symbols, x15_symbols, x16_symbols, x17_symbols, x18_symbols]

            plt.plot(np.real(A), np.imag(A), 'ko')
            if(hasNoise):
                generateNoise(np,num_sumbols,A,plt)

        # Here we print the 8-ary HQAM constellation

        first_and_fourth_quarters()

        plt.title("Irregular 8-ary HQAM")
        plt.xlabel("Quadrature")
        plt.ylabel("In-phase")
        plt.gca().set_aspect('equal', adjustable='box')
        plt.grid(True)
        plt.show()


def generateNoise(np,num_symbols,A,plt):
    n = (np.random.randn(num_symbols) + 0.5j * np.random.randn(num_symbols)) / np.sqrt(2)
    noise_power = 0.05
    r = A + n * np.sqrt(noise_power)
    plt.plot(np.real(r), np.imag(r), 'ko')
