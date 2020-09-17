# -*- coding: utf-8 -*-
"""

@author: Adrien Wehrlé, GEUS (Geological Survey of Denmark and Greenland)

"""


from scipy.optimize import rosen, minimize 

sol=minimize(rosen,np.zeros(2,), method='Nelder-Mead')