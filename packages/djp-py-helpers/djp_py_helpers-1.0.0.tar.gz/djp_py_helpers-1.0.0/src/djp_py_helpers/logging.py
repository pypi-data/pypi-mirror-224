""" helper functions for configuring python built-in logger. """

# This file is part of djp_py_helpers.
#
# djp_py_helpers is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# djp_py_helpers is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with djp_py_helpers. If not, see <https://www.gnu.org/licenses/>.

import sys
import logging

def configure_logger(log_level = 'DEBUG', log_file_path = None) -> None:
    " basic logging configuration "

    log_format = '%(asctime)s - PID %(process)d - %(levelname)s - %(message)s'
    formatter = logging.Formatter(log_format)

    logger = logging.getLogger()
    logger.setLevel(log_level)

    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    if log_file_path is not None:
        file_handler = logging.FileHandler(log_file_path)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
