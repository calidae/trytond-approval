# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
from trytond.pool import Pool
import approval

def register():
    Pool.register(
        approval.Group,
        approval.GroupUser,
        approval.Request,
        module='approval', type_='model')
