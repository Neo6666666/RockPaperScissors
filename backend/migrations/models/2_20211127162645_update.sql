-- upgrade --
ALTER TABLE "invite" ADD "is_closed" INT NOT NULL  DEFAULT 0;
-- downgrade --
ALTER TABLE "invite" DROP COLUMN "is_closed";
