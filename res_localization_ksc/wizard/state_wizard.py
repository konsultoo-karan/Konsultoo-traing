from odoo import fields, models

class Statewizard(models.TransientModel):
    _name = 'ksc.state.wizard'
    _description = 'Bulk Customer Label Print Report'

    name = fields.Char(string="Name", required=True)

    def print_report(self):
        print('\n active_id::::::',self.env.context)
        state = self.env[self.env.context['active_model']].browse(self.env.context['active_id'])
        data = {
            'active_model':self.env.context['active_model'],
            'active_id':self.env.context['active_id'],
            'docs': state,
            'name':self.name,
            'layout_wizard': self.id,
        }

        print('print report')

        # report_action = self.env.ref('res_localization_ksc.action_report_state').report_action(docids=state, data=data)
        return self.env.ref('res_localization_ksc.action_report_stat_wizard').report_action(docids=state, data=data)

class StateWizardAbstract(models.AbstractModel):
    _name = 'report.res_localization_ksc.report_state_wizard_ksc'
    _description = 'State Report'

    def _get_report_values(self, docids, data):
        print(self.env.context)

        state = self.env[self.env.context['active_model']].browse(self.env.context['active_id'])
        print("\n\n\n 'number' : data.get('number'),", data.get('name'))
        return {
            'active_model': 'res.state.ksc',
            'active_id': self.env.context['active_id'],
            'name': data.get('name'),
            'docs': state,
        }


