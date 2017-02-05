#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
	Repeat values for the ONE simulator setting files.
'''

def main():
	l = range(1, 14)
	nrof_runs = 2 			# nrof runs for each

	list_repeat  = list()

	for item in l:
	    for i in range(nrof_runs):
	        list_repeat.append(str(item))

	s = '[' + '; '.join(list_repeat) + ']'

	print(s)

if __name__ == '__main__':
	main()