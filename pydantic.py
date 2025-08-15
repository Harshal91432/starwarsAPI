"""THis is first introduction to pydantic"""



from pydantic import BaseModel



class Foo(BaseModel):
    """BaseModel is a class in pydantic ysed to writing data models"""

    count : int
    size : float

external_data = {"count":100, "size" :30.5}

xyz = Foo(**external_data)

print(xyz)
