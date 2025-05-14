from .baseModel import BaseModel
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .types import types


class RecordLink(BaseModel):
    
    __tablename__ = f"Record Link"
    
    linkId: Mapped[types.PyInteger] = mapped_column("Link ID", types.DbInteger, primary_key=True, nullable=False)
    
    recordId: Mapped[types.PyBinary] = mapped_column("Record ID", types.DbBinary448, nullable=False)
    
    url1: Mapped[types.PyUnicode] = mapped_column("URL1", types.DbUnicode2048, nullable=False)

    url2: Mapped[types.PyUnicode] = mapped_column("URL2", types.DbUnicode250, nullable=False)
    
    url3: Mapped[types.PyUnicode] = mapped_column("URL3", types.DbUnicode250, nullable=False)
    
    url4: Mapped[types.PyUnicode] = mapped_column("URL4", types.DbUnicode250, nullable=False)

    description: Mapped[types.PyUnicode] = mapped_column("Description", types.DbUnicode250, nullable=False)
    
    type: Mapped[types.PyInteger] = mapped_column("Type", types.DbInteger, nullable=False)
    
    note: Mapped[types.PyImage] = mapped_column("Note", types.DbImage, nullable=True)
    
    created: Mapped[types.PyDateTime] = mapped_column("Created", types.DbDateTime, nullable=False)
    
    userId: Mapped[types.PyUnicode] = mapped_column("User ID", types.DbUnicode132, nullable=False)
    
    company: Mapped[types.PyUnicode] = mapped_column("Company", types.DbUnicode30, nullable=False)

    notify: Mapped[types.PyBoolean] = mapped_column("Notify", types.DbBoolean, nullable=False)
    
    toUserId: Mapped[types.PyUnicode] = mapped_column("To User ID", types.DbUnicode132, nullable=False)


    #   ,[$systemId]``
    #   ,[$systemId]``
    #   ,[$systemCreatedAt]
    #   ,[$systemCreatedBy]
    #   ,[$systemModifiedAt]
    #   ,[$systemModifiedBy]