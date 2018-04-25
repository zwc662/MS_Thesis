file_name = open('runtime', 'r')
lines = file_name.readline()
data_lines = []
for line in lines:
	if line is not '':
		print line
		print line.split('&')
		data_lines.append(line.split('&'))
data = []
for data_line in data_lines:
	data.append([])
	for data_str in data_line:
		if data_str is not '\n':
			data[-1].append(float(data_str))

