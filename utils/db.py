"""
    Database scripts
    2023 Juan Luis Ruiz Vanegas (juanluisruiz971@gmail.com)
"""

import subprocess


class DatabaseScripts():

    def save_file_to_server(FILEPATH):
        subprocess.run(["scp", FILEPATH, "omar@192.1268.0.100:/path/to/foo"])