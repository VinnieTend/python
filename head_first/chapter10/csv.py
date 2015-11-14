with open('PaceData.csv') as paces:
		column_headings=paces.readline().strip().split(',')
		row_label=row.pop(0)
