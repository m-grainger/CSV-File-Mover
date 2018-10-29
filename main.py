import csv
import os
import shutil
import sys

old_servers = ["01","02","03","04","05"]
new_servers = ["06","07","08","09"]

def read_csv(server_num,cd_drive):
	dupe_list = []
	if not os.path.exists(f"{os.getcwd()}/BadDates"):
		os.makedirs(f"{os.getcwd()}/BadDates")
	if not os.path.exists(f"{os.getcwd()}/Holding"):
		os.makedirs(f"{os.getcwd()}/Holding")

	with open (full_path, newline='') as csvfile:
		row_reader = csv.reader(csvfile, delimiter=',', quotechar='|')
		file_list = []
		for column in row_reader:
			# note that this is pulling from the second column of the report.
			# there MUST be data in the first column for this tool to work!
			new_column = column[1].replace("\\","/").replace('"', "").replace("'", "")
			file_list.append(f"{cd_drive}/earinbox{server_num}/{new_column}")

	count = 1
	for f in file_list:
		shutil.copy(f,f"{os.getcwd()}/Holding")
		x = os.listdir(f"{os.getcwd()}/Holding")
		for num, filename in enumerate(x, start= 1):
			print(f"File Number: {count}")
			fname, ext = filename, ''
			if '.' in filename:
				print(f"File Name: {fname}")
				fname, ext = filename.split('.')   
				shutil.move(f"{os.getcwd()}\\Holding\\{fname}.eml",f"{os.getcwd()}/BadDates")
				os.rename(f"{os.getcwd()}\\BadDates\\{fname}.eml", f"{os.getcwd()}\\BadDates\\{fname}_{count}.{ext}")
		count += 1

if __name__ == "__main__":
	server_num = input("Which server is this data located on? (e.g. 07): " )
	csv_name = input("What is the name of the CSV File? (e.g. BadDate-1-100000):  " )
	full_path = f"{os.getcwd()}/{csv_name}.csv"
	if server_num in old_servers:
		cd_drive = "E:"
	elif server_num in new_servers:
		cd_drive = "D:"		
	else:
		print("Invalid server name, please restart the application.")
		sys.exit()

read_csv(server_num,cd_drive)
os.rmdir(f"{os.getcwd()}/Holding")
