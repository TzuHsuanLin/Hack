from datetime import datetime, timedelta, timezone
from pydantic import BaseModel,Field

class Inventory(BaseModel):
    signature: str = Field(default='')
    material:float = Field(default=0.0)

class Result(BaseModel):
    success: bool = Field(default=True)
    @staticmethod
    def ok():
        return Result(success=True)
    @staticmethod
    def failed():
        return Result(success=False)

class Data(BaseModel):
    a: float = Field(default=0.0)
    b: float = Field(default=0.0)
    c: float = Field(default=0.0)
    d: float = Field(default=0.0)


class Orders(BaseModel):
    location: str = Field(default='l1')
    timestamp: str = Field(
        default_factory=datetime.now(timezone(timedelta(hours=+8))).isoformat(timespec='milliseconds'),
        example='2023-01-01T00:00:00+08:00',
    )
    data: Data = Field(default_factory=Data)


class Record(BaseModel):
    location: str = Field(default='l1')
    timestamp: str = Field(example='2023-01-01T00:00:00+08:00')
    signature: str = Field(default='')
    material: float = Field(default=0.0)
    a: float = Field(default=0.0)
    b: float = Field(default=0.0)
    c: float = Field(default=0.0)
    d: float = Field(default=0.0)


class Report(BaseModel):
    location: str = Field(default='l1')
    date: str = Field(example='2023-01-01')

    count: int = Field(default=0)
    material: float = Field(default=0.0)
    a: float = Field(default=0.0)
    b: float = Field(default=0.0)
    c: float = Field(default=0.0)
    d: float = Field(default=0.0)


# def order_to_record(order: Orders) -> Record:
#     return Record(
#         location=order.location,
#         timestamp=order.timestamp,
#         a=order.data.a,
#         b=order.data.b,
#         c=order.data.c,
#         d=order.data.d,
#     )
