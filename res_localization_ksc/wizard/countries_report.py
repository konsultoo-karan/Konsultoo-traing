# -*- coding: utf-8 -*-

from odoo import fields, models


class CountrykscWizard(models.TransientModel):
    _name = 'country.ksc.wizard'
    _description = 'country Label Print Report'

    name = fields.Char(string=" Country Name", required=True)
    code=fields.Integer(string="Code")


    def print_report(self):
        # print('::::::::::::::lllllll: ',self.env.context)
        country = self.env[self.env.context['active_model']].browse(self.env.context['active_id'])
        # print("Country",country)

        data = {
            'active_model': self.env.context['active_model'],
            'active_id': self.env.context['active_id'],
            'docs': country,
            'name': self.name,
            'layout_wizard': self.id,
            'form_data':self.read()[0],
            'country':country
        }
        print("print_report")
        # report_action = self.env.ref('res_localization_ksc.res_country_ksc_of_report_2').report_action(docids=country, data=data)
        # report_action.update({'close_on_report_download': True})
        return self.env.ref('res_localization_ksc.res_country_ksc_of_report_2').report_action(docids=country, data=data)

class ReportcountryReport(models.AbstractModel):
    _name = 'report.res_localization_ksc.report_country_ksc_2'
    _description = 'Country Report'

    def _get_report_values(self, docids, data):
        country = self.env['res.country.ksc'].browse(self.env.context['active_id'])
        print("\n\n\n'number': data.get('number'),", data.get('name'))
        return {
            'active_model': 'res.country.ksc',
            'active_id': self.env.context['active_id'],
            'name': data.get('name'),
            'docs': country,

        }



#
#

