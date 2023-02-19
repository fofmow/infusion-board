from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class InactivePeriodStatus:
    LESS_DAY = 0
    MORE_DAY = 1
    MORE_THREE_DAYS = 2