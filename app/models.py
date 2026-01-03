from pydantic import BaseModel, Field

class PersonDetails(BaseModel):
    first_name: str = Field(default="Unknown", description="First name.")
    last_name: str = Field(default="Unknown", description="Last name.")
    address: str = Field(default="Unknown", description="Full address.")
    phone: str = Field(default="Unknown", description="Phone number.")

class SuspectDescription(BaseModel):
    race: str = Field(default="Unknown", description="Race.")
    gender: str = Field(default="Unknown", description="Gender.")
    clothing: str = Field(default="Unknown", description="Clothing.")
    physical_features: str = Field(default="Unknown", description="Features.")

class VehicleDescription(BaseModel):
    make: str = Field(default="Unknown", description="Make.")
    model: str = Field(default="Unknown", description="Model.")
    color: str = Field(default="Unknown", description="Color.")
    plate_number: str = Field(default="Unknown", description="Plate.")


class IncidentReport(BaseModel):
    reporting_person: PersonDetails = Field(default_factory=PersonDetails)
    incident_type: str = Field(default="Unknown", description="Crime type (Theft, Damage, etc).")
    when_time: str = Field(default="Unknown", description="Date/Time.")
    where_location: str = Field(default="Unknown", description="Location.")
    what_happened: str = Field(default="Unknown", description="Narrative.")
    suspect_info: SuspectDescription = Field(default_factory=SuspectDescription)
    vehicle_info: VehicleDescription = Field(default_factory=VehicleDescription)