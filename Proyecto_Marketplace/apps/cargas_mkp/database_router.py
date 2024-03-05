from .models import *

class AuthRouterModlelDB:   

    #route_app_labels = {'auth', 'admin', 'sessions', 'messages'}

    def db_for_read(self, model, **hints):
        """Point all operations on auth models to 'DB_TiendaVirtual' db."""
        if (model == CatOfertasmarketplace):
            return 'DB_TiendaVirtual'
        return None
