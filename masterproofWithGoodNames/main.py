import os
import sys
import json
import sqlite3

from ClassClimber import Climber
from ClassMountain import Mountain
from ClassExpedition import Expedition


def read_json_file():
    fhand = open('expeditions.json', encoding="utf8") # fhand = file handeling

    expeditions_data_dict = json.load(fhand)
    fhand.close()

    return expeditions_data_dict


def configure_database(data):
    mountains = [expedition['mountain'] for expedition in data]
    set_mountains(mountains, data)


def set_mountains(mountains: list, data):
    conn = sqlite3.connect(os.path.join(sys.path[0], 'climbersapp.db'))
    conn.set_trace_callback(print)

    for mountain in mountains:
        query = f"""
                    INSERT INTO mountains (`id`, `name`, `country`, `rank`, `height`, `prominence`, `range`)
                    SELECT NULL, ?, ?, ?, ?, ?, ?
                    WHERE NOT EXISTS (SELECT 1 FROM mountains WHERE `name` LIKE '%{mountain['name']}%');
        """
        values = [
            mountain['name'],
            mountain['countries'][0],
            mountain['rank'],
            mountain['height'],
            mountain['prominence'],
            mountain['range']
        ]

        executedQuery = conn.execute(query, values)
        conn.commit()

        set_expedition(data, mountain['name'], executedQuery.lastrowid, conn)


def set_expedition(data, mountainName, mountainId, conn):
    for expedition in data:
        if expedition['mountain']['name'] == mountainName:
            query = f"""
                INSERT INTO expeditions (`id`, `name`, `mountain_id`, `start_location`, `date`, `country`, `duration`, `success`)
                SELECT ?, ?, ?, ?, ?, ?, ?, ?
                WHERE NOT EXISTS (SELECT 1 FROM expeditions WHERE id = {expedition['id']})
            """

            values = [
                expedition['id'],
                expedition['name'],
                mountainId,
                expedition['start'],
                expedition['date'],
                expedition['country'],
                expedition['duration'],
                expedition['success']
            ]

            conn.execute(query, values)
            conn.commit()

            set_climbers(conn, data, expedition)


def set_climbers(conn, data, expedition):
    for climber in expedition['climbers']:
        query = f"""
            INSERT OR IGNORE INTO climbers (id, first_name, last_name, nationality, date_of_birth)
            SELECT ?, ?, ?, ?, ?
            WHERE NOT EXISTS (SELECT 1 FROM climbers WHERE id = {expedition['id']})
        """

        values = [
            climber['id'],
            climber['first_name'],
            climber['last_name'],
            climber['nationality'],
            climber['date_of_birth']
        ]

        for value in values:
            print(type(value))

        return

        conn.execute(query, values)
        set_expedition_climber(conn, climber['id'], expedition['id'])


def set_expedition_climber(conn, climberId, expeditionId):
    query = """
        INSERT INTO expedition_climbers (climber_id, expedition_id)
        SELECT ?, ?
        WHERE NOT EXISTS (SELECT 1 FROM expedition_climbers WHERE climber_id = ? AND expedition_id = ?)
    """

    conn.execute(query, [climberId, expeditionId, climberId, expeditionId])
    conn.commit()


def truncate_table():
    conn = sqlite3.connect(os.path.join(sys.path[0], 'climbersapp.db'))
    conn.set_trace_callback(print)
    cursor = conn.cursor()

    conn.execute("DELETE FROM climbers")
    conn.execute("DELETE FROM expedition_climbers")
    conn.execute("DELETE FROM expeditions")
    conn.execute("DELETE FROM mountains")
    conn.commit()
    conn.close()

def main():
    data = read_json_file()
    configure_database(data)
    # truncate_table()
    # print(data)


if __name__ == "__main__":
    main()
