# This file is part account_invoice_helpdesk module for Tryton.
# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.
from trytond.model import fields
from trytond.pool import PoolMeta

__all__ = ['HelpdeskConfiguration']


class HelpdeskConfiguration:
    __metaclass__ = PoolMeta
    __name__ = 'helpdesk.configuration'
    smtp_invoice = fields.Many2One('smtp.server', 'SMTP Invoice Server')
