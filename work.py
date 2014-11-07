# This file is part project_reference_product module for Tryton.
# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.
from trytond.pool import PoolMeta

__all__ = ['Work']
__metaclass__ = PoolMeta


class Work:
    __name__ = 'project.work'

    @classmethod
    def _get_reference(cls):
        models = super(Work, cls)._get_reference()
        models.append('product.template')
        models.append('product.product')
        return models
