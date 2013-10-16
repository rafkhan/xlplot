import xlrd
import datetime

class ExcelReader:

	def __init__(self, f):
		self.xlfile = f
		self.workbook = xlrd.open_workbook(self.xlfile)
		self.worksheets = self.workbook.sheets()


	# Get column(s) in sheet, concatenated
	# when you specify a range
	#
	# si is the sheet #
	# ci can be a tuple or int
	def get_sheet_cols(self, si, ci):
		bounds = self.check_bounds_type(ci)
		values = [] # Values to geocode (the return value)
		sheet = self.worksheets[si]
		num_rows = sheet.nrows - 1
		curr_row = 0

		if type(bounds) == tuple:
			while curr_row < num_rows:
				temp_vals = []
				for i in range(bounds[0], bounds[1] + 1):
					cv = self.cellval(sheet.cell(curr_row, i), self.workbook.datemode)
					temp_vals.append(cv)
				values.append(" ".join(temp_vals))
				curr_row += 1

		if type(bounds) == int:
			while curr_row < num_rows:
				cv = self.cellval(sheet.cell(curr_row, bounds), self.workbook.datemode)
				values.append(cv)
				curr_row += 1

		return values;


	def check_bounds_type(self, ci):
		if type(ci) == tuple:
			if ci[0] < ci[1]:
				return ci
			else:
				raise ValueError("Upper bound is lower than higher bound")

		#
		# TODO: Add list support
		# 

		elif type(ci) == int or type(ci) == float:
			return int(round(ci))
		else:
			raise ValueError("Invalid argument type")

		
	# Creds to: https://classic.scraperwiki.com/docs/python/python_excel_guide/
	#
	# Returns python types of corresponding excel types:
	# - numeric excel dates => python datetime
	# - empty cell => None
	# - excel bool => Boolean
	def cellval(self, cell, datemode):
		if cell.ctype == xlrd.XL_CELL_DATE:
			datetuple = xlrd.xldate_as_tuple(cell.value, datemode)
			if datetuple[3:] == (0, 0, 0):
				return datetime.date(datetuple[0], datetuple[1], datetuple[2])
			else:
				return datetime.date(datetuple[0], datetuple[1], datetuple[2],
						datetuple[3], datetuple[4], datetuple[5])

		elif cell.ctype == xlrd.XL_CELL_EMPTY:
			return "" 

		elif cell.ctype == xlrd.XL_CELL_BOOLEAN:
			return cell.value == 1

		else:
			return cell.value

if __name__ == "__main__":
	xl = ExcelReader("/Users/rafy/Documents/hanen/map plotter/data/excel/LLLI IN CA NO ABC.xlsx")
	print(xl.gsc(0, (1, 3)))
