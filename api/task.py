from celery import shared_task
from django.db import transaction
from .models import MusicSheet
import pymupdf 


@shared_task
def generate_thumbnail(pdf_id):
    with transaction.atomic():
        try: 
            pdf = MusicSheet.objects.get(id=pdf_id)
            doc = pymupdf.open(pdf)  
            
            thumb_page = doc.select([0])
            pix = thumb_page.get_pixmap()
            pix.save(pdf.title, output="png")

            return f"Thumbnail generated for {pdf.title}"
        
        except Exception as e:
            return f"Error generating thumbnail: {e}"
    
    
    
