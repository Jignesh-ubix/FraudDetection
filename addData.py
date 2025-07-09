from utils.dbOperations import add_data_to_db

entries = [
    ('C1093826151', 4, 'M', 'M348934600', 'es_transportation', 4.55),
    ('C352968107', 2, 'M', 'M348934600', 'es_transportation', 39.68),
    ('C2054744914', 4, 'F', 'M1823072687', 'es_transportation', 26.89),
    ('C1760612790', 3, 'M', 'M348934600', 'es_transportation', 17.25),
    ('C757503768', 5, 'M', 'M348934600', 'es_transportation', 35.72),
    ('C1315400589', 3, 'F', 'M348934600', 'es_transportation', 25.81),
    ('C765155274', 1, 'F', 'M348934600', 'es_transportation', 9.10),
    ('C202531238', 4, 'F', 'M348934600', 'es_transportation', 21.17),
    ('C105845174', 3, 'M', 'M348934600', 'es_transportation', 32.40),
    ('C39858251', 5, 'F', 'M348934600', 'es_transportation', 35.40),
    ('C98707741', 4, 'F', 'M348934600', 'es_transportation', 14.95),
    ('C1551465414', 1, 'M', 'M1823072687', 'es_transportation', 1.51),
    ('C623601481', 3, 'M', 'M50039827', 'es_health', 68.79),
    ('C583110837', 3, 'M', 'M480139044', 'es_health', 44.26),
    ('C1332295774', 3, 'M', 'M480139044', 'es_health', 324.50),
    ('C1160421902', 3, 'M', 'M857378720', 'es_hotelservices', 176.32),
    ('C966214713', 3, 'M', 'M857378720', 'es_hotelservices', 337.41),
    ('C1450140987', 4, 'F', 'M1198415165', 'es_wellnessandbeauty', 220.11),
    ('C60026962', 2, 'F', 'M1198415165', 'es_wellnessandbeauty', 4.32)
]


add_data_to_db(entries)