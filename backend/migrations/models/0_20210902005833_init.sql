-- upgrade --
CREATE TABLE IF NOT EXISTS "users" (
    "id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    "username" VARCHAR(20) NOT NULL UNIQUE,
    "password_hash" BLOB NOT NULL,
    "salt" BLOB NOT NULL,
    "status" VARCHAR(7) NOT NULL  DEFAULT 'Active' /* ACTIVE: Active\nIN_GAME: In Game\nOFFLINE: Offline */
);
CREATE TABLE IF NOT EXISTS "aerich" (
    "id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    "version" VARCHAR(255) NOT NULL,
    "app" VARCHAR(20) NOT NULL,
    "content" JSON NOT NULL
);
