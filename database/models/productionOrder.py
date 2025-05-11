
from sqlalchemy import ForeignKeyConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .baseModel import BaseModel
from ..utils import constants
from ..types import types


class ProductionOrder(BaseModel):
    '''docstring'''

    __tablename__ = f"{constants.COMPANY_NAME}$Production Order${constants.EXTENSIONS['Base Application']}"

    timestamp: Mapped[types.PyDateTime] = mapped_column(
        f"timestamp",
        types.DbDateTime,
        primary_key=False,
        nullable=False,
        info={
            "translations": {
                "pl": "timestamp",
                "en": "timestamp",
            }
        }
    )
    '''docstring'''

    status: Mapped[types.PyInteger] = mapped_column(
        f"Status",
        types.DbInteger,
        primary_key=True,
        nullable=False,
        info={
            "translations": {
                "pl": "status",
                "en": "status",
            }
        }
    )
    '''docstring'''

    no: Mapped[types.PyUnicode] = mapped_column(
        f"No_",
        types.DbUnicode20,
        primary_key=True,
        nullable=False,
        info={
            "translations": {
                "pl": "no",
                "en": "no",
            }
        }
    )
    '''docstring'''

    description: Mapped[types.PyUnicode] = mapped_column(
        f"Description",
        types.DbUnicode100,
        primary_key=False,
        nullable=False,
        info={
            "translations": {
                "pl": "description",
                "en": "description",
            }
        }
    )
    '''docstring'''

    searchDescription: Mapped[types.PyUnicode] = mapped_column(
        f"Search Description",
        types.DbUnicode100,
        primary_key=False,
        nullable=False,
        info={
            "translations": {
                "pl": "searchDescription",
                "en": "searchDescription",
            }
        }
    )
    '''docstring'''

    description2: Mapped[types.PyUnicode] = mapped_column(
        f"Description 2",
        types.DbUnicode50,
        primary_key=False,
        nullable=False,
        info={
            "translations": {
                "pl": "description2",
                "en": "description2",
            }
        }
    )
    '''docstring'''

    creationDate: Mapped[types.PyDateTime] = mapped_column(
        f"Creation Date",
        types.DbDateTime,
        primary_key=False,
        nullable=False,
        info={
            "translations": {
                "pl": "creationDate",
                "en": "creationDate",
            }
        }
    )
    '''docstring'''

    lastDateModified: Mapped[types.PyDateTime] = mapped_column(
        f"Last Date Modified",
        types.DbDateTime,
        primary_key=False,
        nullable=False,
        info={
            "translations": {
                "pl": "lastDateModified",
                "en": "lastDateModified",
            }
        }
    )
    '''docstring'''

    sourceType: Mapped[types.PyInteger] = mapped_column(
        f"Source Type",
        types.DbInteger,
        primary_key=False,
        nullable=False,
        info={
            "translations": {
                "pl": "sourceType",
                "en": "sourceType",
            }
        }
    )
    '''docstring'''

    sourceNo: Mapped[types.PyUnicode] = mapped_column(
        f"Source No_",
        types.DbUnicode20,
        primary_key=False,
        nullable=False,
        info={
            "translations": {
                "pl": "sourceNo",
                "en": "sourceNo",
            }
        }
    )
    '''docstring'''

    routingNo: Mapped[types.PyUnicode] = mapped_column(
        f"Routing No_",
        types.DbUnicode20,
        primary_key=False,
        nullable=False,
        info={
            "translations": {
                "pl": "routingNo",
                "en": "routingNo",
            }
        }
    )
    '''docstring'''

    variantCode: Mapped[types.PyUnicode] = mapped_column(
        f"Variant Code",
        types.DbUnicode10,
        primary_key=False,
        nullable=False,
        info={
            "translations": {
                "pl": "variantCode",
                "en": "variantCode",
            }
        }
    )
    '''docstring'''

    inventoryPostingGroup: Mapped[types.PyUnicode] = mapped_column(
        f"Inventory Posting Group",
        types.DbUnicode20,
        primary_key=False,
        nullable=False,
        info={
            "translations": {
                "pl": "inventoryPostingGroup",
                "en": "inventoryPostingGroup",
            }
        }
    )
    '''docstring'''

    genProdPostingGroup: Mapped[types.PyUnicode] = mapped_column(
        f"Gen_ Prod_ Posting Group",
        types.DbUnicode20,
        primary_key=False,
        nullable=False,
        info={
            "translations": {
                "pl": "genProdPostingGroup",
                "en": "genProdPostingGroup",
            }
        }
    )
    '''docstring'''

    genBusPostingGroup: Mapped[types.PyUnicode] = mapped_column(
        f"Gen_ Bus_ Posting Group",
        types.DbUnicode20,
        primary_key=False,
        nullable=False,
        info={
            "translations": {
                "pl": "genBusPostingGroup",
                "en": "genBusPostingGroup",
            }
        }
    )
    '''docstring'''

    startingTime: Mapped[types.PyDateTime] = mapped_column(
        f"Starting Time",
        types.DbDateTime,
        primary_key=False,
        nullable=False,
        info={
            "translations": {
                "pl": "startingTime",
                "en": "startingTime",
            }
        }
    )
    '''docstring'''

    startingDate: Mapped[types.PyDateTime] = mapped_column(
        f"Starting Date",
        types.DbDateTime,
        primary_key=False,
        nullable=False,
        info={
            "translations": {
                "pl": "startingDate",
                "en": "startingDate",
            }
        }
    )
    '''docstring'''

    endingTime: Mapped[types.PyDateTime] = mapped_column(
        f"Ending Time",
        types.DbDateTime,
        primary_key=False,
        nullable=False,
        info={
            "translations": {
                "pl": "endingTime",
                "en": "endingTime",
            }
        }
    )
    '''docstring'''

    endingDate: Mapped[types.PyDateTime] = mapped_column(
        f"Ending Date",
        types.DbDateTime,
        primary_key=False,
        nullable=False,
        info={
            "translations": {
                "pl": "endingDate",
                "en": "endingDate",
            }
        }
    )
    '''docstring'''

    dueDate: Mapped[types.PyDateTime] = mapped_column(
        f"Due Date",
        types.DbDateTime,
        primary_key=False,
        nullable=False,
        info={
            "translations": {
                "pl": "dueDate",
                "en": "dueDate",
            }
        }
    )
    '''docstring'''

    finishedDate: Mapped[types.PyDateTime] = mapped_column(
        f"Finished Date",
        types.DbDateTime,
        primary_key=False,
        nullable=False,
        info={
            "translations": {
                "pl": "finishedDate",
                "en": "finishedDate",
            }
        }
    )
    '''docstring'''

    blocked: Mapped[types.PyBoolean] = mapped_column(
        f"Blocked",
        types.DbBoolean,
        primary_key=False,
        nullable=False,
        info={
            "translations": {
                "pl": "blocked",
                "en": "blocked",
            }
        }
    )
    '''docstring'''

    shortcutDimension1Code: Mapped[types.PyUnicode] = mapped_column(
        f"Shortcut Dimension 1 Code",
        types.DbUnicode20,
        primary_key=False,
        nullable=False,
        info={
            "translations": {
                "pl": "shortcutDimension1Code",
                "en": "shortcutDimension1Code",
            }
        }
    )
    '''docstring'''

    shortcutDimension2Code: Mapped[types.PyUnicode] = mapped_column(
        f"Shortcut Dimension 2 Code",
        types.DbUnicode20,
        primary_key=False,
        nullable=False,
        info={
            "translations": {
                "pl": "shortcutDimension2Code",
                "en": "shortcutDimension2Code",
            }
        }
    )
    '''docstring'''

    locationCode: Mapped[types.PyUnicode] = mapped_column(
        f"Location Code",
        types.DbUnicode10,
        primary_key=False,
        nullable=False,
        info={
            "translations": {
                "pl": "locationCode",
                "en": "locationCode",
            }
        }
    )
    '''docstring'''

    binCode: Mapped[types.PyUnicode] = mapped_column(
        f"Bin Code",
        types.DbUnicode20,
        primary_key=False,
        nullable=False,
        info={
            "translations": {
                "pl": "binCode",
                "en": "binCode",
            }
        }
    )
    '''docstring'''

    replanRefNo: Mapped[types.PyUnicode] = mapped_column(
        f"Replan Ref_ No_",
        types.DbUnicode20,
        primary_key=False,
        nullable=False,
        info={
            "translations": {
                "pl": "replanRefNo",
                "en": "replanRefNo",
            }
        }
    )
    '''docstring'''

    replanRefStatus: Mapped[types.PyInteger] = mapped_column(
        f"Replan Ref_ Status",
        types.DbInteger,
        primary_key=False,
        nullable=False,
        info={
            "translations": {
                "pl": "replanRefStatus",
                "en": "replanRefStatus",
            }
        }
    )
    '''docstring'''

    lowLevelCode: Mapped[types.PyInteger] = mapped_column(
        f"Low-Level Code",
        types.DbInteger,
        primary_key=False,
        nullable=False,
        info={
            "translations": {
                "pl": "lowLevelCode",
                "en": "lowLevelCode",
            }
        }
    )
    '''docstring'''

    quantity: Mapped[types.PyDecimal] = mapped_column(
        f"Quantity",
        types.DbDecimal,
        primary_key=False,
        nullable=False,
        info={
            "translations": {
                "pl": "quantity",
                "en": "quantity",
            }
        }
    )
    '''docstring'''

    unitCost: Mapped[types.PyDecimal] = mapped_column(
        f"Unit Cost",
        types.DbDecimal,
        primary_key=False,
        nullable=False,
        info={
            "translations": {
                "pl": "unitCost",
                "en": "unitCost",
            }
        }
    )
    '''docstring'''

    costAmount: Mapped[types.PyDecimal] = mapped_column(
        f"Cost Amount",
        types.DbDecimal,
        primary_key=False,
        nullable=False,
        info={
            "translations": {
                "pl": "costAmount",
                "en": "costAmount",
            }
        }
    )
    '''docstring'''

    noSeries: Mapped[types.PyUnicode] = mapped_column(
        f"No_ Series",
        types.DbUnicode20,
        primary_key=False,
        nullable=False,
        info={
            "translations": {
                "pl": "noSeries",
                "en": "noSeries",
            }
        }
    )
    '''docstring'''

    plannedOrderNo: Mapped[types.PyUnicode] = mapped_column(
        f"Planned Order No_",
        types.DbUnicode20,
        primary_key=False,
        nullable=False,
        info={
            "translations": {
                "pl": "plannedOrderNo",
                "en": "plannedOrderNo",
            }
        }
    )
    '''docstring'''

    firmPlannedOrderNo: Mapped[types.PyUnicode] = mapped_column(
        f"Firm Planned Order No_",
        types.DbUnicode20,
        primary_key=False,
        nullable=False,
        info={
            "translations": {
                "pl": "firmPlannedOrderNo",
                "en": "firmPlannedOrderNo",
            }
        }
    )
    '''docstring'''

    simulatedOrderNo: Mapped[types.PyUnicode] = mapped_column(
        f"Simulated Order No_",
        types.DbUnicode20,
        primary_key=False,
        nullable=False,
        info={
            "translations": {
                "pl": "simulatedOrderNo",
                "en": "simulatedOrderNo",
            }
        }
    )
    '''docstring'''

    startingDatetime: Mapped[types.PyDateTime] = mapped_column(
        f"Starting Date-Time",
        types.DbDateTime,
        primary_key=False,
        nullable=False,
        info={
            "translations": {
                "pl": "startingDatetime",
                "en": "startingDatetime",
            }
        }
    )
    '''docstring'''

    endingDatetime: Mapped[types.PyDateTime] = mapped_column(
        f"Ending Date-Time",
        types.DbDateTime,
        primary_key=False,
        nullable=False,
        info={
            "translations": {
                "pl": "endingDatetime",
                "en": "endingDatetime",
            }
        }
    )
    '''docstring'''

    dimensionSetId: Mapped[types.PyInteger] = mapped_column(
        f"Dimension Set ID",
        types.DbInteger,
        primary_key=False,
        nullable=False,
        info={
            "translations": {
                "pl": "dimensionSetId",
                "en": "dimensionSetId",
            }
        }
    )
    '''docstring'''

    assignedUserId: Mapped[types.PyUnicode] = mapped_column(
        f"Assigned User ID",
        types.DbUnicode50,
        primary_key=False,
        nullable=False,
        info={
            "translations": {
                "pl": "assignedUserId",
                "en": "assignedUserId",
            }
        }
    )
    '''docstring'''

    systemId: Mapped[types.PyUUID] = mapped_column(
        f"$systemId",
        types.DbUUID,
        primary_key=False,
        nullable=False,
        info={
            "translations": {
                "pl": "systemId",
                "en": "systemId",
            }
        }
    )
    '''docstring'''

    systemCreatedAt: Mapped[types.PyDateTime] = mapped_column(
        f"$systemCreatedAt",
        types.DbDateTime,
        primary_key=False,
        nullable=False,
        info={
            "translations": {
                "pl": "systemCreatedAt",
                "en": "systemCreatedAt",
            }
        }
    )
    '''docstring'''

    systemCreatedBy: Mapped[types.PyUUID] = mapped_column(
        f"$systemCreatedBy",
        types.DbUUID,
        primary_key=False,
        nullable=False,
        info={
            "translations": {
                "pl": "systemCreatedBy",
                "en": "systemCreatedBy",
            }
        }
    )
    '''docstring'''

    systemModifiedAt: Mapped[types.PyDateTime] = mapped_column(
        f"$systemModifiedAt",
        types.DbDateTime,
        primary_key=False,
        nullable=False,
        info={
            "translations": {
                "pl": "systemModifiedAt",
                "en": "systemModifiedAt",
            }
        }
    )
    '''docstring'''

    systemModifiedBy: Mapped[types.PyUUID] = mapped_column(
        f"$systemModifiedBy",
        types.DbUUID,
        primary_key=False,
        nullable=False,
        info={
            "translations": {
                "pl": "systemModifiedBy",
                "en": "systemModifiedBy",
            }
        }
    )
    '''docstring'''

    #__table_args__ = (
    #    ForeignKeyConstraint(
    #        [
    #            
    #        ],
    #        [
    #            
    #        ]
    #    ),
    #    ForeignKeyConstraint(
    #        [
    #            
    #        ],
    #        [
    #            
    #        ]
    #    )
    #)