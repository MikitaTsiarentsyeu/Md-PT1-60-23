from pydantic import BaseModel


class FilmDTO(BaseModel):
    name: str
    year: int
    jenre: str
    dir: str