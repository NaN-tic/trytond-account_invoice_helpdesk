# This file is part of the invoice_helpdesk module for Tryton.
# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
from trytond.pool import Pool
from .configuration import *
from .helpdesk import *
from .getmail import *

def register():
    Pool.register(
        HelpdeskConfiguration,
        Helpdesk,
        InvoiceHelpdesk,
        GetmailServer,
        module='account_invoice_helpdesk', type_='model')
