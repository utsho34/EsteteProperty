from odoo import models, fields, api, _
from odoo.exceptions import *



class CustomReportWizard(models.TransientModel):
    _name = "custom.report.wizard"
    _description = "Generate custom report"

    col_no = fields.Integer()
    row_no = fields.Integer()
    #
    # def action_print_report(self):
    #     return
    #
    #



