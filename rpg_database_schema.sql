-- Example RPG/MMORPG SQL Database Schema

CREATE TABLE characters (
    id INTEGER PRIMARY KEY,
    name TEXT,
    level INTEGER,
    exp INTEGER,
    str INTEGER,
    dex INTEGER,
    vit INTEGER,
    class TEXT,
    guild_id INTEGER
);

CREATE TABLE items (
    id INTEGER PRIMARY KEY,
    name TEXT,
    type TEXT,
    rarity TEXT,
    stats TEXT
);

CREATE TABLE inventory (
    character_id INTEGER,
    item_id INTEGER,
    quantity INTEGER,
    equipped BOOLEAN,
    PRIMARY KEY (character_id, item_id)
);

CREATE TABLE skills (
    id INTEGER PRIMARY KEY,
    name TEXT,
    description TEXT,
    power INTEGER,
    cost INTEGER
);

CREATE TABLE quests (
    id INTEGER PRIMARY KEY,
    name TEXT,
    description TEXT,
    status TEXT
);

CREATE TABLE guilds (
    id INTEGER PRIMARY KEY,
    name TEXT,
    leader_id INTEGER
);

CREATE TABLE parties (
    id INTEGER PRIMARY KEY,
    leader_id INTEGER
);

CREATE TABLE party_members (
    party_id INTEGER,
    character_id INTEGER,
    PRIMARY KEY (party_id, character_id)
);

CREATE TABLE chat (
    id INTEGER PRIMARY KEY,
    sender_id INTEGER,
    message TEXT,
    timestamp DATETIME
);
