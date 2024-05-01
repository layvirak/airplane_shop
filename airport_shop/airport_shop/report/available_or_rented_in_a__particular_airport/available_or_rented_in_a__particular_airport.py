# Copyright (c) 2024, Lay Virak and contributors
# For license information, please see license.txt

import frappe


def execute(filters=None):
	columns = [
		{
			"fieldname": "airport",
			"label": "Airport",
			"fieldtype": "int",
            "width": 150
		},
		{
			"fieldname": "not_available",
			"label": "Not Available",
			"fieldtype": "int",
            "width": 150
		},{
			"fieldname": "available",
			"label": "Available",
			"fieldtype": "int",
            "width": 150
		},
		# {
		# 	"fieldname": "total_shop",
		# 	"label": "Total Shop",
		# 	"fieldtype": "int",
        #     "width": 150
		# }
	]
	data = []
	# get airport list
	airport_list = frappe.db.get_list("Airport", {}, ['name'])
	# get shop list
	airport_shop = frappe.db.get_list("Shop", {}, ['airport'])
	# get all the shop
	contract_list = frappe.get_all("Contract",fields=['shop.airport',])

	for i,item in enumerate(airport_list):
		data.append({
						'airport':item.name,
						'total_shop':0,
						'available':0,
						'not_available':0,
					})
		for item_data in airport_shop:
			if item_data['airport']==item['name']:
				data[i]['total_shop']+=1
				
	print('skadsm,sfddsmsjgdknmsfsg',data)
	for item in contract_list:
		
		for index,item_data in enumerate(data):
			print('index',index,item_data)
			if item_data['airport'] == item.airport:
				data[index]['not_available'] += 1
				data[index]['available'] = data[index]['total_shop'] - data[index]['not_available']
			

			
		
	# 	if data != []:
	# 		for item_data in data:
	# 			if item_data['airport'] == item.airport:
	# 				data[item_data]['available'] += 1
	# 	else:
	# 		data.append({
	# 			'airport':item.airport,
	# 			'total_shop':1,
	# 			'available':0,
	# 			'not_available':0,
	# 		})
		
	# get all the 
	# contract_list = frappe.get_list("Contract", fields=["shop"])
	# field report
	# data.append({
	# 	'airport':'',
	# 	'available':0,
	# 	'not_available':0,
	# })
	
	

	return columns, data