from .panier import Panier


def panier(request):
    return {'cart': Panier(request)}

