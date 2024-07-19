from django_enumfield import enum


class StatusEnum(enum.Enum):
    AVAILABLE = 0
    BOOKED = 1