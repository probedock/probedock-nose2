#!/usr/bin/env python

"""
This is tests for Probedock nose2 plugin
"""


import unittest
import time


__author__ = "Benjamin Schubert <ben.c.schubert@gmail.com>"


class Test(unittest.TestCase):
    def test_success(self):
        time.sleep(1)
        self.assertTrue(True)

    def test_failure(self):
        time.sleep(0.2)
        self.assertTrue(False)

    def test_error(self):
        raise Exception()

    @unittest.skip("Not yet implemented")
    def test_skip(self):
        raise Exception()

    @unittest.expectedFailure
    def test_expected_failure(self):
        self.assertTrue(False)

    @unittest.expectedFailure
    def test_unexpected_success(self):
        self.assertTrue(True)


def test_success_function():
    time.sleep(1)
    assert True is True


def test_failure_function():
    time.sleep(0.2)
    assert True is False


def test_error_function():
    raise Exception()


@unittest.skip("Not yet implemented")
def test_skip_function():
    raise Exception()


# FIXME this is not reported correctly
@unittest.expectedFailure
def test_expected_failure_function():
    assert True is False


# FIXME this is not reported correctly
@unittest.expectedFailure
def test_unexpected_success_function():
    assert True is True
