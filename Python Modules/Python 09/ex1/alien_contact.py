from pydantic import BaseModel, Field, model_validator, ValidationError
from datetime import datetime
from typing import Optional
from enum import Enum 

class ContactType(str, Enum):
    radio = "radio"
    visual = "visual"
    physical = "physical"
    telepathic = "telepathic"

class AlienContact(BaseModel):
    contact_id: str = Field(min_length=5, max_length=15)
    timestamp: datetime
    location: str = Field(min_length=3, max_length=100)
    contact_type: ContactType
    signal_strength: float = Field(ge=0.0, le=10.0)
    duration_minutes: int = Field(ge=1, le=1440)
    witness_count: int = Field(ge=1, le=100)
    message_received: Optional[str] = Field(default=None, max_length=500)
    is_verified: bool = Field(default=False)

    @model_validator(mode='after')
    def validate_info(self) -> "AlienContact":
        # contact_id = self.contact_id
        # contact_type = self.contact_type
        # signal = self.signal_strength
        # witnesses = self.witness_count
        # message = self.message_received
        # verified = self.is_verified
        if not self.contact_id.startswith("AC"):
            raise ValueError("Contact ID must start with 'AC' (Alien Contact)")
        if self.contact_type == ContactType.physical and not verified:
            raise ValueError("Physical Contact must be verified")
        if self.contact_type == ContactType.telepathic and self.witness_count < 3:
            raise ValueError("Telepathic contact requires at least 3 witnesses")
        if self.signal_strength > 7.0 and not self.message_received:
            raise ValueError("Strong signals (>7.0) should include received messages")
        return self


def demo() -> None:
    print("Alien Contact Log Validation")
    try:
        print("=====================================")
        first_c= AlienContact(
            contact_id= "AC_2024_001",
            timestamp = datetime.now(),
            location = "Area 51, Nevada",
            contact_type = ContactType.radio,
            signal_strength = 8.5,
            duration_minutes = 45,
            witness_count = 5,
            message_received = "Greetings from Zeta Reticuli",
            # is_verified = False
        )

        print("Valid contract report:")
        print(f"ID: {first_c.contact_id}")
        print(f"Type: {first_c.contact_type.value}")
        print(f"Location: {first_c.location}")
        print(f"Signal: {first_c.signal_strength}/10")
        print(f"Duration: {first_c.duration_minutes} minutes")
        print(f"Witnesses: {first_c.witness_count}")
        print(f"Message: '{first_c.message_received}'")

    except ValidationError as e:
        print("Validation Error:")
        for error in e.errors():
            print(error["msg"])

    try:
        failed_contact = AlienContact(
            contact_id= "AC_2024_001",
            timestamp = datetime.now(),
            location = "Area 51, Nevada",
            contact_type = ContactType.telepathic,
            signal_strength = 8.5,
            duration_minutes = 45,
            witness_count = 2,
            message_recieved = "Greetings from Zeta Reticuli",
        )

    except ValidationError as e:
        print("\n=====================================")
        print("Expected validation error:")
        for error in e.errors():
            print(error["msg"])



if __name__ == "__main__":
    demo()
