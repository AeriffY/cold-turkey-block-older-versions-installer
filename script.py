import json
import sqlite3
import os

# change it to your own path
DATABASE_FILE = "C:/ProgramData/Cold Turkey/data-app.db"

def run_patch():
    if not os.path.exists(DATABASE_FILE):
        print(f"Error: Path not found - {DATABASE_FILE}")
        return

    try:
        with sqlite3.connect(DATABASE_FILE) as db_conn:
            cursor = db_conn.cursor()
            record = cursor.execute("SELECT value FROM settings WHERE key = 'settings'").fetchone()
            
            if not record:
                print("Error: Configuration missing.")
                return

            config_obj = json.loads(record[0])
            config_obj["additional"]["proStatus"] = "pro"
            
            cursor.execute("UPDATE settings SET value = ? WHERE key = 'settings'", (json.dumps(config_obj),))
            db_conn.commit()
            print("success")
    except Exception as err:
        print(f"Error: {err}")

if __name__ == '__main__':
    run_patch()