import datedifffile
class Date:
	def __init__(self,date):
		self.date = date

dt1 = Date("11/10/2021")
dt2 = Date("11/10/2022")
print("Difference between two dates is",
	datedifffile.datediff(dt1, dt2))
