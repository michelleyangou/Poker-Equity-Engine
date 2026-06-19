# Poker Analytics — Database Schema

## players
One row per unique player username.

| column    | type    | notes                          |
|-----------|---------|--------------------------------|
| player_id | SERIAL  | primary key, auto-increments   |
| username  | TEXT    | unique, e.g. "michelleou99"    |
| is_hero   | BOOLEAN | TRUE = you, FALSE = opponents  |

## sessions
One row per hand history file you upload.

| column      | type      | notes                        |
|-------------|-----------|------------------------------|
| session_id  | SERIAL    | primary key                  |
| source_file | TEXT      | filename, e.g. "jan_cash.phh"|
| game_type   | TEXT      | "NLHE" or "PLO"              |
| stakes      | TEXT      | e.g. "1/2" or "2/5"         |
| played_at   | TIMESTAMP | when the session happened    |

## hands
One row per individual hand played.

| column           | type      | notes                              |
|------------------|-----------|------------------------------------|
| hand_id          | SERIAL    | primary key                        |
| session_id       | INT       | which session this hand belongs to |
| external_hand_no | TEXT      | hand number from the PHH file      |
| board            | TEXT[]    | community cards, e.g. ["Ah","Kd","2c"] |
| pot_size         | NUMERIC   | total pot at end of hand           |
| rake             | NUMERIC   | fee taken by the house             |
| played_at        | TIMESTAMP | when this hand was played          |

## hand_players
One row per player per hand (links players to hands).

| column         | type    | notes                                    |
|----------------|---------|------------------------------------------|
| hand_id        | INT     | which hand                               |
| player_id      | INT     | which player                             |
| seat           | INT     | seat number at the table                 |
| position       | TEXT    | "BTN","SB","BB","UTG","HJ","CO"          |
| starting_stack | NUMERIC | how many chips they started the hand with|
| hole_cards     | TEXT[]  | their cards, NULL if they mucked/unknown |
| net_result     | NUMERIC | positive = won chips, negative = lost    |

## hand_actions
One row per action taken during a hand (fold, call, raise, etc).

| column      | type    | notes                                       |
|-------------|---------|---------------------------------------------|
| action_id   | SERIAL  | primary key                                 |
| hand_id     | INT     | which hand this action belongs to           |
| player_id   | INT     | who took this action                        |
| street      | TEXT    | "preflop","flop","turn","river"             |
| action_type | TEXT    | "fold","check","call","bet","raise","allin" |
| amount      | NUMERIC | how much, NULL for fold/check               |
| action_seq  | INT     | order of this action in the hand (0,1,2...) |

## player_stats_snapshots
One row per player per time we recompute their stats.

| column            | type      | notes                              |
|-------------------|-----------|------------------------------------|
| player_id         | INT       | which player                       |
| computed_at       | TIMESTAMP | when we ran the calculation        |
| hands_played      | INT       | total hands in our data            |
| vpip              | NUMERIC   | % of hands they voluntarily put $ in|
| pfr               | NUMERIC   | % of hands they raised preflop     |
| three_bet_pct     | NUMERIC   | % of hands they 3-bet              |
| aggression_factor | NUMERIC   | ratio of bets+raises to calls      |
| cluster_label     | TEXT      | e.g. "tight-aggressive"            |