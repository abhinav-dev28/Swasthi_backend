from typing import Optional, List
from sqlmodel import Field, SQLModel, Relationship
from datetime import datetime


# P2PTransfer
class P2PTransfer(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    amount: int
    timestamp: datetime

    from_user_id: int = Field(foreign_key="user.id")
    to_user_id: int = Field(foreign_key="user.id")

    from_user: Optional["User"] = Relationship(
        back_populates="sent_transfers",
        sa_relationship_kwargs={"foreign_keys": "[P2PTransfer.from_user_id]"},
    )
    to_user: Optional["User"] = Relationship(
        back_populates="received_transfers",
        sa_relationship_kwargs={"foreign_keys": "[P2PTransfer.to_user_id]"},
    )


class OnRampTransaction(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    status: str  # Enum mapping to be handled separately (e.g. with Enum and validators)
    token: str = Field(unique=True)
    provider: str
    amount: int
    start_time: datetime

    user_id: int = Field(foreign_key="user.id")
    user: Optional["User"] = Relationship(back_populates="on_ramp_transactions")


class Balance(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key="user.id", unique=True)
    amount: int
    locked: int

    user: Optional["User"] = Relationship(back_populates="balances")


class LockedBalance(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key="user.id")
    amount: int
    is_locked: bool
    start_date: datetime
    maturity_date: datetime
    name: str
    current_value: int = 0
    interest_rate: int = 3

    user: Optional["User"] = Relationship(back_populates="locked_balances")


class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    email: Optional[str] = Field(default=None, unique=True)
    name: Optional[str] = None
    number: str = Field(unique=True)
    password: str
    locker_pin: int = Field(default=0)

    on_ramp_transactions: List[OnRampTransaction] = Relationship(back_populates="user")
    balances: List[Balance] = Relationship(back_populates="user")
    sent_transfers: List[P2PTransfer] = Relationship(
        back_populates="from_user",
        sa_relationship_kwargs={"foreign_keys": "[P2PTransfer.from_user_id]"},
    )
    received_transfers: List[P2PTransfer] = Relationship(
        back_populates="to_user",
        sa_relationship_kwargs={"foreign_keys": "[P2PTransfer.to_user_id]"},
    )
    locked_balances: List[LockedBalance] = Relationship(back_populates="user")
