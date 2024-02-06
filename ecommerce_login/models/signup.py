from odoo import api, models

class MyModel(models.Model):
    _name = 'sign.up'

    def action_redirect_to_template(self):
        return {
            'name': 'My Template',
            'type': 'ir.actions.act_url',
            'url': '/web#id=%s&view_type=form&model=sign.up&menu_id=complete_your_profile' % self.id,
            'target': 'self',
        }
