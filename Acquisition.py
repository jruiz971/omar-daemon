"""Signal acquisition code through RTLSDR devices using a python wrapper (pyrtlsdr)

    2023 Juan Luis Ruiz Vanegas (juanluisruiz971@gmail.com)
"""

from typing import Tuple

from rtlsdr import RtlSdr
import numpy as np
import sys
import os.path
from datetime import datetime
from pathlib import Path
import configparser


class Acquisition():

    def __init__(self):
        self.sdr = RtlSdr()

    def read_config(self):
        self.config = configparser.ConfigParser()
        self.config.read('config.ini')

        self.station = self.config['STATION']['ID']

        self.sdr.center_freq = self.config['SPECTRUM']['CENTER_FREQ']
        self.sdr.sample_rate = self.config['SPECTRUM']['SAMPLE_RATE']
        self.sdr.freq_correction = self.config['SPECTRUM']['FREQ_CORRECTION']
        self.sdr.gain = self.config['SPECTRUM']['GAIN']
        self.sdr.num_samples = self.config['SPECTRUM']['SAMPLES']

    def read_samples(self):
        samples = self.sdr.read_samples(self.sdr.num_samples)
        self.samples = samples.astype(np.complex64)

        self.datetime_ = datetime.now()

    def save_samples(self):
        date_ = datetime.today()

        PATH = str(self.station) + '/' + str(date_.year) + '/' + str(
            date_.month) + '/' + str(date_.day) + str(date_.hour) + str(
                date_.minute) + str(date_.second)

        Path(PATH).mkdir(parents=True, exist_ok=True)

        FILENAME = 'number_samples:' + \
        str(self.sdr.num_samples)+"-center_freq:"+str(self.sdr.center_freq)+'_Mhz.iq'

        self.FILEPATH = os.path.join(PATH, FILENAME)

        self.samples.tofile(self.FILEPATH)
