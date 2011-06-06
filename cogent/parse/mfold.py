#!/usr/bin/env python

from cogent.parse.ct import ct_parser

__author__ = "Shandy Wikman"
__copyright__ = "Copyright 2007-2011, The Cogent Project"
__contributors__ = ["Shandy Wikman"]
__license__ = "GPL"
__version__ = "1.5.1"
__maintainer__ = "Shandy Wikman"
__email__ = "ens01svn@cs.umu.se"
__status__ = "Development"

def mfold_parser(lines=None):
    """Parser for Mfold output"""
    result = ct_parser(lines)
    return result
    
    
