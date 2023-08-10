import logging
# from opencensus.ext.azure.log_exporter import AzureEventHandler

logger = logging.getLogger(__name__)

# Para ver estos datos de registro en Azure Monitor.
# Puede especificar una variable de entorno, APPLICATIONINSIGHTS_CONNECTION_STRING.
# También puede pasar connection_string directamente a AzureEventHandler, pero las cadenas de conexión no deben agregarse al control de versiones.
# Automática
# logger.addHandler(AzureEventHandler())
#
# Manual
# logger.addHandler(AzureEventHandler(connection_string=<appinsights-connection-string>))

# También puede agregar propiedades personalizadas a sus mensajes de registro
#  en el extraargumento de palabra clave usando el custom_dimensionscampo.
# Estas propiedades aparecen como pares clave-valor en customDimensionsAzure Monitor.


logger.setLevel(logging.INFO)
logger.info('Hello, World!')
