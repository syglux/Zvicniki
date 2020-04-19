import fileinput
import sys
import re
import itertools
from math import ceil
file = sys.argv[1]
name = sys.argv[2]

# print(re.findall("* Start Frequency:", fileinput.input()))
with open("{}.js".format(name), "w") as o:
	with open(file) as f:
		lines = f.readlines()
		

		# if float(lines[42].split()[0])>20:
		# 	start = 41
		# elif float(lines[63].split()[0])>20:
		# 	start = 62
		# elif float(lines[64].split()[0])>20:
		# 	start = 63
		# print(start)

		# if float(lines[54601].split()[0])>20000:
		# 	end = 54601
		# elif float(lines[54623].split()[0])>20000:
		# 	end = 54623
		# print(end)


		# a = itertools.islice(f, start, 9700, 1)
		# b = itertools.islice(f, 0, end, 500)
		a = lines[14:401:1]
		b = lines[9701:54571+1:500]
		c = lines[401:9701:20]


		o.write("var {} = [\n".format(name))
		
		for i in a:
			i = i.split()
			o.write("{{ x: {}, y: {} }},\n".format(i[0], i[1]))
		for k in c:
			k = k.split()
			o.write("{{ x: {}, y: {} }},\n".format(k[0], k[1]))
		for j in b:
			j = j.split()
			o.write("{{ x: {}, y: {} }},\n".format(j[0], j[1]))
		o.write("];\n".format(name))

		o.write("var {}_phase = [\n".format(name))
		
		for i in a:
			i = i.split()
			# print("{{ x: {}, y: {} }},\n".format(i[0], i[1]))
			o.write("{{ x: {}, y: {} }},\n".format(i[0], i[2]))
		for k in c:
			k = k.split()
			o.write("{{ x: {}, y: {} }},\n".format(k[0], k[2]))
		for j in b:
			j = j.split()
			o.write("{{ x: {}, y: {} }},\n".format(j[0], j[2]))
		o.write("];\n".format(name))




