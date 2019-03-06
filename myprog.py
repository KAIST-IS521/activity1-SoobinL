import csv
import sys

with open( sys.argv[1], 'r') as csv_file :

	rdr = csv.reader(csv_file, delimiter=',')
	Nth_column = []
	
	#Check given CSV file is well-formed
	
	N = int(sys.argv[2])
	
	for row in rdr:
	
		#Check column number N is out of the valid range
		if len(row) < N :
			print( "N is out of valid range" )
			exit(1)
		
		Nth_column.append( row[N-1] )
			
		
	csv_file.close
	print( Nth_column )
	
	exit(0)
	
