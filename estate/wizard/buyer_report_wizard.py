from odoo import models, fields, api, _
from odoo.exceptions import *



class BuyerReportWizard(models.TransientModel):
    _name = "buyer.report.wizard"
    _description = "Generate buyer report"


    report_type = fields.Selection(
        selection=[('buyer', 'Buyer '), ('seller', 'Seller ')], string='Report For',default='buyer',required=True)
    property_id = fields.Many2one('estate.property')
    buyer_id = fields.Many2many("res.partner", string="Buyer", copy=False)
    user_id = fields.Many2many("res.users", string=' Seller', copy=False)
    buyer_all = fields.Boolean(string='Select All Buyer')
    seller_all = fields.Boolean(string='Select all Seller')
    tag = fields.Many2one('estate.property.tag',string='Tag',copy=False)
    type_id = fields.Many2one('estate.property',related='property_id.property_type_id',  string='Type')
    type = fields.Many2one('estate.property.type', copy=False, string='Type')
    report_ver = fields.Selection([('pdf', 'PDF'), ('xlsx', 'Excel')],default='pdf', string='Report Type',required = True)



    def action_xls_report(self):


        if self.report_type == 'seller':
            domain = []
            user_id = self.user_id
            if user_id:
                domain += [('user_id', '=', user_id.ids)]
            type = self.type
            if type:
                domain += [('property_type_id','=',type.id)]

            tag = self.tag
            if tag:
                domain += [('tag_ids', '=', tag.id)]




            info = self.env['estate.property'].search(domain)
            # info_tag = self.env['estate.property.tag'].search(domain)
            lst = []
            for i in info:
                vals = {
                    # 'user_id': i.user_id,
                    'user_name': i.user_id.name,
                    'name': i.name,
                    'selling_price': i.selling_price,
                    # 'buyer': i.buyer_id.name,
                    'expected_price': i.expected_price,
                    'type': i.property_type_id.name,
                    'offers': i.offer_ids,
                    'invoice': i.move_id.name,
                    'tag': i.tag_ids.name,
                    'payment': i.move_id.payment_state,

                    # 'tag':i.tag_ids.name,


                }
                lst.append(vals)

            data = {
                'info': lst
            }

            report_action = self.env.ref('estate.action_report_seller_report_wizard_xlsx').report_action(self,
                                                                                                         data=data)
            return report_action

        else:
            domain = []
            buyer_id = self.buyer_id
            if buyer_id:
                domain += [('buyer_id', '=', buyer_id.ids)]
            type = self.type
            if type:
                domain += [('property_type_id', '=', type.id)]
            tag = self.tag
            if tag:
                domain += [('tag_ids', '=', tag.id)]

            info = self.env['estate.property'].search(domain)
            lst = []
            for i in info:
                vals = {
                    # 'user_id': i.user_id,
                    'user_name': i.buyer_id.name,
                    'name': i.name,
                    'selling_price': i.selling_price,
                    # 'Seller': i.user_id.name,
                    'expected_price': i.expected_price,
                    'type': i.property_type_id.name,
                    'invoice': i.move_id.name,
                    'tag':i.tag_ids.name,
                    'payment': i.move_id.payment_state,

                }
                lst.append(vals)
            data = {
                'info': lst
            }

            report_action = self.env.ref('estate.action_report_seller_report_wizard_xlsx').report_action(self,
                                                                                                         data=data)
            return report_action

    def action_print_report(self):

        # if self.report_type not in ['buyer','seller'] or self.report_ver not in ['pdf','xlsx']:
        #     raise UserError("Select a proper type report!!Please")

        if self.report_ver == 'xlsx':
            return self.action_xls_report()

        else:
            if self.report_type == 'buyer':
                domain = []
                buyer_id = self.buyer_id
                if buyer_id:
                    domain += [('buyer_id', '=', buyer_id.ids)]
                type = self.type
                if type:
                    domain += [('property_type_id', '=', type.id)]

                tag = self.tag
                if tag:
                    domain += [('tag_ids', '=', tag.id)]


                info = self.env['estate.property'].search(domain)
                # account_info = self.env['account.move'].search(domain)

                lst = []

                for i in info :

                    vals = {
                        'buyer_id': i.buyer_id,
                        'user_name': i.buyer_id.name,
                        'name': i.name,
                        'selling_price': i.selling_price,
                        'type': i.property_type_id.name,
                        'invoice': i.move_id.name,
                        'payment': i.move_id.payment_state,
                        'tag': i.tag_ids.name,
                        # 'tag':tag_list
                        # for t in i.tag_ids:
                        #     'self.tag': t.tag_ids.name,





                    }
                    lst.append(vals)
                # for i in account_info:
                #     vals = {
                #         'num': i.payment_id,
                #     }
                #     lst.append(vals)




                data = {
                    # 'form_data': self.read(tag)[0],
                    'info': lst
                }
                if lst:
                    report_action = self.env.ref('estate.action_report_buyer_report_wizard').report_action(self,
                                                                                                           data=data)
                    return report_action
                else:
                    report_action = self.env.ref('estate.action_report_buyer_report_wizard').report_action(self,
                                                                                                           data=data)
                    return report_action


            else:
                domain = []
                user_id = self.user_id
                if user_id:
                    domain += [('user_id', '=', user_id.ids)]
                type = self.type
                if type:
                    domain += [('property_type_id', '=', type.id)]

                tag = self.tag
                if tag:
                    domain += [('tag_ids', '=', tag.id)]

                info = self.env['estate.property'].search(domain)
                lst = []
                for i in info:
                    vals = {
                        'user_id': i.user_id,
                        'user_name': i.user_id.name,
                        'name': i.name,
                        'selling_price': i.selling_price,
                        'type':i.property_type_id.name,
                        'invoice': i.move_id.name,
                        'payment': i.move_id.payment_state,
                        'tag': i.tag_ids.name,

                    }
                    lst.append(vals)
                if not lst:
                    return True


                data = {

                    'info': lst
                }

                if lst:
                    report_action = self.env.ref('estate.action_report_seller_report_wizard').report_action(self,
                                                                                                            data=data)
                    return report_action
                else:
                    report_action = self.env.ref('estate.action_report_seller_report_wizard').report_action(self,
                                                                                                            data=data)
                    return report_action












