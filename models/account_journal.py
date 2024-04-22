# -*- coding: utf-8 -*-
from odoo import models, fields, api, _


class AccountJournal(models.Model):
    _inherit = "account.journal"

    account_journal_type = fields.Selection([('a', 'A'), ('b', 'B')], string="Type de journal")
