# import arrow
# brewing_time = arrow.utcnow()
# brewing_time.to('Europe/London')

from collections import namedtuple

ChaiOrder = namedtuple('ChaiOrder', ['type', 'size', 'sugar'])
print(f"Chai order namedtuple: {ChaiOrder(type='Masala Chai', size='Large', sugar=2)}")