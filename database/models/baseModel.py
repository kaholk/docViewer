from sqlalchemy.orm import DeclarativeBase


class BaseModel(DeclarativeBase):
    '''Base model for all database models.'''
    
    
    def to_dict(self):
        """Convert the model to a dictionary."""
        return {key: self.__getattribute__(key) for key in self.__annotations__}
    
    def translations(self):
        """Return the translations for this model."""
        return self.metadata.info.get('translations', {})
    
    def caption(self):
        """Return the captions for this model."""
        return self.translations.get('pl', 'no translation')