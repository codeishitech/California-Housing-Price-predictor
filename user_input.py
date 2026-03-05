from pydantic import BaseModel, Field, computed_field
from typing import Annotated, Literal

class UserInput(BaseModel):
    longitude: Annotated[float, Field(..., description="Longitude of the location")]
    latitude: Annotated[float, Field(..., description="Latitude of the location")]
    housing_median_age: Annotated[float, Field(..., description="Median age of the houses in the area")]
    total_rooms: Annotated[int, Field(..., description="Total number of rooms in the area")]
    total_bedrooms: Annotated[int, Field(..., description="Total number of bedrooms in the area")]
    population: Annotated[int, Field(..., description="Total population in the area")]
    households: Annotated[int, Field(..., description="Total number of households in the area")]
    median_income: Annotated[float, Field(..., description="Median income of the area")]
    ocean_proximity: Annotated[Literal["<1H OCEAN", "INLAND", "ISLAND", "NEAR BAY", "NEAR OCEAN"], Field(..., description="Proximity to the ocean" )]
    