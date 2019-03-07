import csv
import sys

with open( sys.argv[1], 'r') as csvfile :
	
	#Check given CSV file is well-formed
	try :
		dialect = csv.Sniffer().sniff(csvfile.read(), delimiters=',')
		csvfile.seek(0)
	except :
		print("CSV is not well-formed")
		exit(1)			
			
			
	rdr = csv.reader(csvfile, dialect)
	
	Nth_column = []
	
	N = int(sys.argv[2])
	
	for row in rdr:
	
		#Check column number N is out of the valid range
		if N >len(row) or N <= 0:
			print( "Column number N is out of valid range" )
			exit(1)
		
		Nth_column.append( row[N-1] )
			
	csvfile.close
	
	for i in Nth_column :
		print(i)
	
	exit(0)
	
