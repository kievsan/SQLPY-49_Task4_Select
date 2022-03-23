# [SQLPY-49] 4. Музыкальный сервис
# к лекции «Select-запросы, выборки из одной таблицы»
# ДЗ-2 Написать SELECT-запросы и вывести информацию


def get_tasks():
    select_list = [
        {'task': '--1. название и год выхода альбомов, вышедших в 2018 году',
         'select':
            """
            SELECT album_name Альбомы, 
                    album_release_year год_выхода
            FROM music_albums
            WHERE album_release_year = 2018 ;
        """},
        {'task': '--2. название и продолжительность самого длительного трека',
         'select':
            """
            SELECT track_name Треки, 
                    track_duration Длит_сек
            FROM music_tracks
            ORDER BY Длит_сек DESC 
            LIMIT 1
        """},
        {'task': '--3. название треков, продолжительность которых не менее 3,5 минуты',
         'select':
            """
            SELECT track_name Треки
            FROM music_tracks
            WHERE track_duration > 210 ;
        """},
        {'task': '--4. названия сборников, вышедших в период с 2018 по 2020 год включительно',
         'select':
            """
            SELECT collection_name Сборники
            FROM music_collections
            WHERE collection_release_year <= 2020 
                AND collection_release_year >= 2018 ;
        """},
        {'task': '--5. исполнители, чье имя состоит из 1 слова',
         'select':
            """
            SELECT artist_name Исполнители
                FROM music_artists
                WHERE position(' ' IN trim(artist_name)) = 0 ;
                --WHERE array_length(regexp_split_to_array(artist_name, '\\s+'), 1) = 1 ;
            """},
        {'task': "--6. название треков, которые содержат слово 'мой'/'my'",
         'select':
            """
            SELECT track_name Треки
            FROM music_tracks
            WHERE ( SELECT COUNT(*) 
                    FROM ( SELECT word 
                            FROM regexp_split_to_table(track_name, '\\s+') AS word
                            WHERE word = 'мой' OR word = 'my' ) AS my
                    ) > 0
        """}
    ]
    return select_list
