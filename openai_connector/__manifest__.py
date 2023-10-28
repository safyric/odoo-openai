# -*- coding: utf-8 -*-
# Copyright (C) 2022 - Myrrkel (https://github.com/myrrkel).
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).
{
    'name': 'OpenAI Connector',
    'version': '12.0.0.0',
    'author': 'Myrrkel',
    'website': 'https://github.com/myrrkel',
    'summary': "Connector for OpenAI API",
    'license': 'AGPL-3',
    'depends': [
        'base',
        'mail',
    ],
    'category': 'OpenAI',
    'data': [
        'security/ir.model.access.csv',
        'security/security.xml',
        'views/res_config_settings_views.xml',
        'views/openai_completion_views.xml',
        'views/openai_completion_result_views.xml',
        'views/openai_edit_views.xml',
        'views/openai_edit_result_views.xml',
        'views/openai_image_views.xml',
        'views/openai_image_result_views.xml',
    ],
    'auto_install': False,
    'installable': True,
}
