# Pablo Gainza Cirauqui 2016 LPDI IBI STI EPFL
# This pymol plugin for Masif just enables the load ply functions.

from pymol import cmd
from .loadhsPLY import *
from .loadhsDOTS import *
import sys

cmd.extend("loadhsply", load_hs_ply)
cmd.extend('loadhsdots', load_hs_dots)
cmd.extend('loadhsgiface', load_hs_giface)

