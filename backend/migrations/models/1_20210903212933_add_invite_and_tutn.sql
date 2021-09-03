-- upgrade --
CREATE TABLE IF NOT EXISTS "invite" (
    "id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    "uuid" CHAR(36) NOT NULL UNIQUE,
    "creator_id" INT REFERENCES "users" ("id") ON DELETE SET NULL,
    "guest_id" INT REFERENCES "users" ("id") ON DELETE SET NULL
);
CREATE INDEX IF NOT EXISTS "idx_invite_uuid_99663f" ON "invite" ("uuid");;
CREATE TABLE IF NOT EXISTS "turn" (
    "id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    "uuid" CHAR(36) NOT NULL UNIQUE,
    "result" VARCHAR(17) NOT NULL  DEFAULT 'Not Decide' /* NOT_DECIDE: Not Decide\nF_PLAYER_WIN: First Player Win\nS_PLAYER_WIN: Second Player Win\nDRAW: Draw */,
    "invite_id" INT NOT NULL REFERENCES "invite" ("id") ON DELETE CASCADE,
    "previous_turn_id" INT REFERENCES "turn" ("id") ON DELETE SET NULL
);
CREATE INDEX IF NOT EXISTS "idx_turn_uuid_757425" ON "turn" ("uuid");-- downgrade --
DROP TABLE IF EXISTS "invite";
DROP TABLE IF EXISTS "turn";
