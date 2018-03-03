#
# linter.py
# Linter for SublimeLinter3, a code checking framework for Sublime Text 3
#
# Written by Dmitry Tsoy
# Copyright (c) 2013 Dmitry Tsoy
#
# License: MIT
#

"""This module exports the Phpcs plugin class."""

from SublimeLinter.lint import Linter


class Phpcs(Linter):
    """Provides an interface to phpcs."""

    syntax = ('php', 'html', 'html 5')
    cmd = ('phpcs', '--report=checkstyle', '--stdin-path=${file}', '-')
    regex = (
        r'.*line="(?P<line>\d+)" '
        r'column="(?P<col>\d+)" '
        r'severity="(?:(?P<error>error)|(?P<warning>warning))" '
        r'message="(?P<message>.*)" source'
    )
    defaults = {
        '--standard=': 'PSR2',
    }
