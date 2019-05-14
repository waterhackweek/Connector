CREATE TABLE community (
	person_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
	person_name TEXT,
	github_id TEXT,
	orcid_id TEXT,
	hydroshare_id TEXT
);

CREATE TABLE github_cxns (
	cxn_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
	user1 TEXT NOT NULL,
	user2 TEXT NOT NULL,
	FOREIGN KEY(user1) REFERENCES community(github_id),
	FOREIGN KEY(user2) REFERENCES community(github_id)
);