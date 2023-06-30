from datetime import datetime
now = datetime.now()
print(f'{now}')
print(f'{now:%d}')
print(f'{now:%d-%m-%Y }')
print(f'{now:%d-%m-%Y  %H:%M:%S}')
print(f'{now:%H:%M}')
