# -*- coding: utf-8 -*-
# © 2016 Akretion (Alexis de Lattre <alexis.delattre@akretion.com>)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'Purchase Reports Py3o',
    'version': '10.0.1.0.0',
    'category': 'Purchases',
    'license': 'AGPL-3',
    'summary': 'Sample py3o purchase reports',
    'description': """
Purchase Reports Py3o
=====================

This module adds a sample py3o purchase reports.

This module has been written by Alexis de Lattre from Akretion
<alexis.delattre@akretion.com>.
    """,
    'author': 'Akretion',
    'depends': [
        'report_py3o',
        'purchase_commercial_partner',
        'base_company_extension',
        'base_usability',  # to have res_partner.name_title
        'purchase_usability',
        'account_payment_partner',
        ],
    'data': ['report.xml'],
    'installable': True,
}
