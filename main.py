"""Signal acquisition code through RTLSDR devices using a python wrapper (pyrtlsdr)

    2023 Juan Luis Ruiz Vanegas (juanluisruiz971@gmail.com)
"""
from datetime import datetime

from Acquisition import Acquisition
from utils.db import DatabaseScripts


def get_data(acquisition):
    acquisition.read_config()
    acquisition.read_samples()
    acquisition.save_samples()

    execution_time = datetime.now()
    return execution_time


def get_data_same_config(acquisition):
    acquisition.read_samples()
    acquisition.save_samples()

    execution_time = datetime.now()
    return execution_time


if __name__ == '__main__':
    acquisition = Acquisition()

    execution_time = get_data(acquisition)

    if execution_time > datetime.now() + datetime.timedelta(minutes=5):
        execution_time = get_data(acquisition)
    else:
        execution_time = get_data_same_config(acquisition)

    db_manager = DatabaseScripts()
    db_manager.save_file_to_server(acquisition.FILEPATH)

    check_semaforo