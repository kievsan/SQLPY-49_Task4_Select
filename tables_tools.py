# [SQLPY-49] 4. ДЗ-1 ДЗ-2 Музыкальный сервис
# к лекции «Select-запросы, выборки из одной таблицы»


def create_tables(connection):
    # --СОЗДАДИМ ОТНОШЕНИЯ:
    connection.execute("""
        CREATE TABLE IF NOT EXISTS music_genres(
            genre_id SERIAL PRIMARY KEY,
            genre_name TEXT NOT NULL UNIQUE
        );
        CREATE TABLE IF NOT EXISTS music_artists(
            artist_id SERIAL PRIMARY KEY,
            artist_name TEXT NOT NULL UNIQUE
        );
        CREATE TABLE IF NOT EXISTS music_albums(
            album_id SERIAL PRIMARY KEY,
            album_name TEXT NOT NULL,
            album_release_year NUMERIC(4)
        );
        CREATE TABLE IF NOT EXISTS music_tracks(
            track_id SERIAL PRIMARY KEY,
            track_name TEXT NOT NULL,
            track_duration NUMERIC(4)
        );
        CREATE TABLE IF NOT EXISTS music_collections(
            collection_id SERIAL PRIMARY KEY,
            collection_name TEXT NOT NULL,
            collection_release_year NUMERIC(4)
        );
    """)


def create_relations(connection):
    # --ПОСТРОИМ СВЯЗИ:
    connection.execute(""" 
        --добавим в табл.треков огр-е внеш.ключа для столбца с альбомами
        ALTER TABLE music_tracks         
        ADD COLUMN album_id INTEGER  
        REFERENCES music_albums ; 
    """)
    connection.execute(""" 
        --1. создадим табл-связей для таблиц певцов и жанров
        CREATE TABLE IF NOT EXISTS relate_genre_into_artist(
            genre_id INTEGER REFERENCES music_genres(genre_id) ,
            artist_id INTEGER references music_artists(artist_id) ,
            CONSTRAINT pk_artist_into_genre PRIMARY KEY (genre_id , artist_id)
        );
        --2. создадим табл-связей для таблиц альбомов и певцов
        CREATE TABLE IF NOT EXISTS relate_artist_into_album(
            album_id INTEGER REFERENCES music_albums(album_id) ,
            artist_id INTEGER REFERENCES music_artists(artist_id) ,
            CONSTRAINT pk_artist_into_album PRIMARY KEY (album_id , artist_id)
        );
         --3. создадим табл-связей для таблиц альбомов и певцов
        CREATE TABLE IF NOT EXISTS relate_track_into_collection(
            collection_id INTEGER REFERENCES music_collections(collection_id) ,
            track_id INTEGER REFERENCES music_tracks (track_id) ,
            CONSTRAINT pk_track_into_collection PRIMARY KEY (collection_id , track_id)
        );
    """)


def drop_tables(connection):
    # --УДАЛИМ ОТНОШЕНИЯ:
    connection.execute("""
        DROP TABLE IF EXISTS relate_track_into_collection ;
        DROP TABLE IF EXISTS relate_genre_into_artist ;
        DROP TABLE IF EXISTS relate_artist_into_album ;
        
        DROP TABLE IF EXISTS music_genres ;
        DROP TABLE IF EXISTS music_tracks ;
        DROP TABLE IF EXISTS music_collections ;
        DROP TABLE IF EXISTS music_artists ;
        DROP TABLE IF EXISTS music_albums ;
    """)


def fill_tables(connection):
    # --ЗАПОЛНИМ ТАБЛИЦЫ:
    connection.execute("""
    INSERT INTO music_genres 
        (genre_id, genre_name)
    VALUES
        (1, 'жанр-1') , 
        (2, 'жанр-2') ,
        (3, 'жанр-3'), 
        (4, 'жанр-4') ,
        (5, 'жанр-5') ;
    """)

    connection.execute("""
    INSERT INTO music_collections 
        (collection_id, collection_name, collection_release_year)
    VALUES
        (1, 'сборник-1', 2020) , 
        (2, 'сборник-2', 2022) ,  
        (3, 'сборник-3', 2013) ,
        (4, 'сборник-4', 2014) ,  
        (5, 'сборник-5', 2015) ,
        (6, 'сборник-6', 2016) ,  
        (7, 'сборник-7', 2017) ,
        (8, 'сборник-8', 2018) ;
    """)

    connection.execute("""
    INSERT INTO music_artists 
        (artist_id, artist_name)
    VALUES
        (1, ' исполнитель-1') , 
        (2, 'исполнитель 2') ,  
        (3, 'исполнитель-3') ,
        (4, 'исполнитель 4') ,  
        (5, 'исполнитель-5') ,
        (6, 'исполнитель 6') ,  
        (7, 'исполнитель-7') ,
        (8, 'исполнитель 8') ;
    """)

    connection.execute("""
    INSERT INTO music_albums 
        (album_id, album_name, album_release_year)
    VALUES
        (1, 'альбом-1', 2020) , 
        (2, 'альбом-2', 2022) ,  
        (3, 'альбом-3', 2013) ,
        (4, 'альбом-4', 2014) ,  
        (5, 'альбом-5', 2015) ,
        (6, 'альбом-6', 2016) ,  
        (7, 'альбом-7', 2017) ,
        (8, 'альбом-8', 2018) ;
    """)

    connection.execute("""
    INSERT INTO music_tracks 
        (track_id, track_name, track_duration, album_id)
    VALUES
        (1, 'трек-1', 212, 1) , 
        (2, ' трек-2', 222, 2) ,  
        (3, 'трек-3', 233, 3) ,
        (4, 'трек-4', 244, 4) ,  
        (5, 'мой трек-5', 255, 5) ,
        (6, 'трек-6', 266, 6) ,  
        (7, 'мой', 277, 7) ,
        (8, 'трек-8', 288, 8) ,
        (9, 'трек-2', 312, 7) , 
        (10, 'my трек-2', 322, 6) ,  
        (11, 'трек-3', 333, 5) ,
        (12, 'немой трек-4', 344, 4) ,  
        (13, 'трек-5', 355, 3) ,
        (14, 'трек-6', 366, 2) ,  
        (15, 'трек-7', 377, 1)  ;
    """)

    connection.execute("""
    INSERT INTO relate_track_into_collection 
        (collection_id, track_id)
    VALUES
        (1, 1) , 
        (2, 2) ,  
        (3, 3) ,
        (4, 4) ,  
        (5, 5) ,
        (6, 6) ,  
        (7, 7) ,
        (8, 1) , 
        (7, 2) ,  
        (6, 3) ,
        (5, 4) ,  
        (4, 5) ,
        (3, 6) ,  
        (2, 7) ,  
        (1, 8)  ;
    """)

    connection.execute("""
    INSERT INTO relate_artist_into_album 
        (album_id, artist_id)
    VALUES
        (8, 1) , 
        (7, 2) ,  
        (6, 3) ,
        (5, 4) ,  
        (4, 5) ,
        (3, 6) ,  
        (2, 7) ,  
        (1, 8)  ;
    """)

    connection.execute("""
    INSERT INTO relate_genre_into_artist 
        (genre_id, artist_id)
    VALUES
        (1, 1) , 
        (2, 2) ,  
        (3, 3) ,
        (4, 4) ,  
        (5, 5) ,
        (4, 6) ,  
        (3, 7) ,  
        (2, 8)  ;
    """)


def selects_tasks(connection):
    select_list = list()

    task = connection.execute("""
                SELECT album_name AS название_альбома, 
                        album_release_year AS год_выхода
                FROM music_albums
                WHERE album_release_year = 2018 ;
            """)
    select_list.append(
        {'task_name': '--1. название и год выхода альбомов, вышедших в 2018 году',
         'select': task})

    task = connection.execute("""
                SELECT track_name AS название_трека, 
                        track_duration AS Длит_сек
                FROM music_tracks
                ORDER BY track_duration DESC 
                LIMIT 1 ;
            """)
    select_list.append(
        {'task_name': '--2. название и продолжительность самого длительного трека',
         'select': task})

    task = connection.execute("""
                SELECT track_name AS название_трека
                FROM music_tracks
                WHERE track_duration > 210 ;
            """)
    select_list.append(
        {'task_name': '--3. название треков, продолжительность которых не менее 3,5 минуты',
         'select': task})

    task = connection.execute("""
                SELECT collection_name AS название_сборника
                FROM music_collections
                WHERE collection_release_year <= 2020 AND collection_release_year >= 2018 ;
            """)
    select_list.append(
        {'task_name': '--4. названия сборников, вышедших в период с 2018 по 2020 год включительно',
         'select': task})

    task = connection.execute("""
                SELECT artist_name AS имя_исполнителя
                FROM music_artists
                WHERE position(' ' IN trim(artist_name)) = 0 ;
                --WHERE array_length(regexp_split_to_array(artist_name, '\\s+'), 1) = 1 ;
            """)
    select_list.append(
        {'task_name': '--5. исполнители, чье имя состоит из 1 слова',
         'select': task})

    task = connection.execute("""
                SELECT track_name AS название_трека
                FROM music_tracks
                WHERE ( SELECT COUNT(*) 
                        FROM ( SELECT word 
                            FROM regexp_split_to_table(track_name, '\\s+') AS word
                            WHERE word = 'мой' OR word = 'my' ) AS my
                    ) > 0
            """)
    select_list.append(
        {'task_name': "--6. название треков, которые содержат слово 'мой'/'my'",
         'select': task})

    return select_list

