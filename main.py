import easytrader

user = easytrader.use('yh_client')
user.prepare('yh_client.json')
print(user.position)
print(user.entrust)
