from odoo import fields, models, api, _
from docx import Document
from docxtpl import DocxTemplate,InlineImage
import jinja2
import tempfile
from PyPDF2 import PdfFileMerger
from odoo.exceptions import UserError
import io
import os
import base64

class ResPartner(models.Model):
    _inherit = 'res.partner'

    profession = fields.Selection([('individual', 'An Individual'), ('student', 'A Student'), ('company', 'A Company'), ('library','A Material Library'), ('project','Starting a new project')], string='Profession')
    about_us = fields.Selection([('engine', 'Search engine'), ('instagram', 'Instagram'), ('linkedin', 'Linkedin'), ('word','Word of Mouth'), ('events','Events'), ('newspaper', 'Newspaper/ Press'),('other','Other')], string='About Us')


    def generateTempFile(self):
        tf = tempfile.NamedTemporaryFile(mode='w+', delete=False)
        temp_file_name = tf.name
        folder = tempfile.gettempdir()
        tf.close()
        return { 'name': temp_file_name, 'folder': folder }  
    
    def createDocumentMDNA(self, partner_id, data):
        folder = 'Templates'
        template_name = "mnda.docx"
        folder_id = self.env['documents.folder'].search([ ('name', '=', folder)])
        docs = self.env['documents.document'].search( [('folder_id', '=', folder_id.id), ('name', '=', template_name)])
        merger = PdfFileMerger()
        for doc in docs:
            output = io.BytesIO()
            output.write(doc.raw)
            output.seek(0)

            temp_file = self.generateTempFile()
                       
            temp_file_name = temp_file.get('name')
			
            outfile = open(temp_file_name, "wb+")
            outfile.write(output.getbuffer())
            outfile.close()
			
            dic = {}
            template_render = self.template_renderer(temp_file, dic)
            temp_file_name_pdf = template_render['name'] + ".pdf"

            os_cmd = os.system("soffice --headless --convert-to pdf --outdir %s %s" % (template_render['folder'], template_render['name']) )
            merger.append(temp_file_name_pdf, import_bookmarks=False)
            
        myio = io.BytesIO()
        merger.write(myio)
        merger.close()
        myio.seek(0)
        
        byte_str = myio.read()
        fileAscii = base64.b64encode(byte_str).decode('ASCII')
        folder_id = self.env['documents.folder'].search([ ('name', '=', 'MDNA')])
        self.env['documents.document'].create ({
            'name': 'mdna.pdf',
            'partner_id': partner_id.id,
            'datas': fileAscii,
            'type': 'binary',
            'mimetype': 'application/pdf',
            'folder_id': folder_id.id
        })
    
    def template_renderer(self, docTemplate, dataTemplate, field_not_found = False):
        docTemplate_new =self.generateTempFile()
        jinja_env = jinja2.Environment(autoescape=True)
        tpl = DocxTemplate(docTemplate['name'])
        try:
            tpl.render(dataTemplate, jinja_env)
            tpl.save(docTemplate_new['name'])
        except Exception as e:
            ods = self._context.get('active_id')
            ods_id = self.env['service.order'].browse(ods)
            new_field = e.message.split(' ')[0].replace("'","")
            if (field_not_found == new_field):
                raise UserError (_("Campo %s no encontrado" % ( new_field )))
            dataTemplate[new_field] = getattr(ods_id, new_field, None)
            return self.template_renderer(docTemplate, dataTemplate, new_field)
        return docTemplate_new