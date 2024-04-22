# -*- coding: utf-8 -*-
{
    'name': 'Account filter',
    'version': '1.1',
    'category': 'Accounting/Accounting',
    'sequence': 30,
    'summary': 'filter account journal',
    'description': """
    filter account journal
    """,

    'depends': ['base', 'account', 'account_reports'],
    'data': [
        'views/account_journal.xml'
    ],

    'installable': True,
    'application': True,
    'assets': {
        'web.assets_backend': [
            'account_filter/static/src/components/account_report/filters/filters.xml',
            'account_filter/static/src/components/account_report/filters/filters.js',
            'account_filter/static/src/components/account_report/filters/filter_account_journal.xml'
        ],
    }
}
