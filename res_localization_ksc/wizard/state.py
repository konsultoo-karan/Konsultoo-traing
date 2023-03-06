# -*- coding: utf-8 -*-

from odoo import fields, models


class StateWizard(models.TransientModel):
    _name = 'state.wizard'
    _description = 'State Print Report'

    name = fields.Char(string="Name", required=True)

    def print_report(self):
        state = self.env[self.env.context['active_model']].browse(self.env.context['active_id'])

        data = {
            'active_model': self.env.context['active_model'],
            'active_id': self.env.context['active_id'],
            'docs': state,
            'name': self.name,
            'layout_wizard': self.id,
        }
        print("print_report")
        report_action = self.env.ref('res_localization_ksc.res_state_id_1').report_action(docids=state, data=data)
        return self.env.ref('res_localization_ksc.res_state_id_1').report_action(docids=state, data=data)


class ReportStateReport(models.AbstractModel):
    _name = 'report.res_localization_ksc.report_action_wizard_1'
    _description = 'State Report'

    def _get_report_values(self, docids, data):
        state = self.env['res.state.ksc'].browse(self.env.context['active_id'])
        print("\n\n\n'number': data.get('number'),", data.get('name'))
        return {
            'active_model': 'res.state.ksc',
            'active_id': self.env.context['active_id'],
            'name': data.get('name'),
            'docs': state,
        }