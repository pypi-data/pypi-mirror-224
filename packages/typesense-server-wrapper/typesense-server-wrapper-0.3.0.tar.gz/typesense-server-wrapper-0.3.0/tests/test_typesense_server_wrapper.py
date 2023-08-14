"""Test Python wrapper for Typesense Server"""
import os
import shutil
import time

import typesense_server_wrapper


def test_title():
    assert typesense_server_wrapper.__title__ == 'typesense-server-wrapper'


def test_run():
    shutil.rmtree('data', ignore_errors=True)
    os.mkdir('data')
    args = ['--api-key', 'abc', '--data-dir', 'data']
    with typesense_server_wrapper.run(*args):
        time.sleep(10)
