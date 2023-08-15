import sys, os

sys.path.append(os.getcwd() + '/..')

from brickscout.api import BrickScoutAPI


api = BrickScoutAPI(username='brickstarbelgium', password='Planten11$')

# order = api.orders.get('406c2bfa-1bc1-40ae-9b25-8e6e13ee3205')
order = api.orders.get('4d4f7a2f-dd78-42ab-a209-6ad6d13fa75a')

print(vars(order.payment))