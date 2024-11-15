#select randomly 'Who will pay the bill?'

import random

friends = ['Alice' , 'Bob' , 'Margret' , 'Charlie' , 'Danny']

# Method 1
print(random.choice(friends))

#Method 2
random_index = random.randint(0,4)
print(friends[random_index])