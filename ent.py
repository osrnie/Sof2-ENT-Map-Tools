from Points import *


def toEnt(arr, **properties):
	pts = ''
	txt = ''
	for name, value in properties.items():
		pts += (f'\"{name}\" \"{value}\"\n')
	
	for i in range(len(arr)):
		txt += (f'{{\n'
						f'{pts}'
						f'\"origin\" {arr[i].toString()}\n'
						f'}}\n')
		
	return txt
	
