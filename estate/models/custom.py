from dateutil.relativedelta import relativedelta
from odoo import api, fields, models
from odoo.exceptions import UserError, ValidationError
from odoo.tools import float_compare, float_is_zero

class Custom(models.Model):
    _name = 'custom.report'
    _description = 'Custom Report Generator'
    _inherit = 'report.report_xlsx.abstract'

    name=fields.Char()

    type = fields.Selection([('buyer','Buyer'),('seller','Seller'),('property','Property Details')])
    description = fields.Boolean(string='Description')
    postcode = fields.Boolean(string='Postcode')
    date_availability = fields.Boolean(string='Date of availability')
    expected_price = fields.Boolean(string='Expected Price')
    selling_price = fields.Boolean(string='Selling Price' )
    bedrooms = fields.Boolean(string='Bedrooms')
    living_area = fields.Boolean(string='Living Area')
    facades = fields.Boolean(string='Facades')
    garden_area = fields.Boolean(string='Garden Area')
    lst = []


    def check_data(self):

        if self.description:
            self.lst.append('description')
        if self.postcode:
            self.lst.append('postcode')
        if self.date_availability:
            self.lst.append('date availability')
        if self.expected_price:
            self.lst.append('expected_price')
        if self.selling_price:
            self.lst.append('selling_price')
        if self.bedrooms:
            self.lst.append('bedrooms')
        if self.living_area:
            self.lst.append('living_area')
        if self.facades:
            self.lst.append('facades')
        if self.garden_area:
            self.lst.append('garden area')

        col = len(self.lst)
        print(self.lst)
        print(col)



    def action_print_report(self):
        if self.type == 'buyer':
            domain=[]
            #
            # user_id = self.user_id
            # if user_id:
            #     domain += [('user_id', '=', user_id.ids)]
            info = self.env['estate.property'].search(domain)
            data_list = []
            # for i in self.lst:
            #     values = {
            #         'row': i.lst,
            #     }
            #     data_list.append(values)

            for i in info:
                values = {
                    'user_name':i.user_id.name,

                }
                data_list.append(values)



        data = {
             # 'rows': self.lst,

             'info': data_list


        }
        self.check_data()
        report_action = self.env.ref('estate.action_report_custom_report_xlx').report_action(self,
                                                                                                data=data)
        return report_action
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





