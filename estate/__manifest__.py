{
    'name': 'RealestatE',
    "category": 'Real Estate/Brokerage',
    'depends': ['base','web','report_xlsx'],

    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',



        'wizard/buyer_report_wizard_view.xml',
        'wizard/custom_report_view.xml',
        "views/estate_property_offer_views.xml",
        "views/estate_property_tag_views.xml",
        "views/estate_property_type_views.xml",
        "views/estate_property_views.xml",

        "views/res_users_views.xml",
        "views/custom_views.xml",
        "views/estate_menus.xml",
        "report/estate_reports.xml",
        "report/estate_report_view.xml",
        'report/estate_property_templates.xml',
        'report/buyer_report_wizard_templates.xml',

    ],
    "demo": [
        "data/estate_demo.xml"
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3'

}
