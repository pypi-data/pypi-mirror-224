import logging
# from opencensus.ext.azure.log_exporter import AzureLogHandler

logger = logging.getLogger(__name__)

# Para ver estos datos de registro en Azure Monitor.
# Puede especificar una variable de entorno, APPLICATIONINSIGHTS_CONNECTION_STRING. 
# También puede pasar connection_string directamente a AzureLogHandler, pero las cadenas de conexión no deben agregarse al control de versiones.
# Automática
#logger.addHandler(AzureLogHandler())
#
# Manual
# logger.addHandler(AzureLogHandler(connection_string=<appinsights-connection-string>))

# También puede agregar propiedades personalizadas a sus mensajes de registro
#  en el extraargumento de palabra clave usando el custom_dimensionscampo.
# Estas propiedades aparecen como pares clave-valor en customDimensionsAzure Monitor.
properties = {'custom_dimensions': {'key_1': 'value_1', 'key_2': 'value_2'}}


def main():
    """Generate random log data."""

    for num in range(5):
        logger.warning(f"Log Entry - {num}", extra=properties)


if __name__ == "__main__":
    main()
