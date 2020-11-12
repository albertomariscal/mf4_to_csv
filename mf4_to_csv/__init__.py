import mdf_iter, canedge_browser, can_decoder
from fsspec.implementations.local import LocalFileSystem
import pandas as pd

def mf42csv_converter(DBC_file, MF4_file):
	"""
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
	"""
	# initialize DBC converter and file loader
	db = can_decoder.load_dbc(DBC_file)
	df_decoder = can_decoder.DataFrameDecoder(db)

	fs = LocalFileSystem()
	signals = []
	res = "1S"

	log_files = [MF4_file]
	print(f"Found a total of {len(log_files)} log files")

	for log_file in log_files:

		# ALM: Creamos un dataframe vacio
		dataframe = pd.DataFrame()
		# open log file, get device_id and extract dataframe with raw CAN data
		with fs.open(log_file, "rb") as handle:
			mdf_file = mdf_iter.MdfFile(handle)
			device_id = mdf_file.get_metadata()["HDComment.Device Information.serial number"]["value_raw"]
			df_raw = mdf_file.get_data_frame()
		# DBC convert the raw CAN dataframe
		df_phys = df_decoder.decode_frame(df_raw)
		if df_phys.empty:
			continue

		print(f"\nExtracted a total of {len(df_phys)} decoded messages")

		# group the data to enable a signal-by-signal loop
		df_phys_grouped = df_phys.groupby("Signal")["Physical Value"]

		# for each signal in your list, resample the data and write to InfluxDB
		for signal, group in df_phys_grouped:
			if signal in signals or len(signals) == 0:
				df_phys_signal = group.to_frame().rename(columns={"Physical Value": signal})
				if res != "":
					df_phys_signal = df_phys_signal.resample(res).pad().dropna()

				if dataframe.empty:
					dataframe = dataframe.append(df_phys_signal)
				else:
					dataframe = dataframe.join(df_phys_signal)
	
	dataframe.to_csv(device_id + '-' + MF4_file.split('.')[0] + '.csv')
	return

