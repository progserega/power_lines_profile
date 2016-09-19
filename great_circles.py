#!/usr/bin/env python
# -*- coding: utf-8 -*-


# ---------------------------------------------------------------------------
# great-circles.py
# Расчет длины большого круга и начального азимута используя полное уравнение.
# More info: http://gis-lab.info/qa/great-circles.html
# Date created: 04.07.2010
# Last updated: 11.08.2010
# ---------------------------------------------------------------------------

import math

#def coord2meters(llong1, llat1, llong2, llat2):
def get_dist(llong1, llat1, llong2, llat2):
		#pi - число pi, rad - радиус сферы (Земли)
		rad = 6372795

		#координаты двух точек
		#llat1 = 77.1539
		#llong1 = -120.398
		#llat1 = 43.17724
		#llong1 = 132.04543

		#llat2 = 77.1804
		#llong2 = 129.55
		#llat2 = 43.17838
		#llong2 = 132.04658

		#в радианах
		lat1 = llat1*math.pi/180.
		lat2 = llat2*math.pi/180.
		long1 = llong1*math.pi/180.
		long2 = llong2*math.pi/180.

		#косинусы и синусы широт и разницы долгот
		cl1 = math.cos(lat1)
		cl2 = math.cos(lat2)
		sl1 = math.sin(lat1)
		sl2 = math.sin(lat2)
		delta = long2 - long1
		cdelta = math.cos(delta)
		sdelta = math.sin(delta)

		#вычисления длины большого круга
		y = math.sqrt(math.pow(cl2*sdelta,2)+math.pow(cl1*sl2-sl1*cl2*cdelta,2))
		x = sl1*sl2+cl1*cl2*cdelta
		ad = math.atan2(y,x)
		dist = ad*rad

		#вычисление начального азимута
		x = (cl1*sl2) - (sl1*cl2*cdelta)
		y = sdelta*cl2
		z = math.degrees(math.atan(-y/x))

		if (x < 0):
			z = z+180.

		z2 = (z+180.) % 360. - 180.
		z2 = - math.radians(z2)
		anglerad2 = z2 - ((2*math.pi)*math.floor((z2/(2*math.pi))) )
		angledeg = (anglerad2*180.)/math.pi

		#print 'Distance >> %.0f' % dist, ' [meters]'
		#print 'Initial bearing >> ', angledeg, '[degrees]'
		return dist
