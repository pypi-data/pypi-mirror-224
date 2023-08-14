"""Typesense Server Wrapper
"""

import contextlib
import pathlib
import shutil
import stat
import subprocess

import typesense_server_wrapper_alpha as ts_alpha
import typesense_server_wrapper_omega as ts_omega


def get_path():
    """Get Typesense Server path."""
    init_path = pathlib.Path(__file__)
    bin_path = (init_path.parent / 'typesense-server').resolve()

    if not bin_path.exists():
        alpha_path = ts_alpha.get_path()

        with alpha_path.open('rb') as reader, bin_path.open('wb') as writer:
            shutil.copyfileobj(reader, writer)

        omega_path = ts_omega.get_path()

        with omega_path.open('rb') as reader, bin_path.open('ab') as writer:
            shutil.copyfileobj(reader, writer)

        bin_path.chmod(bin_path.stat().st_mode | stat.S_IEXEC)

    return bin_path


@contextlib.contextmanager
def run(*typesense_server_args, **proc_args):
    """Run Typesense Server

    :param list typesense_server_args: list of arguments for Typesense Server
    :param dict proc_args: dict of subprocess.Popen arguments
    """
    bin_path = str(get_path())
    proc = subprocess.Popen([bin_path, *typesense_server_args], **proc_args)
    with proc:
        yield proc
        proc.terminate()


__title__ = 'typesense-server-wrapper'
__version__ = '0.3.0'
__author__ = 'Grant Jenks'
__license__ = 'Apache 2.0'
__copyright__ = '2023, Grant Jenks'
