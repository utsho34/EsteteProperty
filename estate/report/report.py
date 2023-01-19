from odoo import models
import base64
import io


class BuyerReportWizardXLS(models.AbstractModel):
    _name = 'report.estate.report_seller_report_wizard_xlsx'
    _inherit = 'report.report_xlsx.abstract'


    def generate_xlsx_report(self, workbook, data,info ):

        sheet = workbook.add_worksheet('info')
        bold = workbook.add_format({'bold': True})
        row = 9
        col = 2
        count =0

        sheet.write(row, col+1, 'Name', bold)
        sheet.write(row, col + 2, 'Property', bold)
        sheet.write(row, col + 3, 'Selling Price', bold)
        # sheet.write(row,col+4,'Buyer',bold)
        sheet.write(row, col + 5, 'Expected price', bold)
        sheet.write(row,col+7,'Type',bold)
        sheet.write(row,col+9,'Invoice',bold)
        sheet.write(row,col+11,'Tag',bold)
        sheet.write(row,col+12,'Payment',bold)
        for i in data['info']:
            row += 2
            count+=1
            sheet.write(row,col,count)
            sheet.write(row, col+1, i['user_name'])
            sheet.write(row, col + 2, i['name'])
            sheet.write(row, col + 3, i['selling_price'])
            # sheet.write(row, col + 4, i['buyer'], bold)
            sheet.write(row, col + 5, i['expected_price'])
            sheet.write(row,col+7,i['type'])
            sheet.write(row,col+9,i['invoice'])
            sheet.write(row,col+11,i['tag'])
            sheet.write(row,col+12,i['payment'])
