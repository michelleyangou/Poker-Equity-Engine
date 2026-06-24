from sqlalchemy import (
    Column, Integer, Text, Boolean,
    Numeric, DateTime, ARRAY, ForeignKey
)
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Player(Base):
    __tablename__ = "players"

    player_id = Column(Integer, primary_key=True, autoincrement=True)
    username  = Column(Text, unique=True, nullable=False)
    is_hero   = Column(Boolean, default=False)


class Session(Base):
    __tablename__ = "sessions"

    session_id  = Column(Integer, primary_key=True, autoincrement=True)
    source_file = Column(Text)
    game_type   = Column(Text)
    stakes      = Column(Text)
    played_at   = Column(DateTime)


class Hand(Base):
    __tablename__ = "hands"

    hand_id          = Column(Integer, primary_key=True, autoincrement=True)
    session_id       = Column(Integer, ForeignKey("sessions.session_id"))
    external_hand_no = Column(Text)
    board            = Column(ARRAY(Text))
    pot_size         = Column(Numeric)
    rake             = Column(Numeric)
    played_at        = Column(DateTime)


class HandPlayer(Base):
    __tablename__ = "hand_players"

    hand_id        = Column(Integer, ForeignKey("hands.hand_id"), primary_key=True)
    player_id      = Column(Integer, ForeignKey("players.player_id"), primary_key=True)
    seat           = Column(Integer)
    position       = Column(Text)
    starting_stack = Column(Numeric)
    hole_cards     = Column(ARRAY(Text))
    net_result     = Column(Numeric)


class HandAction(Base):
    __tablename__ = "hand_actions"

    action_id   = Column(Integer, primary_key=True, autoincrement=True)
    hand_id     = Column(Integer, ForeignKey("hands.hand_id"))
    player_id   = Column(Integer, ForeignKey("players.player_id"))
    street      = Column(Text)
    action_type = Column(Text)
    amount      = Column(Numeric)
    action_seq  = Column(Integer)


class PlayerStatsSnapshot(Base):
    __tablename__ = "player_stats_snapshots"

    player_id          = Column(Integer, ForeignKey("players.player_id"), primary_key=True)
    computed_at        = Column(DateTime, primary_key=True)
    hands_played       = Column(Integer)
    vpip               = Column(Numeric)
    pfr                = Column(Numeric)
    three_bet_pct      = Column(Numeric)
    aggression_factor  = Column(Numeric)
    cluster_label      = Column(Text)