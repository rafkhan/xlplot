from flask import render_template

class XlMap:

	def __init__(self, points=[]):
		self.coords = []
		self.add_point_set(points)

	def add_point(self, lat, lng):
		self.coords.append((lat, lng))

	def add_point_set(self, points):
		for p in points:
			self.add_point(p["lat"], p["lng"])

	def make_html(self):
		pass
