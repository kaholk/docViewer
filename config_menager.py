import configparser


class ConfigManager:
    def __init__(self, config_file="config.ini"):
        self.config_file = config_file
        self.config = configparser.ConfigParser()
        self.config.optionxform = str
        self.default_values = self.set_default_values()
        self.load_config()

    def set_default_values(self):
        """Ustawia domyślne wartości konfiguracji."""
        return {
            ("App", "PositionX"): "100",
            ("App", "PositionY"): "100",
            ("App", "Width"): "800",
            ("App", "Height"): "600",
            ("App", "Fullscreen"): "true",
            ("App", "SplitterSections"): 1,
        }

    def load_config(self):
        """Wczytuje plik konfiguracyjny."""
        self.config.read(self.config_file)

    def get(self, section, option, convert_to=str):
        """Pobiera wartość z pliku konfiguracyjnego, uwzględniając wartości domyślne i konwersję."""
        value = self.config.get(section, option, fallback=self.default_values.get((section, option), None))
        try:
            return convert_to(value)
        except (ValueError, TypeError):
            print(f"Błąd konwersji wartości '{value}' na {convert_to.__name__}")
            return None

    def set(self, section, option, value):
        """Ustawia wartość w pliku konfiguracyjnym."""
        if section not in self.config:
            self.config[section] = {}
        self.config[section][option] = value
        self.save_config()

    def save_config(self):
        """Zapisuje zmiany w pliku konfiguracyjnym."""
        with open(self.config_file, "w", encoding="utf-8") as configfile:
            self.config.write(configfile)


appConfig = ConfigManager()
