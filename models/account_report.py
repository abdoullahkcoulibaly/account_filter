# -*- coding: utf-8 -*-
from odoo import models, fields, api, _


class AccountReport(models.Model):
    _inherit = 'account.report'

    def _init_options_journals(self, options, previous_options=None, additional_journals_domain=None):
        super()._init_options_journals(options, previous_options, additional_journals_domain)
        options['filter_list'] = []

        for journal_option in options.get('journals', []):
            if journal_option.get('model') == 'account.journal':
                journal_id = journal_option.get('id')
                journal = self.env['account.journal'].browse(journal_id)
                journal_option['account_journal_type'] = journal.account_journal_type

        selection_labels = dict(
            self.env['account.journal'].fields_get('account_journal_type')['account_journal_type']['selection'])
        for key, value in selection_labels.items():
            options['filter_list'].append({
                'id': key,
                'name': value,
            })
