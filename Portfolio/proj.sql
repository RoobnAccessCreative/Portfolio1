--linked to projects.db
CREATE TABLE IF NOT EXISTS proj(
    ID INTEGER NOT NULL PRIMARY KEY,
    name TEXT NOT NULL,
    image TEXT NOT NULL,
    logo TEXT NOT NULL,
    mainBio TEXT,
    bio TEXT,
    git TEXT,
    fig TEXT, 
    isMain BOOLEAN NOT NULL CHECK (isMain IN (0, 1)),
    date DATE CHECK (date IS strftime('%Y-%m-%d', date))
);

INSERT OR IGNORE INTO proj(ID, name, image, logo, mainbio, git, isMain, date)
 VALUES (1, 'EPIC - Unofficial Wiki', 'epicss.jpg', 'epic.png',
  'This is a wiki website for EPIC: The Musical, which implements Flask, Jinja2 and Semantic UI.',
   'EPIC-Wiki', 1, '2024-09-30');

INSERT OR IGNORE INTO proj(ID, name, image, logo, bio, git, isMain, date)
 VALUES (2, 'DEXTER 2', 'dexter2ss.jpg', 'dexter2.png',
  'A Python program using a command line interface to store and display your 6 or less Pokémon. You can also search for Pokémon to add to your account via name, id number or elemental type. It uses external assets such as Pandas and Matplotlib libraries, for dataframes and graphs  respectivley, as well as PokéAPI.',
   'Pok-dex-Project', 0, '2024-02-08');

INSERT OR IGNORE INTO proj(ID, name, image, logo, bio, git, isMain, date)
 VALUES (3, 'Coin Count', 'ccss.jpg', 'cc.png',
  '''Coin Count is a command line program that documents peoples'' progress and accuracy in sorting each type of coin into seperate bags of specific weights. This program''s main feature is its use of file handling with a .txt file to save all progression made in a given instance,  with it using dictionary data structures to store ongoing data.''',
   'Coin-Count-project', 0, '2023-11-09');




