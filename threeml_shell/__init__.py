# -*- coding: utf-8 -*-

"""Top-level package for 3ML shell tools."""

__author__ = """J. Michael Burgess"""
__email__ = 'jburgess@mpe.mpg.de'


from .utils.configuration import threeml_shell_config, show_configuration
from .utils.logging import update_logging_level, activate_warnings, silence_warnings
