import configparser
import os

class ConfigManager:
    def __init__(self, config_file="config.ini"):
        self.config_file = config_file
        self.config = configparser.ConfigParser()
        self.config.optionxform = str  # Zachowuje wielkość liter w kluczach
        self.default_values = self.set_default_values()

        # Jeśli plik nie istnieje, ustaw domyślne wartości i zapisz konfigurację
        # if not os.path.exists(self.config_file):
        #     self.apply_default_values()
        #     self.save_config()

        self.load_config()

    def set_default_values(self):
        """Ustawia domyślne wartości konfiguracji."""
        return {
            ("App", "PositionX"): "100",
            ("App", "PositionY"): "100",
            ("App", "Width"): "800",
            ("App", "Height"): "600",
            ("App", "Fullscreen"): "false",
            ("App", "SplitterSections"): "2",
            ("App", "ShowPopUpOnStart"): "true",
            ("App", "PdfViewMode"): "single",
            ("App", "AutoSelectFirstDocumentation"): "true",
            ("App", "AutoSelectCategoryPanel1"): "LC",
            ("App", "AutoSelectCategoryPanel2"): "LC",
            
            
            ("Database", "Driver"): "mssql+pymssql",
            ("Database", "Host"): "DB_IP_ADDRESS",
            ("Database", "User"): "DB_USER_NAME",
            ("Database", "Password"): "DB_PASSWORD",
            ("Database", "Database"): "DB_NAME",
            
            ("BC", "CompanyName"): "BC_COMPANY_NAME",
            ("BC", "ExtensionBaseApplication"): "437dbf0e-84ff-417a-965d-ed2bb9650972",
            
            ("Documentation", "Path"): "DOCUMENTATION_PATH"
        }

    def apply_default_values(self):
        """Dodaje domyślne wartości do obiektu ConfigParser."""
        for (section, option), value in self.default_values.items():
            if section not in self.config:
                self.config[section] = {}
            self.config[section][option] = f'"{value}"'  # Dodanie cudzysłowów

    def load_config(self):
        """Wczytuje plik konfiguracyjny."""
        self.config.read(self.config_file, encoding="utf-8")

    def get(self, section, option, convert_to=str):
        """Pobiera wartość z pliku konfiguracyjnego, usuwając cudzysłowy i konwertując typ."""
        value = self.config.get(section, option, fallback=self.default_values.get((section, option), None))

        if value is not None and value.startswith('"') and value.endswith('"'):
            value = value[1:-1]  # Usunięcie cudzysłowów

        try:
            return convert_to(value)
        except (ValueError, TypeError):
            print(f"Błąd konwersji wartości '{value}' na {convert_to.__name__}")
            return None

    def set(self, section, option, value):
        """Ustawia wartość w pliku konfiguracyjnym, dodając cudzysłowy."""
        if section not in self.config:
            self.config[section] = {}
        self.config[section][option] = f'"{value}"'
        self.save_config()

    def save_config(self):
        """Zapisuje zmiany w pliku konfiguracyjnym, wymuszając cudzysłowy."""
        with open(self.config_file, "w", encoding="utf-8") as configfile:
            self.config.write(configfile)


appConfig = ConfigManager()
