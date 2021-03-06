#-------------------------------------------------------------------------------
#
#  data files
#
# Author: Martin Paces <martin.paces@eox.at>
#
#-------------------------------------------------------------------------------
# Copyright (C) 2014 EOX IT Services GmbH
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies of this Software or works derived from this Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
#-------------------------------------------------------------------------------

from os.path import dirname, join

_DIRNAME = dirname(__file__)

# magnetic models
WMM_2015 = join(_DIRNAME, 'WMM2015v2.COF')
WMM_2020 = join(_DIRNAME, 'WMM2020.COF')
EMM_2010_STATIC = join(_DIRNAME, 'EMM-720_V3p0_static.cof')
EMM_2010_SECVAR = join(_DIRNAME, 'EMM-720_V3p0_secvar.cof')
EMM_2017_STATIC = join(_DIRNAME, 'EMM2017.COF')
EMM_2017_SECVAR = join(_DIRNAME, 'EMM2017SV.COF')
CHAOS6_CORE_X8 = join(_DIRNAME, 'CHAOS-6-x8_core.shc')
CHAOS6_CORE_LATEST = CHAOS6_CORE_X8
CHAOS6_STATIC = join(_DIRNAME, 'CHAOS-6_static.shc')
CHAOS7_CORE = join(_DIRNAME, 'CHAOS-7.2_core.shc')
CHAOS7_CORE_LATEST = CHAOS7_CORE
CHAOS7_STATIC = join(_DIRNAME, 'CHAOS-7.2_static.shc')
IGRF11 = join(_DIRNAME, 'igrf11coeffs.txt')
IGRF12 = join(_DIRNAME, 'IGRF12.shc')
IGRF13 = join(_DIRNAME, 'igrf13.COF')
SIFM = join(_DIRNAME, 'SIFM.shc')
LCS1 = join(_DIRNAME, 'LCS-1.shc')
MF7 = join(_DIRNAME, 'MF7.shc')
DIFI3 = join(_DIRNAME, 'SW_OPER_MIO_SHAi2D_20131201T000000_20170129T235959_0301.txt')
DIFI4 = join(_DIRNAME, 'SW_OPER_MIO_SHAi2D_20131201T000000_20171231T235959_0401.txt')

# magnetic models used by the apex point calculation
APEX_2015 = join(_DIRNAME, 'apexsh_1995-2015.txt')
APEX_2020 = join(_DIRNAME, 'apexsh_1980-2020.txt')
APEX = APEX_2020
