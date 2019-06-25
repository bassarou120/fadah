
from .models import Category

def shop(request):
	return {'categories': Category.objects.all()}
 

