


from enum import Enum
from enum import IntEnum



from sqlalchemy import select

import datetime

from sqlalchemy import inspect
import database.utils.constants as const





url = "http://192.168.23.16/dokumentacja/Produkcje/DRA-19140-000 RevC(19_02_2025)_979121154113446624023224211743128184226140.pdf"
print(url.split("/")[-1])



# hexString = '0x1B000000027BFF440055005400300031003000310030003100300030003900370000000000'
            #    
# hexString = '0xD801000000919E454A41CB0FCF4CBA118589FF1E37240000'
# hexString =  ttttttttt
# http://192.168.23.16/dokumentacja/DUT0102030027_cat.pdf

# byteArray = bytearray.fromhex(hexString[2:])
# print(byteArray)
# print(byteArray[0:4])
# print(byteArray[4:5]) #codeFileld
# print(byteArray[6:7]) #alfanumeric
# print(byteArray[6:32])

# tableId = int.from_bytes(byteArray[0:4], byteorder='little')
# codeFileld = int.from_bytes(byteArray[4:5], byteorder='little')
# # codeFileld2 = int.from_bytes(byteArray[6:7], byteorder='little')


# print(tableId)
# print(codeFileld)
# # print(codeFileld2)
# print(byteArray[7:32].decode('utf-8'))



# def create_component_bytes(component: str, table_id: int, field_type: int) -> bytearray:
#     component_bytes = bytearray()
#     component_bytes += table_id.to_bytes(length=4, byteorder='little')
#     component_bytes += field_type.to_bytes(length=1, byteorder='little')

#     for idx, char in enumerate(component):
#         prefix = (255).to_bytes(length=1, byteorder='little') if idx == 0 else (0).to_bytes(length=1, byteorder='little')
#         component_bytes += prefix + char.encode(encoding='utf-8', errors='strict')

#     # Dodanie pięciu bajtów zerowych na końcu
#     component_bytes += (0).to_bytes(length=5, byteorder='little')

#     return component_bytes

# # Przykładowe użycie
# component = "DUT0101010097"
# table_id = 27
# field_type = 2

# component_bytes = create_component_bytes(component, table_id, field_type)
# print(component_bytes)

# bbb = b'\x1b\x00\x00\x00\x02{\xffA\x00G\x00F\x009\x000\x000\x002\x004\x009\x005\x001\x00.\x000\x00.\x000\x003\x00R\x00D\x00\x00\x00\x00\x00'
# print(int.from_bytes(bbb[0:4], byteorder='little'))
# print(int.from_bytes(bbb[4:5], byteorder='little'))

# encoded_bytes = b''.join([char.encode('utf-8') for char in text])
# print(encoded_bytes.hex())



# with Session() as session:
    
#     # not work
#     # rows = session.scalars(select(RecordLink).where(RecordLink.recordId == "0xD8010000009151957617F8BB5C40BB36BA5FBDEAF12C0000")).all()
    
#     #work
#     rows = session.scalars(select(RecordLink).where(RecordLink.recordId == b'\x1b\x00\x00\x00\x02{\xffA\x00G\x00F\x009\x000\x000\x002\x004\x009\x005\x001\x00.\x000\x00.\x000\x003\x00R\x00D\x00\x00\x00\x00\x00')).all()
#     rows = [row.to_dict() for row in rows]
#     df = pd.DataFrame(rows)
#     print(df)
    
#     for row in rows:
#         print(row.productionOrderStatus)
    