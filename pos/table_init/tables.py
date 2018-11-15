STORES_QUERY = """ CREATE TABLE store
            (
                id INTEGER PRIMARY KEY ASC,
                name TEXT
            )"""

outlet = """create table outlets(
	id integer primary key,
	store_id integer not null,
	db_loc text not null,
	store_loc text not null,
	auth_key text not null
	)"""
