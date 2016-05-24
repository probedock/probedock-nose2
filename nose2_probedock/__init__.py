#!/usr/bin/env python

"""
This is a nose2 plugin for reporting with Probe Dock
"""

import logging
from unittest import FunctionTestCase

import re
import time

from nose2 import util
from nose2.events import Plugin

from probedock import ProbeDockReporter, REMOVE_PARENTHESIS_REGEX


__author__ = "Benjamin Schubert <ben.c.schubert@gmail.com>"


log = logging.getLogger('nose2.plugins.probedock')


class Nose2ProbeDockTestResult(ProbeDockReporter):
    """
    This is a wrapper for the ProbeDockReporter to enable accurate information to be extracted from the tests
    """
    def _is_test_function(self, test):
        """ determines whether the test run is in a class or is only a function """
        return issubclass(test.__class__, FunctionTestCase)

    def _get_test_module(self, test):
        """ gets the module in which the test is located """
        if self._is_test_function(test):
            return self._get_test_namespace(test)
        return super(Nose2ProbeDockTestResult, self)._get_test_module(test)

    def _get_test_class(self, test):
        """ gets the class of the test if it has one """
        if self._is_test_function(test):
            return None
        return super(Nose2ProbeDockTestResult, self)._get_test_class(test)

    def _get_test_method(self, test):
        """ gets the method name of the test """
        if self._is_test_function(test):
            return re.sub(REMOVE_PARENTHESIS_REGEX, "", str(test)).split(" ")[1]
        return super(Nose2ProbeDockTestResult, self)._get_test_method(test)

    def _get_test_namespace(self, test):
        """ gets the namespace in which the test is run """
        if self._is_test_function(test):
            return re.sub(r"\.transplant_class.*", "", re.sub(REMOVE_PARENTHESIS_REGEX, "", str(test)).split(" ")[0])
        return super(Nose2ProbeDockTestResult, self)._get_test_namespace(test)


class ProbedockPlugin(Plugin):
    """
    Nose2 plugin for Probe Dock
    """
    commandLineSwitch = ("P", 'probedock', 'Turn on probedock reporting')
    reporter = Nose2ProbeDockTestResult(category="nose2")

    _start_time = None

    def startTest(self, event):
        """ records time when the test starts """
        self._start_time = event.startTime

    def reportSuccess(self, event):
        """ reports a test that succeeded """
        self.reporter.addSuccess(event.testEvent.test, self._time())

    def reportError(self, event):
        """ reports a test that ended up with an error """
        self.reporter.addError(event.testEvent.test, self._time(), self._get_traceback(event))

    def reportFailure(self, event):
        """ reports a test that failed """
        self.reporter.addFailure(event.testEvent.test, self._time(), self._get_traceback(event))

    def reportSkip(self, event):
        """ reports a test that was skipped """
        self.reporter.addSkip(event.testEvent.test, self._time(), event.testEvent.reason)

    def reportExpectedFailure(self, event):
        """ reports a test that was expected to fail and did fail """
        self.reporter.addExpectedFailure(event.testEvent.test, self._time(), self._get_traceback(event))

    def reportUnexpectedSuccess(self, event):
        """ reports a test that should have failed but didn't """
        self.reporter.addUnexpectedSuccess(event.testEvent.test, self._time())

    def afterTestRun(self, event):
        """ sends the report to the Probe Dock server """
        self.reporter.send_report(event.timeTaken)

    def _get_traceback(self, event):
        """ extracts the traceback from the test """
        return util.exc_info_to_string(event.testEvent.exc_info, event.testEvent.test)

    def _time(self):
        """ gets the time passed since the start of the test """
        return time.time() - self._start_time
