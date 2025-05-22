from sqlalchemy import Numeric, Unicode, Integer, DateTime, Boolean, Uuid, TypeDecorator
# from decimal import Decimal
from datetime import datetime
from enum import IntEnum
from typing import Any, Literal, TypedDict, Dict, Union, Generic, TypeVar
from dataclasses import dataclass
from uuid import UUID

# PyNumeric = Decimal
# DbNumeric = Numeric(precision=38, scale=20, asdecimal=True)
PyNumeric = float
DbNumeric = Numeric(precision=38, scale=20, asdecimal=False)

PyDecimal = float
DbDecimal = Numeric(precision=38, scale=20, asdecimal=False)


PyUnicode = str
DbUnicode10 = Unicode(length=10)
DbUnicode20 = Unicode(length=20)
DbUnicode30 = Unicode(length=30)
DbUnicode50 = Unicode(length=50)
DbUnicode100 = Unicode(length=100)
DbUnicode132 = Unicode(length=100)
DbUnicode200 = Unicode(length=200)
DbUnicode250 = Unicode(length=250)
DbUnicode2048 = Unicode(length=2048)

PyBinary = str
DbBinary448 = Unicode(length=500)

PyImage = str
DbImage = Unicode(length=500)

PyInteger = int
DbInteger = Integer()


PyDateTime = datetime
DbDateTime = DateTime()


PyBoolean = bool
DbBoolean = Boolean()


PyUUID = UUID
DbUUID = Uuid


Language = Literal['pl', 'en']
Translations = Dict[Language, str]
DEFAULT_LANGUAGE: Language = 'pl'


class DbIntegerEnum(TypeDecorator):
    impl = DbInteger
    
    cache_ok = True
    
    def __init__(self, enumtype):
        super(DbIntegerEnum, self)
        self._enumtype = enumtype
    
    
    def process_bind_param(self, value, dialect):
        if isinstance(value, self._enumtype):
            return value.value
        elif isinstance(value, int):
            return value
        elif value is None:
            return None
        else:
            raise ValueError(f"Cannot bind parameter of type {type(value)} to {self._enumtype.__name__}")
    
    def process_result_value(self, value , dialect):
        return self._enumtype(value)
    


class TranslatableIntegerEnum(IntEnum):

    def __new__(cls, value: int, translations: Translations):
        obj = int.__new__(cls, value)
        obj._value_ = value
        obj.translations = translations
        return obj

    def __init__(self, value: int, translations: Translations):
        self._value_ = value
        self.translations = translations

    def get_translation(self, lang:Language) -> str:
        return self.translations.get(lang, "brak")

    @property
    def caption(self) -> str:
        return self.get_translation(DEFAULT_LANGUAGE)

    def __str__(self) -> str:
        return self.caption

    @classmethod
    def __missing__(cls, value: int):
        if hasattr(cls, "Undefined"):
            return cls.Undefined
        raise ValueError(f"Value {value} is not a valid {cls.__name__}")



class PyEnumItemLedgerEntryType(TranslatableIntegerEnum):
    Undefined = (-1, {'en': 'Undefined', 'pl': 'Niezdefiniowane'})
    
    Purchase = (0, {'en': 'Purchase', 'pl': 'Zakup'})
    Sale = (1, {'en': 'Sale', 'pl': 'Sprzedaż'})
    PositiveAdjmt = (2, {'en': 'Positive Adjmt.', 'pl': 'Korekta dodatnia'})
    NegativeAdjmt = (3, {'en': 'Negative Adjmt.', 'pl': 'Korekta ujemna'})
    Transfer = (4, {'en': 'Transfer', 'pl': 'Przesunięcie'})
    Consumption = (5, {'en': 'Consumption', 'pl': 'Zużycie'})
    Output = (6, {'en': 'Output', 'pl': 'Wynik'})
    Empty = (7, {'en': ' ', 'pl': ' '})
    AssemblyConsumption = (8, {'en': 'Assembly Consumption', 'pl': 'Zużycie montażowe'})
    AssemblyOutput = (9, {'en': 'Assembly Output', 'pl': 'Wynik montażu'})

    

class PyEnumProductionOrderStatus(TranslatableIntegerEnum):
    Undefined = (-1, {'en': 'Undefined', 'pl': 'Niezdefiniowane'})
    
    Simulated = (0, {'en': 'Simulated', 'pl': 'Symulowane'})
    Planned = (1, {'en': 'Planned', 'pl': 'Planowane'})
    FirmPlanned = (2, {'en': 'Firm Planned', 'pl': 'Potwierdzone'})
    Released = (3, {'en': 'Released', 'pl': 'Zwolnione'})
    Finished = (4, {'en': 'Finished', 'pl': 'Zakończone'})


class PyEnumProductionOrderSourceType(TranslatableIntegerEnum):
    Undefined = (-1, {'en': 'Undefined', 'pl': 'Niezdefiniowane'})
    
    Item = (0, {'en': 'Item', 'pl': 'Zapas'})
    Family = (1, {'en': 'Family', 'pl': 'Rodzina'})
    SalesHeader = (2, {'en': 'Sales Header', 'pl': 'Nagłówek sprzedaży'})


class PyEnumProductionOrderRoutingStatus(TranslatableIntegerEnum):
    Undefined = (-1, {'en': 'Undefined', 'pl': 'Niezdefiniowane'})
    
    Default = (0, {'en': 'Default', 'pl': 'Domyślny'})
    Planned = (1, {'en': 'Planned', 'pl': 'Planowany'})
    InProgress = (2, {'en': 'In Progress', 'pl': 'W toku'})
    Finished = (3, {'en': 'Finished', 'pl': 'Zakończony'})


class PyEnumBomStatus(TranslatableIntegerEnum):
    Undefined = (-1, {'en': 'Undefined', 'pl': 'Niezdefiniowane'})
    
    New = (0, {'en': 'New', 'pl': 'Nowy'})
    Certified = (1, {'en': 'Certified', 'pl': 'Certyfikowany'})
    UnderDevelopment = (2, {'en': 'Under Development', 'pl': 'W trakcie rozwoju'})
    Closed = (3, {'en': 'Closed', 'pl': 'Zamknięty'})


class PyEnumProductionBomLineType(TranslatableIntegerEnum):
    Undefined = (-1, {'en': 'Undefined', 'pl': 'Niezdefiniowane'})
    
    Default = (0, {'en': 'Default', 'pl': 'Domyślny'})
    Item = (1, {'en': 'Item', 'pl': 'Zapas'})
    ProductionBom = (2, {'en': 'Production BOM', 'pl': 'BOM Produkcyjny'})


class PyEnumPurchaseLineType(TranslatableIntegerEnum):
    Undefined = (-1, {'en': 'Undefined', 'pl': 'Niezdefiniowane'})
    
    Comment = (0, {'en': 'Comment', 'pl': 'Komentarz'})
    GeneralLedgerAccount = (1, {'en': 'G/L Account', 'pl': 'Konto K/G'})
    Item = (2, {'en': 'Item', 'pl': 'Zapas'})
    Resource = (3, {'en': 'Resource', 'pl': 'Zasób'})
    FixedAsset = (4, {'en': 'Fixed Asset', 'pl': 'Środek trwały'})
    ChargeItem = (5, {'en': 'Charge (Item)', 'pl': 'Koszt dodatkowy (zapas)'})
    AllocationAccount = (10, {'en': 'Allocation Account', 'pl': 'Konto Alokacji'})