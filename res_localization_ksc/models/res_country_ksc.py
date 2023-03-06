from odoo import fields,models

class ResLocalizationKsc(models.Model):
    _name = "res.country.ksc"
    _description = "Preset to create journal localization model "

    name = fields.Char(string="Name of Country")
    code = fields.Char(string="short code of country")
    states_ids = fields.One2many('res.state.ksc','country_id' , string="states")

    _sql_constraints = [
        ('unique_code', 'unique(code)', 'The country code must be unique!')
    ]

