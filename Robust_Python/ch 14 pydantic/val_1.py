from typing import Literal, Optional, Union
from pydantic.dataclasses import dataclass
from pydantic import constr, PositiveInt, conint, conlist
from pydantic import validator

import yaml

@dataclass
class AccountAndRoutingNumber:
    # account_number: str
    # routing_number: str
    account_number: constr(min_length=8, max_length=12)
    routing_number: constr(min_length=9, max_length=9)


@dataclass
class BankDetails:
    bank_details: AccountAndRoutingNumber


AddressOrBankDetails = Union[str, BankDetails]

Position = Literal['Chef', 'Sous Chef', 'Host', 'Server', 'Delivery Driver']


@dataclass
class Dish:
    name: constr(min_length=1, max_length=20)
    price_in_cents: PositiveInt
    description: constr(min_length=1, max_length=80)
    picture: Optional[str] = None


@dataclass
class Employee:
    name: str
    position: Position
    payment_details: AddressOrBankDetails


@dataclass
class Restaurant:
    name: constr(min_length=1, max_length=16)
    owner: constr(min_length=1)
    address: constr(min_length=1)
    # employees: list[Employee]
    employees: conlist(Employee, min_items=2)
    dishes: conlist(Dish, min_items=3)
    number_of_seats: conint(gt=3)
    to_go: bool
    delivery: bool

    @validator('employees')
    def check_chef_and_server(cls, employees):
        if (any(e for e in employees if e.position == 'Chef') and
                any(e for e in employees if e.position == 'Server')):
            return employees

    raise ValueError('Must have at least one chef and one server')


def load_restaurant(filename: str) -> Restaurant:
    with open(filename) as yaml_file:
        data = yaml.safe_load(yaml_file)
    return Restaurant(**data)