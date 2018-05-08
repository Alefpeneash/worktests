CREATE USER docker WITH SUPERUSER PASSWORD 'docker';

CREATE SCHEMA someschema;

CREATE DATABASE somedb;

grant all privileges on database somedb to docker ;

GRANT ALL ON ALL TABLES IN SCHEMA someschema TO docker;

CREATE TABLE someschema.something ( id uuid, created_at date, updated_at date, deleted_at date);

INSERT INTO "someschema"."something" ("id","created_at","updated_at") VALUES ('47cf2dd4-67b3-1f08-26c7-4f6516680e9c','2018-04-11 09:29:43.113 +00:00','2018-04-11 09:29:43.113 +00:00') RETURNING *;

SELECT * FROM "someschema"."something";
