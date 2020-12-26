supermarket={
'store1':{'name':'durga general store',
	'items':[{'name':'soap','quantity':20},
			 {'name':'brush','quantity':10},
			 {'name':'pen','quantity':30}
			]
		 },
		   
'store2':{'name':'sunny book store',
	'items':[{'name':'python','quantity':100},
			 {'name':'django','quantity':200},
			 {'name':'java','quantity':300}
	  ]
		}
		}	
for d in (supermarket['store2']['items']):
	if d['name']=='django':
		print(d['quantity'])