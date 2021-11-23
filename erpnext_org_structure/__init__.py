# -*- coding: utf-8 -*-
from __future__ import unicode_literals

__version__ = '0.0.1'

import erpnext.accounts.general_ledger
import erpnext_org_structure.api

erpnext.accounts.general_ledger.validate_accounting_period = erpnext_org_structure.api.validate_accounting_period

