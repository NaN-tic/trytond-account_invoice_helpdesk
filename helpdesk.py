# This file is part of the account_invoice_helpdesk module for Tryton.
# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
from trytond.model import ModelSQL, fields
from trytond.pool import PoolMeta
from trytond.pyson import Eval

__all__ = [
    'Helpdesk', 'InvoiceHelpdesk'
    ]
__metaclass__ = PoolMeta


class Helpdesk:
    __name__ = 'helpdesk'
    invoices = fields.Many2Many('invoice.helpdesk', 'helpdesk', 'invoice',
        'Invoices', states={
            'readonly': Eval('state').in_(['cancel', 'done']),
            'invisible': ~Eval('kind').in_(['invoice', 'generic']),
            },
        depends=['state'])

    @classmethod
    def __setup__(cls):
        super(Helpdesk, cls).__setup__()
        value = ('invoice', 'Invoice')
        if not value in cls.kind.selection:
            cls.kind.selection.append(value)


class InvoiceHelpdesk(ModelSQL):
    'Invoice - Helpdesk'
    __name__ = 'invoice.helpdesk'
    _table = 'invoice_invoice_helpdesk_rel'
    invoice = fields.Many2One('account.invoice', 'Invoice', ondelete='CASCADE',
        select=True, required=True)
    helpdesk = fields.Many2One('helpdesk', 'Helpdesk', ondelete='RESTRICT',
        select=True, required=True)
