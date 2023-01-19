from odoo import models
import base64
import io


class CustomReportXlsx(models.AbstractModel):
    _name = 'report.estate.report_custom_report_xlsx'
    _inherit = 'report.report_xlsx.abstract'

    def generate_xlsx_report(self, workbook, data, info):
        sheet = workbook.add_worksheet('Custom Report')
        bold = workbook.add_format({'bold': True})

        row = 4
        col = 3
        # for j in info:
        #     col+=2
        #     sheet.write(row,col,j[row])
        for i in data['info']:
            row+=2
            sheet.write(row,col,i['user_name'])

