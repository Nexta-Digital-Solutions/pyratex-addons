# -*- coding: utf-8 -*-

from . import controllers
from . import models

from odoo import api, SUPERUSER_ID
import os
import base64

def  post_init_hook (cr, registry):
    env = api.Environment(cr, SUPERUSER_ID, {})
    folder = 'templates'
    template_name = "mldna.docx"
    path_template = "%s/templates/%s" % (os.path.dirname(__file__), template_name)
    folder_id = env['documents.folder'].search([ ('name', '=', folder)])
    if (not folder_id):
        folder_id = env['documents.folder'].create({
            'name': folder
        })
    env['documents.folder'].create({
            'name': 'mldna'
    })  
    
    docs = env['documents.document'].search( [('folder_id', '=', folder_id.id), ('name', '=', template_name)], limit = 1)
    if (not docs):
        outfile = open(path_template, "rb")
        data_file = outfile.read()
        outfile.close()
        
        fileAscii = base64.b64encode(data_file).decode('ASCII')
        folder_id = env['documents.folder'].search([ ('name', '=', folder)], limit = 1)
        env['documents.document'].create ({
            'name': 'mldna.docx',
            'datas': fileAscii,
            'type': 'binary',
            'mimetype': 'application/msword',
            'folder_id': folder_id.id
        })