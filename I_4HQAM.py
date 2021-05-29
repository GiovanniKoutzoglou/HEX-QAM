class I_4HQAM:
    def __init__(x_int, np, plt,hasNoise):
        num_symbols = 250
        def quarters():
            x1_degrees = x_int * 360 / 1.0
            x1_radians = x1_degrees * np.pi / 180.0  # sin() and cos() takes in radians
            x1_symbols = np.cos(x1_radians) + 1j * np.sin(x1_radians)
            x2_degrees = x_int * 360 / 1.0 + 180  # 180 degrees
            x2_radians = x2_degrees * np.pi / 180.0  # sin() and cos() takes in radians
            x2_symbols = np.cos(x2_radians)
            x12_symbols = x1_symbols - 1 + 1j * np.sqrt(3)
            x21_symbols = x2_symbols + 1 - 1j * np.sqrt(3)
            A = [x1_symbols, x2_symbols, x12_symbols, x21_symbols]

            plt.plot(np.real(A), np.imag(A), 'ko')
            if (hasNoise):
                generateNoise(np, num_symbols,A, plt)

        # Here we print the 4-ary HQAM constellation

        quarters()
        plt.title("Irregular 4-ary HQAM")
        plt.xlabel("Quadrature")
        plt.ylabel("In-phase")
        plt.gca().set_aspect('equal', adjustable='box')
        plt.grid(True)
        plt.show()


def generateNoise(np, num_symbols,A,plt):
    n = (np.random.randn(num_symbols) + 0.5j * np.random.randn(num_symbols)) / np.sqrt(2)
    noise_power = 0.05
    r = A + n * np.sqrt(noise_power)
    plt.plot(np.real(r), np.imag(r), 'ko')


