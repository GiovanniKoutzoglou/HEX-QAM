num_symbols = 250


class R_4HQAM:
    def __init__(x_int, np, plt,hasNoise):

        def first_quarter():
            x1_degrees = x_int * 360 / 1.0 + 60  # 60 degrees
            x1_radians = x1_degrees * np.pi / 180.0  # sin() and cos() takes in radians
            x1_symbols = np.cos(x1_radians) + 1j * np.sin(x1_radians)
            plt.plot(np.real(x1_symbols), np.imag(x1_symbols), 'ko')

            if(hasNoise):
                generateNoise(np,x1_symbols,plt)

        def second_quarter():
            x2_degrees = x_int * 360 / 1.0 + 150  # 150 degrees
            x2_radians = x2_degrees * np.pi / 180.0  # sin() and cos() takes in radians
            x2_symbols = np.sqrt(3) * np.cos(x2_radians) - 1j * np.cos(x2_radians)
            plt.plot(np.real(x2_symbols), np.imag(x2_symbols), 'ko')

            if (hasNoise):
                generateNoise(np, x2_symbols, plt)

        def third_quarter():
            x3_degrees = x_int * 360 / 1.0 + 240  # 240 degrees
            x3_radians = x3_degrees * np.pi / 180.0  # sin() and cos() takes in radians
            x3_symbols = np.cos(x3_radians) + 1j * np.sin(x3_radians)
            plt.plot(np.real(x3_symbols), np.imag(x3_symbols), 'ko')

            if (hasNoise):
                generateNoise(np, x3_symbols, plt)

        def fourth_quarter():
            x4_degrees = x_int * 360 / 1.0 + 330  # 330 degrees
            x4_radians = x4_degrees * np.pi / 180.0  # sin() and cos() takes in radians
            x4_symbols = np.sqrt(3) * np.cos(x4_radians) - 1j * np.cos(x4_radians)
            plt.plot(np.real(x4_symbols), np.imag(x4_symbols), 'ko')

            if (hasNoise):
                generateNoise(np, x4_symbols, plt)

        first_quarter()
        second_quarter()
        third_quarter()
        fourth_quarter()
        plt.title("Regular 4-ary HQAM ")
        plt.xlabel("Quadrature")
        plt.ylabel("In-phase")
        plt.gca().set_aspect('equal', adjustable='box')
        plt.grid(True)
        plt.show()



def generateNoise(np,symbols,plt):
    n = (np.random.randn(num_symbols) + 0.5j * np.random.randn(num_symbols)) / np.sqrt(2)
    noise_power = 0.05
    r =  symbols + n * np.sqrt(noise_power)
    plt.plot(np.real(r), np.imag(r), 'ko')