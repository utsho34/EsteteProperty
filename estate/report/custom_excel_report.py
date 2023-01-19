from . import models, fields


class CustomReportWizard(models.AbstractModel):
    _name = 'report.generate_custom_Report'
    _inherit = 'report.report_xlsx.abstract'


    def generate_xlsx_report(self, workbook, data,info ):

        sheet = workbook.add_worksheet('info')
        bold = workbook.add_format({'bold': True})
        row = 9
        col = 2
        count =0