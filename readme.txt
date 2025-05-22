
####################################################
#Informacje
####################################################
- Po pierwszym uruchomieniu aplikacja utworzy plik konfiguracyjny jeśli nie istnieje
- należy skonfigurować patrz poniżej "config.ini":
    - Host
    - User
    - Password
    - Database
    - CompanyName
    - Path

- Minimalne wymagania do uruchomienia skompilowanej aplikacji: 
    Windows 10 (1809 lub nowszego)

####################################################
#config.ini
####################################################
[App] #podstawowa koniguracja aplikacji
PositionX = "100" #domyślna pozycja okna
PositionY = "100" #domyślna pozycja okna
Width = "800" #domyślna szerokość okna
Height = "600" #domyślna wysokość okna
Fullscreen = "false" #Czy aplikacja ma zostać uruchomiona w trubie pełnoekranowym | Wartości: "true" / "false"
SplitterSections = "2" #czy aplikacja ma uruchomić się domyślnie z 1 lub 2 panelami | Wartości: "1" / "2"
ShowPopUpOnStart = "true" #Czy aplikacja ma domyślnie wyśetlić popup do pobiewrania zlecenia | Wartości: "true" / "false"
PdfViewMode = "single" #domyslnie po załadowaniu pdfa wysetla pojedyńcze strony lub wszystkie w jednym widoku | Wartości: "single" / "all"
AutoSelectFirstDocumentation = "true" #Domyślnie wybiera pierwszy dokument po kliknięciu np. "LC", "RYS" | Wartości: "true" / "false"
AutoSelectCategoryPanel1 = "LC" #Domyślne wybranie kategori po załadowaniu dokumentacji dla lewego panelu | Wartości: "None" / "LC" / "RYS" / "IP" / "PIJ" / "SP" / "OTHER"
AutoSelectCategoryPanel2 = "LC" #Domyślne wybranie kategori po załadowaniu dokumentacji dla prawego panelu | Wartości: "None" / "LC" / "RYS" / "IP" / "PIJ" / "SP" / "OTHER"

[Database] #konfiguracja bazy danych
Driver = "mssql+pymssql" #ustawienie silnika/sterownika do połączenia z baza danych | Wartości: "mssql+pymssql" / "mysql+pymysql"
Host = "DB_IP_ADDRESS" #adres ip bazy danych
User = "DB_USER_NAME" #nazwa użytkownika bayz dancyh. W przypadku AD "Domena\uzytkownik"
Password = "DB_PASSWORD" #hasło bazy danych
Database = "DB_NAME" #nazwa bazy

[BC] #konfiguracja firmy
CompanyName = "CompanyName" #nazwa firmy z która ma łączyć się aplikacja
ExtensionBaseApplication = "437dbf0e-84ff-417a-965d-ed2bb9650972" #domyślne rozszerzenie - wykorzystywane do nazwy tabel

[Documentation] #konfiguracja ścieżki gdzie aplikacja ma szukać plików z dokumentacją
Path = "DOCUMENTATION_PATH" #ścieżka do folderu z dokumentacja np. "N":/folder1/folder2"



####################################################
#uruchomienie kodu źródłowego
####################################################
- instalacja python 3.12
- instalacja venv "pip install virtualenv"
- instalacja git
- przygotowanie folderu z kodem źródłowym "https://github.com/kaholk/docViewer
- "git submodule init"
- "git submodule update"
- utworzenie i aktywacja venv
    - "python -m venv env"
    - ".\.venv\Scripts\activate.ps1" lub ".\.venv\Scripts\activate.bat"
- instalacja wymaganych pakietów "pip install -r requirements.txt"


####################################################
#Kompilacja kodu źródłowego
####################################################
"pyinstaller --noconfirm --noconsole --name docViewer docViewer.py"