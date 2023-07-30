import datetime

class Persona:
    def __init__(self, nombre: str, apellido1: str, apellido2: str, relacion: str, contacto_mail: str, contacto_phone: int):
        self._Nombre: str = nombre
        self._Apellido_Paterno: str = apellido1
        self._Apellido_Materno: str = apellido2
        self._Hosp_Relationship: str = relacion
        self._Contact_Mail: str = contacto_mail
        self._contact_Phone: int = contacto_phone

    