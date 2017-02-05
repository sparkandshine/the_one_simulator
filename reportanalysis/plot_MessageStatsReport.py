#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Plot a figure from a batch of MessageStatsReports
'''

import matplotlib.pyplot as plt

def read_files(filenames, metric):
	"""
		Read values with a given metric from a batch of files.
		Return a list of values
	"""
	result = list()

	for filename in filenames:
		with open(filename, 'r') as f:
			for line in f:
				if line.startswith(metric):
					value = float(line.strip().split(':')[1])
					result.append(value)
					break
		
	return result


def main():
	# Step 1: Read files
	# Get filenames
	list_message_intervals = range(1, 14)
	filenames = ['WithXOR-CDSD-TH-3-{interval}_20_MessageBroadcastStatsReport.txt'.format(interval=interval)
					for interval in list_message_intervals]

	print(filenames)

	# Read files
	metric = 'delivered'
	list_delivered = read_files(filenames, metric)
	# [47670.0, 49541.0, 50944.0, 52538.0, 53841.0, 55770.0, 57245.0, 58479.0, 58269.0, 58095.0, 58257.0, 61098.0, 62986.0]

	print(list_delivered)

	# Step 2: Plot figures
	x = list_message_intervals
	y = list_delivered

	fig, ax = plt.subplots()
	ax.plot(x, y, 'r-o', label='With NC', linewidth=2,
					markeredgewidth=1, markerfacecolor='white', markersize=8)

	# Decoration
	plt.ticklabel_format(style='sci', axis='y', scilimits=(0,0))
	plt.grid()

	plt.xlabel(r'The message creation period $\Delta$', fontsize=15)
	plt.ylabel('The number of messages delivered', fontsize=15)

	ax.legend(loc='best')
	plt.xticks(x, x)
	plt.xlim(min(x), max(x))

	out_file = 'delivered.png'
	plt.savefig(out_file)
	plt.show()

	return

if __name__ == '__main__':
	main()


