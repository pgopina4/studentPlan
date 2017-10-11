# # import excel library
import xlrd
import os
DEBUG = 12

# Paths
script_dir = os.path.dirname(os.path.abspath(__file__))
print(script_dir)
rel_path_xl="term2outcome.xlsx"
rel_path_op="Output.py"

xl_path = os.path.join(script_dir,rel_path_xl)
py_path =os.path.join(script_dir,rel_path_op)
#Global variables
# Opens the excel sheet.
book = xlrd.open_workbook(xl_path) 
# Name of the Excel sheet.
FirstSheet = book.sheet_by_name('Sheet1')
firstChapter = 0
### Variables####:
# Writes the output by getting the text path.
output = open(py_path,'w') 
 # It gives the number of rows in the excel sheet.
nrows = FirstSheet.nrows
# Creating a list and taking from the XL.
optionsOfOutput = ["OLD", "NOW"]

# Read each line
# if line has first column then say data_
# if line has second column then start a new chapter list
# if line has third column that is neither OLD or new add it to the list
for i in range(nrows):
	string_read = FirstSheet.row_values(i,0,4)
	if DEBUG>=10:
		print(string_read)
	# if Grade
	if string_read[0]!="":
		firstChapter=1
		if i==0:
			output.write('data_'+string_read[0]+'=[')
		else:
			output.write(']]]\ndata_'+string_read[0]+'=[')
	# if Chapter
	elif string_read[1]!="":
		if firstChapter:
			firstChapter=0
			output.write('["'+string_read[1]+'",[')
		else:
			output.write(']],["'+string_read[1]+'",[')			
	# if Outcome/Goal
	elif string_read[2]!="":
		if not string_read[2] in optionsOfOutput:
			output.write('["'+string_read[2]+'",'+'"'+string_read[3]+'"],')
output.write(']]]')
