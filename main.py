import easytrader

user = easytrader.use('yh')
user.prepare('yh.json')
print(user.position)
print(user.entrust)
