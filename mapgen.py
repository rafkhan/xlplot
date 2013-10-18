from flask import render_template

class MapGen:

	def __init__(self):
		self.coords = []

	def add_point(lat, lng):
		self.coords.append((lat, lng))

	def add_point_set(points):
		for p in points:
			self.add_point(p["lat"], p["lng"])
