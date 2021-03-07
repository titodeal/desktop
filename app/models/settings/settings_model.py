from PySide6 import QtCore


class SettingsModel(QtCore.QSettings):
    def __init__(self):
        organization = "TiToD"
        app_name = "TiToD"
        super().__init__(organization, app_name)
