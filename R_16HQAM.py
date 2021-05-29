class R_16HQAM:
    def __init__(x_int, np, plt,hasNoise):
        num_symbols=250

        def first_quarter():
            x1_degrees = x_int * 360 / 1.0 + 60  # 60 degrees
            x1_radians = x1_degrees * np.pi / 180.0  # sin() and cos() takes in radians
            x1_symbols = np.cos(x1_radians) + 1j * np.sin(x1_radians)  # closest symbol to (0,0) in the 1st quarter
            x12_symbols = x1_symbols + 2
            x13_symbols = x1_symbols + 1 + 1j * np.sqrt(3)
            x14_symbols = x1_symbols + 3 + 1j * np.sqrt(3)
            A = [x1_symbols, x12_symbols, x13_symbols, x14_symbols]
            plt.plot(np.real(A), np.imag(A), 'ko')

            if(hasNoise):
                generateNoise(np,num_symbols,A,plt)
        def second_quarter():
            x2_degrees = x_int * 360 / 1.0 + 150  # 150 degrees
            x2_radians = x2_degrees * np.pi / 180.0  # sin() and cos() takes in radians
            x2_symbols = np.sqrt(3) * np.cos(x2_radians) - 1j * np.cos(
                x2_radians)  # closest symbol to (0,0) in the 2nd quarter
            x22_symbols = x2_symbols - 2
            x23_symbols = x2_symbols - 1 + 1j * np.sqrt(3)
            x24_symbols = x2_symbols + 1 + 1j * np.sqrt(3)
            A = [x2_symbols, x22_symbols, x23_symbols, x24_symbols]
            plt.plot(np.real(A), np.imag(A), 'ko')

            if(hasNoise):
                generateNoise(np,num_symbols,A,plt)

        def third_quarter():
            x3_degrees = x_int * 360 / 1.0 + 240  # 240 degrees
            x3_radians = x3_degrees * np.pi / 180.0  # sin() and cos() takes in radians
            x3_symbols = np.cos(x3_radians) + 1j * np.sin(x3_radians)  # closest symbol to (0,0) in the 3rd quarter
            x32_symbols = x3_symbols - 2
            x33_symbols = x3_symbols - 3 - 1j * np.sqrt(3)
            x34_symbols = x3_symbols - 1 - 1j * np.sqrt(3)
            A = [x3_symbols, x32_symbols, x33_symbols, x34_symbols]
            plt.plot(np.real(A), np.imag(A), 'ko')

            if(hasNoise):
                generateNoise(np,num_symbols,A,plt)

        def fourth_quarter():
            x4_degrees = x_int * 360 / 2.0 + 330  # 330 degrees
            x4_radians = x4_degrees * np.pi / 180.0  # sin() and cos() takes in radians
            x4_symbols = np.sqrt(3) * np.cos(x4_radians) - 1j * np.cos(
                x4_radians)  # closest symbol to (0,0) in the 4th quarter
            x42_symbols = x4_symbols + 2
            x43_symbols = x4_symbols + 1 - 1j * np.sqrt(3)
            x44_symbols = x4_symbols - 1 - 1j * np.sqrt(3)
            A = [x4_symbols, x42_symbols, x43_symbols, x44_symbols]
            plt.plot(np.real(A), np.imag(A), 'ko')


            if(hasNoise):
                generateNoise(np,num_symbols,A,plt)
        # Here we print the 16-ary HQAM constellation

        first_quarter()
        second_quarter()
        third_quarter()
        fourth_quarter()
        plt.title("Regular 16-ary HQAM ")
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