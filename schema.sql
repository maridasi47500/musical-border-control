CREATE TABLE  IF NOT EXISTS contacts (
	contact_id INTEGER PRIMARY KEY,
	first_name TEXT NOT NULL,
	last_name TEXT NOT NULL,
	email TEXT NOT NULL UNIQUE,
	phone TEXT NOT NULL UNIQUE
);
CREATE TABLE IF NOT EXISTS groups (
   group_id INTEGER PRIMARY KEY,
   name TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS contact_groups(
   contact_id INTEGER,
   group_id INTEGER,
   PRIMARY KEY (contact_id, group_id),
   FOREIGN KEY (contact_id) 
      REFERENCES contacts (contact_id) 
         ON DELETE CASCADE 
         ON UPDATE NO ACTION,
   FOREIGN KEY (group_id) 
      REFERENCES groups (group_id) 
         ON DELETE CASCADE 
         ON UPDATE NO ACTION
);
INSERT OR IGNORE INTO contacts (contact_id, first_name, last_name, email, phone)
VALUES( '1', 'anonyme', 'noname', 'anonymous@email.fr', '+2653546434');
INSERT OR IGNORE INTO contacts (contact_id, first_name, last_name, email, phone)
VALUES( '2', 'anne onim', 'onim', 'anne.onim@email.com', '+86877779898');
create table if not exists user(
        id integer primary key autoincrement,
        username text,
            email text,
            password text,
            country_id text,
            phone text
      , created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP                );
create table if not exists custom_officer(
        id integer primary key autoincrement,
        name text,
            country_id text
      , created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP                );
create table if not exists country(
        id integer primary key autoincrement,
        name text
      , created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP                );
create table if not exists customofficierhasuser(
        id integer primary key autoincrement,
        custom_officer_id text,
            user_id text
      , created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP                );
create table if not exists hit(
        id integer primary key autoincrement,
        artist text,
            title text
      , created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP                );
create table if not exists musicalinstrument(
        id integer primary key autoincrement,
        name text
      , created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP                );
create table if not exists userhasmusicalinstrument(
        id integer primary key autoincrement,
        musicalinstrument_id text,
            user_id text
      , created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP                );
create table if not exists userhashit(
        id integer primary key autoincrement,
        hit_id text,
            user_id text
      , created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP                );
create table if not exists userhasrythme(
        id integer primary key autoincrement,
        hit_id text,
            rythme text,
            user_id text
      , created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP                );
create table if not exists userhassignaturemusicale(
        id integer primary key autoincrement,
        motif_musical text,
            hit_id text,
            style_id text
      , created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP                );
create table if not exists style(
        id integer primary key autoincrement,
        name text
      , created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP                );
create table if not exists performance(
        id integer primary key autoincrement,
        user_id text,
            style_id text,
            artist text,
            composer text,
            title text
      , created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP                );
