from odoo import models


class PartnerXlsx(models.AbstractModel):
    _name = 'report.ica_elearning.report_ica_course'
    _inherit = 'report.report_xlsx.abstract'

    def generate_xlsx_report(self, workbook, data, partners):
        for obj in partners:
            report_name = obj.name
            sheet = workbook.add_worksheet(report_name)
            bold = workbook.add_format({'bold': True})
            sheet.write(0, 0, obj.name, bold)
            x, y = 2, 0
            headers = ['Course', 'Fees']
            for header in headers:
                sheet.write(x, y, header)
                y += 1
            x += 1
            y = 0
            for enrollment_id in obj.enrollment_ids:
                sheet.write(x, y, enrollment_id.course_id.name)
                sheet.write(x, y + 1, enrollment_id.fees)
                x += 1
            sheet.write(x, y, 'Total')
            sheet.write(x, y + 1, f'=sum(B{x - (len(obj.enrollment_ids)-1)}:B{x})')
