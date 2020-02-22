# -*- coding: utf-8 -*-
# License Odoo EE.
{
    'name': "Account Invoice Merge Subscription",
    'summary': """Compatibility between Sale Subscriptio and account invoice merge""",
    'author': "Open2Bizz",
    'website': "https://www.open2bizz.tech",
    'category': 'Finance',
    'version': '12.0.1.0.0',
    'depends': [
        'account_invoice_merge',
        'purchase',
	'sale_subscription',
    ],
    'auto_install': True,
    'installable': True,
}
