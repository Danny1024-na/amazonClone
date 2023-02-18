#um dei daten der Firma in eller Webseite zu zeigen
from .models import Company

def getData(request):
    data= Company.objects.first()
    return{'site_data':data}