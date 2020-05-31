from io import BytesIO

from celery import shared_task
from django.core.cache import cache
from pdfdocument.document import PDFDocument


def generate_pdf(data):
    f = BytesIO()
    pdf = PDFDocument(f)
    pdf.init_report()
    pdf.append(data)
    pdf.generate()
    return pdf


def generate_pdf_to_user(question_id, user_id):
    data = get_question_related_data(question_id)  # this function return all the related question in json format
    pdf = generate_pdf(data)
    return pdf


@shared_task
def pdf_task(question_id, user_id):
    existing_question = cache.get(f"reminder_question_{user_id}")
    if existing_question == question_id:
        pdf = generate_pdf_to_user(question_id, user_id)
        send_pdf_to_email(pdf, user_id)  # this function return pdf file to respected user
    else:
        print("New question is asked")
