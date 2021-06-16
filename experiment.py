# -*- coding: utf-8 -*-

import pymysql

class Guild(object):
    id = 1234

class Channel(object):
    id = 4
    name = "'byungshin'"
    guild = Guild()

channel = Channel()
recent_beatmap_id = None

conn = pymysql.connect(host="localhost", user="root", db="osu_bot", password="Holyshit102!",charset="utf8", cursorclass=pymysql.cursors.DictCursor)
cur = conn.cursor()

if recent_beatmap_id is None:
    recent_beatmap_id = "NULL"

try:
    sql = f"INSERT INTO channel(id, name, guild_id, recent_beatmap_id) VALUES({channel.id}, {channel.name}, {channel.guild.id}, {recent_beatmap_id})"
    cur.execute(sql)
    conn.commit()

except:
    sql = f"UPDATE channel SET name={channel.name}, guild_id={channel.guild.id} WHERE id={channel.id}"
    cur.execute(sql)
    conn.commit()

    if recent_beatmap_id != "NULL":
        sql = f"UPDATE channel SET recent_beatmap_id={recent_beatmap_id} WHERE id={channel.id}"
        cur.execute(sql)
        conn.commit()

sql = "SELECT * FROM channel"
cur.execute(sql)
result = cur.fetchall()

print(result)

conn.close()