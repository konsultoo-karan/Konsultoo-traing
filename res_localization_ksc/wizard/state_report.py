from odoo import fields, models


class StateReportViewWizard(models.TransientModel):
    _name = 'ksc.state.wizard'
    _description = 'State Report view wizard'

    name = fields.Char(string="Name")

    def print_report(self):
        state = self.env[self.env.context['active_model']].browse(self.env.context['active_id'])

        data = {
            'active_model': self.env.context['active_model'],
            'active_id': self.env.context['active_id'],
            'docs': state,
            'name': self.name,
            'layout_wizard': self.id,
        }
        report_action = self.env.ref('res_localization_ksc.action_report_state').report_action(docids=state, data=data)
        return self.env.ref('res_localization_ksc.action_report_state').report_action(docids=state, data=data)

    class ReportStateReport(models.AbstractModel):
        _name = 'report.res_localization_ksc.report_state_action_template'
        _description = 'State Report'
        def _get_report_values(self, docids, data):
             if self.env.context['active_id']:
                state = self.env['res.state.ksc'].browse(self.env.context['active_id'])
            # print("\n\n\n'number': data.get('number'),", data.get('name'))
                return {
                    'active_model': 'res.state.ksc',
                    'active_id': self.env.context['active_id'],
                        'name': data.get('name'),
                    'docs': state,
                }
