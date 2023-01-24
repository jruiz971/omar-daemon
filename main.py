"""Signal acquisition code through RTLSDR devices using a python wrapper (pyrtlsdr)

    2023 Juan Luis Ruiz Vanegas (juanluisruiz971@gmail.com)
"""

from Acquisition import Acquisition

if __name__ == '__main__':
    acquisition = Acquisition()

    acquisition.read_config()
    acquisition.read_samples()
    acquisition.save_samples()