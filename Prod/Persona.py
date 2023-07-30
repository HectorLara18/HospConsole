import datetime

class Persona:
    def __init__(self, nombre: str, apellido1: str, apellido2: str, relacion: str, contacto_mail: str, contacto_phone: int):

        """
        :param nombre:
        :param apellido1:
        :param apellido2:
        :param relacion:
        :param contacto_mail:
        :param contacto_phone:
        """

        self._Nombre: str = nombre
        self._Apellido_Paterno: str = apellido1
        self._Apellido_Materno: str = apellido2
        self._Hosp_Relationship: str = relacion
        self._Contact_Mail: str = contacto_mail
        self._contact_Phone: int = contacto_phone

    def __str__(self):
        return f"{self._Nombre} {self._Apellido_Paterno} {self._Apellido_Materno}: {self._Hosp_Relationship}"