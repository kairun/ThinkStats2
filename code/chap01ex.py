"""This file contains code for use with "Think Stats",
by Allen B. Downey, available from greenteapress.com

Copyright 2014 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
"""

from __future__ import print_function

import os
import numpy as np
import sys

import nsfg
import thinkstats2


def main(script):
    """Tests the functions in this module.

    script: string script name
    """
    resps = readRespondentFile('2002FemResp.dct', '2002FemResp.dat.gz')
    pregs = readRespondentFile('2002FemPreg.dct', '2002FemPreg.dat.gz')

    if validate(resps, pregs) is True:
        print('Everything is ok')
    else:
        print('Someting is wrongk')

def readRespondentFile(dct_file_path, dat_file_path):
    path = os.path.dirname(os.path.abspath(__file__))
    dct_file = path + '/' + dct_file_path
    dat_file = path + '/' + dat_file_path
    dct = thinkstats2.ReadStataDct(dct_file)
    resps = dct.ReadFixedWidth(dat_file, compression="gzip")

    return resps

def validate(resps, pregs):
    pregMap = nsfg.MakePregMap(pregs)

    for i, respPregnum in resps.pregnum.items():
        caseId = resps['caseid'][i]
        indices = pregMap[caseId]

        if len(indices) != respPregnum:
            return False

    return True

if __name__ == '__main__':
    main(sys.argv[0])
