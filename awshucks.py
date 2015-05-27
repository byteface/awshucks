from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import random
import time


def awshucks():
    us = 'u'
    while True:
        print('f{0}ck'.format(us))
        new_us = random.choice(range(1, 4))
        wait_time = random.choice(range(3))
        brand_new_us = 'u'.join(['' for _ in range(new_us)])
        us = '{0}{1}'.format(us, brand_new_us)
        time.sleep(wait_time)


if __name__ == '__main__':
    awshucks()
