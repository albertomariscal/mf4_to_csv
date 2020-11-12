# mf4_to_csv
Converter from MF4 to CSV file with need from a DBC file

	Function created by Alberto Mariscal from the original file from Martin Falch
	See https://github.com/CSS-Electronics/dashboard-writer

	The function will take as inputs:
		-DBC name
		-MF4 File name
	Both files have to be in the same path as the file where python script is being executed.
	No arguments will be returned.
	The function will write a csv file in the same path and with the same name as the MF4 file. 

	List of necessary packages to run this script:
		-pandas: pip install pandas
		-numpy: pip install numpy
		-mdf-iter: pip install mdf-iter
		-canedge-browser: pip install canedge-browser
		-can-decoder: pip install can-decoder
		-canmatrix: pip install canmatrix
		-yaml: pip install pyyaml
		-xlsxwriter: pip install xlsxwriter
		-xlrd: pip install xlrd
		-lxml: pip install lxml
		-xlwt: pip install xlwt

	Python 3.8.3 - Some packages may have problems with Python >= 3.9
