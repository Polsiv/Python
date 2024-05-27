import jwt
import datetime

iat =  datetime.datetime.now() + datetime.timedelta(seconds=)
test = int(iat.timestamp())
token = jwt.encode({'user': 'silv', 'exp': test}, 'b7a078fb25f842b788adc528e1f59e29')  

print(token)

print(jwt.decode(token, 'b7a078fb25f842b788adc528e1f59e29', algorithms=['HS256']))