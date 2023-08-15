#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# Copyright (C) 2022 Xiaolong Yang - All Rights Reserved
#----------------------------------------------------------------------------
# Created By  : Xiaolong Yang
# Created Date: 2022/09/22
# version ='1.0'
# ---------------------------------------------------------------------------


# =================================
# all package import from set
# ---------------------------------
# 0-level function: two antenna correlation, grd-grd, grd-sat, sat-sat
# =================================



# for embedding python in CPP
# =================================
import numpy as np
import copy
import datetime

from astropy              import units     as u
from astropy.time         import Time
from astropy.coordinates  import *
from astropy.io           import fits
from astropy              import wcs

from poliastro.bodies     import Moon, Earth, Sun
from poliastro.twobody    import Orbit

from skyfield             import api as sfapi
from skyfield             import positionlib as sfpos



from utils.ant import *
from utils.sat import *
from utils.orb import orbit_sat
from utils.orb import orbit_obj




sched     = schedule(grdant=grt, sat=sat, epoch=epoch, src=src, timerange=timerange, timeinterval=timerange / 1000)



def satGCRS():
  # X_sat: sat to obj G(Object)CRS (no unit, default is km)
  # X_obj: obj to Earth GCRS (no unit, default is km)
  # X_sat_earth: sat to Earth GCRS (no unit, default is km)
  X_sat, Y_sat, Z_sat = orbit_sat(sched)
  X_obj, Y_obj, Z_obj = orbit_obj(sched)
  
  X_sat = X_sat * u.km
  Y_sat = Y_sat * u.km
  Z_sat = Z_sat * u.km
  
  X_obj = X_obj * u.km
  Y_obj = Y_obj * u.km
  Z_obj = Z_obj * u.km
  
  X_sat_earth, Y_sat_earth, Z_sat_earth = X_sat+X_obj, Y_sat+Y_obj, Z_sat+Z_obj
  
  return 