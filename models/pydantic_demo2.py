from pydantic import BaseModel


class Foo(BaseModel):
    """BaseModel is a class in pydantic used to writing data models"""

    count : int
    size : float

external_data = {"count":"", "size":""}  # here passes the wrong parameter

xyz = Foo(**external_data)

breakpoint()

print(xyz)