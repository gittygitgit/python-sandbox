Overview
This documents describes
- How to migrate user preferences from legacy fbms to new fbms
- How to export new fbms preferences to a spreadsheet for review or to stage preference updates.
- How to apply staged preference changes to dbFbms

Dependencies
- Python 2.7
- pyodbc module
- Setup odbc datasource for dbFbms


PREFERENCE MIGRATION
- Create directory migration
- Copy script files to ./migration/scripts
		generate_tuser_inserts.py
		generate_mapping_badge_to_tuserid.py 
		generate_tuserpref_inserts.py
		preference_codecs.py
		constants.py
- Create directory ./migration/sybase
- Copy zipped sybase export file to ./migration/sybase and explode

	Example file: tar -xzvf bcp.tar.070913
	
	Only the following files within the archive are important for the migration:	
		bcp.USERS
		bcp.PROFILES
		
- Navigate to ./migration/scripts		
- Update generate_tuser_inserts.py to point to latest bcp.USERS file
- Generate tUser insert statements
		
		python generate_tuser_inserts.py ==> migration/out/insert_tUsers.sql
		
- Run generated SQL in dbFbms

- Update generate_mapping_badge_to_tuserid.py to point to target db
- Generate mapping between badge and tUser record

		python generate_mapping_badge_to_tuserid.py ==> migration/out/badge_to_uid.txt

- Update generate_tuserpref_inserts.py to point to correct bcp.PROFILES file
- Generate tUserPreference insert statements

		python generate_tuserpref_inserts.py ==> migration/out/preferences.txt

- Run generated SQL in dbFbms


EXPORTING PREFERENCES
- TODO


CHANGING USER PREFERENCES
- TODO

APPLYING STAGED PREFERENCE CHANGES
- TODO
