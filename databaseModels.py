
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped, mapped_column

import databaseTypes as types
from config_menager import appConfig

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


class RecordLink(BaseModel):
    
    __tablename__ = f"Record Link"
    
    linkId: Mapped[types.PyInteger] = mapped_column("Link ID", types.DbInteger, primary_key=True, nullable=False)
    
    recordId: Mapped[types.PyBinary] = mapped_column("Record ID", types.DbBinary448, nullable=False)
    
    url1: Mapped[types.PyUnicode] = mapped_column("URL1", types.DbUnicode2048, nullable=False)

    # url2: Mapped[types.PyUnicode] = mapped_column("URL2", types.DbUnicode250, nullable=False)
    
    # url3: Mapped[types.PyUnicode] = mapped_column("URL3", types.DbUnicode250, nullable=False)
    
    # url4: Mapped[types.PyUnicode] = mapped_column("URL4", types.DbUnicode250, nullable=False)

    description: Mapped[types.PyUnicode] = mapped_column("Description", types.DbUnicode250, nullable=False)
    
    type: Mapped[types.PyInteger] = mapped_column("Type", types.DbInteger, nullable=False)
    
    # note: Mapped[types.PyImage] = mapped_column("Note", types.DbImage, nullable=True)
    
    # created: Mapped[types.PyDateTime] = mapped_column("Created", types.DbDateTime, nullable=False)
    
    # userId: Mapped[types.PyUnicode] = mapped_column("User ID", types.DbUnicode132, nullable=False)
    
    company: Mapped[types.PyUnicode] = mapped_column("Company", types.DbUnicode30, nullable=False)

    # notify: Mapped[types.PyBoolean] = mapped_column("Notify", types.DbBoolean, nullable=False)
    
    # toUserId: Mapped[types.PyUnicode] = mapped_column("To User ID", types.DbUnicode132, nullable=False)
    
class ProductionOrderLine(BaseModel):
    '''docstring'''

    __tablename__ = f"{appConfig.get('BC', 'CompanyName')}$Prod_ Order Line${appConfig.get('BC', 'ExtensionBaseApplication')}"

    # timestamp: Mapped[types.PyDateTime] = mapped_column(
    #     f"timestamp",
    #     types.DbDateTime,
    #     primary_key=False,
    #     nullable=False,
    #     info={
    #         "translations": {
    #             "pl": "timestamp",
    #             "en": "timestamp",
    #         }
    #     }
    # )
    # '''docstring'''

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

    prodOrderNo: Mapped[types.PyUnicode] = mapped_column(
        f"Prod_ Order No_",
        types.DbUnicode20,
        primary_key=True,
        nullable=False,
        info={
            "translations": {
                "pl": "prodOrderNo",
                "en": "prodOrderNo",
            }
        }
    )
    '''docstring'''

    lineNo: Mapped[types.PyInteger] = mapped_column(
        f"Line No_",
        types.DbInteger,
        primary_key=True,
        nullable=False,
        info={
            "translations": {
                "pl": "lineNo",
                "en": "lineNo",
            }
        }
    )
    '''docstring'''

    itemNo: Mapped[types.PyUnicode] = mapped_column(
        f"Item No_",
        types.DbUnicode20,
        primary_key=False,
        nullable=False,
        info={
            "translations": {
                "pl": "itemNo",
                "en": "itemNo",
            }
        }
    )
    '''docstring'''

    # variantCode: Mapped[types.PyUnicode] = mapped_column(
    #     f"Variant Code",
    #     types.DbUnicode10,
    #     primary_key=False,
    #     nullable=False,
    #     info={
    #         "translations": {
    #             "pl": "variantCode",
    #             "en": "variantCode",
    #         }
    #     }
    # )
    # '''docstring'''

    # description: Mapped[types.PyUnicode] = mapped_column(
    #     f"Description",
    #     types.DbUnicode100,
    #     primary_key=False,
    #     nullable=False,
    #     info={
    #         "translations": {
    #             "pl": "description",
    #             "en": "description",
    #         }
    #     }
    # )
    # '''docstring'''

    # description2: Mapped[types.PyUnicode] = mapped_column(
    #     f"Description 2",
    #     types.DbUnicode50,
    #     primary_key=False,
    #     nullable=False,
    #     info={
    #         "translations": {
    #             "pl": "description2",
    #             "en": "description2",
    #         }
    #     }
    # )
    # '''docstring'''

    # locationCode: Mapped[types.PyUnicode] = mapped_column(
    #     f"Location Code",
    #     types.DbUnicode10,
    #     primary_key=False,
    #     nullable=False,
    #     info={
    #         "translations": {
    #             "pl": "locationCode",
    #             "en": "locationCode",
    #         }
    #     }
    # )
    # '''docstring'''

    # shortcutDimension1Code: Mapped[types.PyUnicode] = mapped_column(
    #     f"Shortcut Dimension 1 Code",
    #     types.DbUnicode20,
    #     primary_key=False,
    #     nullable=False,
    #     info={
    #         "translations": {
    #             "pl": "shortcutDimension1Code",
    #             "en": "shortcutDimension1Code",
    #         }
    #     }
    # )
    # '''docstring'''

    # shortcutDimension2Code: Mapped[types.PyUnicode] = mapped_column(
    #     f"Shortcut Dimension 2 Code",
    #     types.DbUnicode20,
    #     primary_key=False,
    #     nullable=False,
    #     info={
    #         "translations": {
    #             "pl": "shortcutDimension2Code",
    #             "en": "shortcutDimension2Code",
    #         }
    #     }
    # )
    # '''docstring'''

    # binCode: Mapped[types.PyUnicode] = mapped_column(
    #     f"Bin Code",
    #     types.DbUnicode20,
    #     primary_key=False,
    #     nullable=False,
    #     info={
    #         "translations": {
    #             "pl": "binCode",
    #             "en": "binCode",
    #         }
    #     }
    # )
    # '''docstring'''

    # quantity: Mapped[types.PyDecimal] = mapped_column(
    #     f"Quantity",
    #     types.DbDecimal,
    #     primary_key=False,
    #     nullable=False,
    #     info={
    #         "translations": {
    #             "pl": "quantity",
    #             "en": "quantity",
    #         }
    #     }
    # )
    # '''docstring'''

    # finishedQuantity: Mapped[types.PyDecimal] = mapped_column(
    #     f"Finished Quantity",
    #     types.DbDecimal,
    #     primary_key=False,
    #     nullable=False,
    #     info={
    #         "translations": {
    #             "pl": "finishedQuantity",
    #             "en": "finishedQuantity",
    #         }
    #     }
    # )
    # '''docstring'''

    # remainingQuantity: Mapped[types.PyDecimal] = mapped_column(
    #     f"Remaining Quantity",
    #     types.DbDecimal,
    #     primary_key=False,
    #     nullable=False,
    #     info={
    #         "translations": {
    #             "pl": "remainingQuantity",
    #             "en": "remainingQuantity",
    #         }
    #     }
    # )
    # '''docstring'''

    # scrap: Mapped[types.PyDecimal] = mapped_column(
    #     f"Scrap _",
    #     types.DbDecimal,
    #     primary_key=False,
    #     nullable=False,
    #     info={
    #         "translations": {
    #             "pl": "scrap",
    #             "en": "scrap",
    #         }
    #     }
    # )
    # '''docstring'''

    # dueDate: Mapped[types.PyDateTime] = mapped_column(
    #     f"Due Date",
    #     types.DbDateTime,
    #     primary_key=False,
    #     nullable=False,
    #     info={
    #         "translations": {
    #             "pl": "dueDate",
    #             "en": "dueDate",
    #         }
    #     }
    # )
    # '''docstring'''

    # startingDate: Mapped[types.PyDateTime] = mapped_column(
    #     f"Starting Date",
    #     types.DbDateTime,
    #     primary_key=False,
    #     nullable=False,
    #     info={
    #         "translations": {
    #             "pl": "startingDate",
    #             "en": "startingDate",
    #         }
    #     }
    # )
    # '''docstring'''

    # startingTime: Mapped[types.PyDateTime] = mapped_column(
    #     f"Starting Time",
    #     types.DbDateTime,
    #     primary_key=False,
    #     nullable=False,
    #     info={
    #         "translations": {
    #             "pl": "startingTime",
    #             "en": "startingTime",
    #         }
    #     }
    # )
    # '''docstring'''

    # endingDate: Mapped[types.PyDateTime] = mapped_column(
    #     f"Ending Date",
    #     types.DbDateTime,
    #     primary_key=False,
    #     nullable=False,
    #     info={
    #         "translations": {
    #             "pl": "endingDate",
    #             "en": "endingDate",
    #         }
    #     }
    # )
    # '''docstring'''

    # endingTime: Mapped[types.PyDateTime] = mapped_column(
    #     f"Ending Time",
    #     types.DbDateTime,
    #     primary_key=False,
    #     nullable=False,
    #     info={
    #         "translations": {
    #             "pl": "endingTime",
    #             "en": "endingTime",
    #         }
    #     }
    # )
    # '''docstring'''

    # planningLevelCode: Mapped[types.PyInteger] = mapped_column(
    #     f"Planning Level Code",
    #     types.DbInteger,
    #     primary_key=False,
    #     nullable=False,
    #     info={
    #         "translations": {
    #             "pl": "planningLevelCode",
    #             "en": "planningLevelCode",
    #         }
    #     }
    # )
    # '''docstring'''

    # priority: Mapped[types.PyInteger] = mapped_column(
    #     f"Priority",
    #     types.DbInteger,
    #     primary_key=False,
    #     nullable=False,
    #     info={
    #         "translations": {
    #             "pl": "priority",
    #             "en": "priority",
    #         }
    #     }
    # )
    # '''docstring'''

    # productionBomNo: Mapped[types.PyUnicode] = mapped_column(
    #     f"Production BOM No_",
    #     types.DbUnicode20,
    #     primary_key=False,
    #     nullable=False,
    #     info={
    #         "translations": {
    #             "pl": "productionBomNo",
    #             "en": "productionBomNo",
    #         }
    #     }
    # )
    # '''docstring'''

    # routingNo: Mapped[types.PyUnicode] = mapped_column(
    #     f"Routing No_",
    #     types.DbUnicode20,
    #     primary_key=False,
    #     nullable=False,
    #     info={
    #         "translations": {
    #             "pl": "routingNo",
    #             "en": "routingNo",
    #         }
    #     }
    # )
    # '''docstring'''

    # inventoryPostingGroup: Mapped[types.PyUnicode] = mapped_column(
    #     f"Inventory Posting Group",
    #     types.DbUnicode20,
    #     primary_key=False,
    #     nullable=False,
    #     info={
    #         "translations": {
    #             "pl": "inventoryPostingGroup",
    #             "en": "inventoryPostingGroup",
    #         }
    #     }
    # )
    # '''docstring'''

    # routingReferenceNo: Mapped[types.PyInteger] = mapped_column(
    #     f"Routing Reference No_",
    #     types.DbInteger,
    #     primary_key=False,
    #     nullable=False,
    #     info={
    #         "translations": {
    #             "pl": "routingReferenceNo",
    #             "en": "routingReferenceNo",
    #         }
    #     }
    # )
    # '''docstring'''

    # unitCost: Mapped[types.PyDecimal] = mapped_column(
    #     f"Unit Cost",
    #     types.DbDecimal,
    #     primary_key=False,
    #     nullable=False,
    #     info={
    #         "translations": {
    #             "pl": "unitCost",
    #             "en": "unitCost",
    #         }
    #     }
    # )
    # '''docstring'''

    # costAmount: Mapped[types.PyDecimal] = mapped_column(
    #     f"Cost Amount",
    #     types.DbDecimal,
    #     primary_key=False,
    #     nullable=False,
    #     info={
    #         "translations": {
    #             "pl": "costAmount",
    #             "en": "costAmount",
    #         }
    #     }
    # )
    # '''docstring'''

    # qtyRoundingPrecision: Mapped[types.PyDecimal] = mapped_column(
    #     f"Qty_ Rounding Precision",
    #     types.DbDecimal,
    #     primary_key=False,
    #     nullable=False,
    #     info={
    #         "translations": {
    #             "pl": "qtyRoundingPrecision",
    #             "en": "qtyRoundingPrecision",
    #         }
    #     }
    # )
    # '''docstring'''

    # qtyRoundingPrecisionBase: Mapped[types.PyDecimal] = mapped_column(
    #     f"Qty_ Rounding Precision (Base)",
    #     types.DbDecimal,
    #     primary_key=False,
    #     nullable=False,
    #     info={
    #         "translations": {
    #             "pl": "qtyRoundingPrecisionBase",
    #             "en": "qtyRoundingPrecisionBase",
    #         }
    #     }
    # )
    # '''docstring'''

    # unitOfMeasureCode: Mapped[types.PyUnicode] = mapped_column(
    #     f"Unit of Measure Code",
    #     types.DbUnicode10,
    #     primary_key=False,
    #     nullable=False,
    #     info={
    #         "translations": {
    #             "pl": "unitOfMeasureCode",
    #             "en": "unitOfMeasureCode",
    #         }
    #     }
    # )
    # '''docstring'''

    # quantityBase: Mapped[types.PyDecimal] = mapped_column(
    #     f"Quantity (Base)",
    #     types.DbDecimal,
    #     primary_key=False,
    #     nullable=False,
    #     info={
    #         "translations": {
    #             "pl": "quantityBase",
    #             "en": "quantityBase",
    #         }
    #     }
    # )
    # '''docstring'''

    # finishedQtyBase: Mapped[types.PyDecimal] = mapped_column(
    #     f"Finished Qty_ (Base)",
    #     types.DbDecimal,
    #     primary_key=False,
    #     nullable=False,
    #     info={
    #         "translations": {
    #             "pl": "finishedQtyBase",
    #             "en": "finishedQtyBase",
    #         }
    #     }
    # )
    # '''docstring'''

    # remainingQtyBase: Mapped[types.PyDecimal] = mapped_column(
    #     f"Remaining Qty_ (Base)",
    #     types.DbDecimal,
    #     primary_key=False,
    #     nullable=False,
    #     info={
    #         "translations": {
    #             "pl": "remainingQtyBase",
    #             "en": "remainingQtyBase",
    #         }
    #     }
    # )
    # '''docstring'''

    # startingDatetime: Mapped[types.PyDateTime] = mapped_column(
    #     f"Starting Date-Time",
    #     types.DbDateTime,
    #     primary_key=False,
    #     nullable=False,
    #     info={
    #         "translations": {
    #             "pl": "startingDatetime",
    #             "en": "startingDatetime",
    #         }
    #     }
    # )
    # '''docstring'''

    # endingDatetime: Mapped[types.PyDateTime] = mapped_column(
    #     f"Ending Date-Time",
    #     types.DbDateTime,
    #     primary_key=False,
    #     nullable=False,
    #     info={
    #         "translations": {
    #             "pl": "endingDatetime",
    #             "en": "endingDatetime",
    #         }
    #     }
    # )
    # '''docstring'''

    # dimensionSetId: Mapped[types.PyInteger] = mapped_column(
    #     f"Dimension Set ID",
    #     types.DbInteger,
    #     primary_key=False,
    #     nullable=False,
    #     info={
    #         "translations": {
    #             "pl": "dimensionSetId",
    #             "en": "dimensionSetId",
    #         }
    #     }
    # )
    # '''docstring'''

    # costAmountAcy: Mapped[types.PyDecimal] = mapped_column(
    #     f"Cost Amount (ACY)",
    #     types.DbDecimal,
    #     primary_key=False,
    #     nullable=False,
    #     info={
    #         "translations": {
    #             "pl": "costAmountAcy",
    #             "en": "costAmountAcy",
    #         }
    #     }
    # )
    # '''docstring'''

    # unitCostAcy: Mapped[types.PyDecimal] = mapped_column(
    #     f"Unit Cost (ACY)",
    #     types.DbDecimal,
    #     primary_key=False,
    #     nullable=False,
    #     info={
    #         "translations": {
    #             "pl": "unitCostAcy",
    #             "en": "unitCostAcy",
    #         }
    #     }
    # )
    # '''docstring'''

    # productionBomVersionCode: Mapped[types.PyUnicode] = mapped_column(
    #     f"Production BOM Version Code",
    #     types.DbUnicode20,
    #     primary_key=False,
    #     nullable=False,
    #     info={
    #         "translations": {
    #             "pl": "productionBomVersionCode",
    #             "en": "productionBomVersionCode",
    #         }
    #     }
    # )
    # '''docstring'''

    # routingVersionCode: Mapped[types.PyUnicode] = mapped_column(
    #     f"Routing Version Code",
    #     types.DbUnicode20,
    #     primary_key=False,
    #     nullable=False,
    #     info={
    #         "translations": {
    #             "pl": "routingVersionCode",
    #             "en": "routingVersionCode",
    #         }
    #     }
    # )
    # '''docstring'''

    # routingType: Mapped[types.PyInteger] = mapped_column(
    #     f"Routing Type",
    #     types.DbInteger,
    #     primary_key=False,
    #     nullable=False,
    #     info={
    #         "translations": {
    #             "pl": "routingType",
    #             "en": "routingType",
    #         }
    #     }
    # )
    # '''docstring'''

    # qtyPerUnitOfMeasure: Mapped[types.PyDecimal] = mapped_column(
    #     f"Qty_ per Unit of Measure",
    #     types.DbDecimal,
    #     primary_key=False,
    #     nullable=False,
    #     info={
    #         "translations": {
    #             "pl": "qtyPerUnitOfMeasure",
    #             "en": "qtyPerUnitOfMeasure",
    #         }
    #     }
    # )
    # '''docstring'''

    # mPSOrder: Mapped[types.PyBoolean] = mapped_column(
    #     f"MPS Order",
    #     types.DbBoolean,
    #     primary_key=False,
    #     nullable=False,
    #     info={
    #         "translations": {
    #             "pl": "mPSOrder",
    #             "en": "mPSOrder",
    #         }
    #     }
    # )
    # '''docstring'''

    # planningFlexibility: Mapped[types.PyInteger] = mapped_column(
    #     f"Planning Flexibility",
    #     types.DbInteger,
    #     primary_key=False,
    #     nullable=False,
    #     info={
    #         "translations": {
    #             "pl": "planningFlexibility",
    #             "en": "planningFlexibility",
    #         }
    #     }
    # )
    # '''docstring'''

    # indirectCost: Mapped[types.PyDecimal] = mapped_column(
    #     f"Indirect Cost _",
    #     types.DbDecimal,
    #     primary_key=False,
    #     nullable=False,
    #     info={
    #         "translations": {
    #             "pl": "indirectCost",
    #             "en": "indirectCost",
    #         }
    #     }
    # )
    # '''docstring'''

    # overheadRate: Mapped[types.PyDecimal] = mapped_column(
    #     f"Overhead Rate",
    #     types.DbDecimal,
    #     primary_key=False,
    #     nullable=False,
    #     info={
    #         "translations": {
    #             "pl": "overheadRate",
    #             "en": "overheadRate",
    #         }
    #     }
    # )
    # '''docstring'''

    # systemId: Mapped[types.PyUUID] = mapped_column(
    #     f"$systemId",
    #     types.DbUUID,
    #     primary_key=False,
    #     nullable=False,
    #     info={
    #         "translations": {
    #             "pl": "systemId",
    #             "en": "systemId",
    #         }
    #     }
    # )
    # '''docstring'''

    # systemCreatedAt: Mapped[types.PyDateTime] = mapped_column(
    #     f"$systemCreatedAt",
    #     types.DbDateTime,
    #     primary_key=False,
    #     nullable=False,
    #     info={
    #         "translations": {
    #             "pl": "systemCreatedAt",
    #             "en": "systemCreatedAt",
    #         }
    #     }
    # )
    # '''docstring'''

    # systemCreatedBy: Mapped[types.PyUUID] = mapped_column(
    #     f"$systemCreatedBy",
    #     types.DbUUID,
    #     primary_key=False,
    #     nullable=False,
    #     info={
    #         "translations": {
    #             "pl": "systemCreatedBy",
    #             "en": "systemCreatedBy",
    #         }
    #     }
    # )
    # '''docstring'''

    # systemModifiedAt: Mapped[types.PyDateTime] = mapped_column(
    #     f"$systemModifiedAt",
    #     types.DbDateTime,
    #     primary_key=False,
    #     nullable=False,
    #     info={
    #         "translations": {
    #             "pl": "systemModifiedAt",
    #             "en": "systemModifiedAt",
    #         }
    #     }
    # )
    # '''docstring'''

    # systemModifiedBy: Mapped[types.PyUUID] = mapped_column(
    #     f"$systemModifiedBy",
    #     types.DbUUID,
    #     primary_key=False,
    #     nullable=False,
    #     info={
    #         "translations": {
    #             "pl": "systemModifiedBy",
    #             "en": "systemModifiedBy",
    #         }
    #     }
    # )
    # '''docstring'''

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