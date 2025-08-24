"""THis is first introduction to pydantic

Request data validation
Response data validation


Sigular and plural urls

HTTP methods
GET
Post
PUt
patch
Delete

"""



from pydantic import BaseModel



class Foo(BaseModel):
    """BaseModel is a class in pydantic ysed to writing data models"""

    count : int
    size : float

external_data = {"count":100, "size" :30.5}

xyz = Foo(**external_data)

breakpoint()

print(xyz)
