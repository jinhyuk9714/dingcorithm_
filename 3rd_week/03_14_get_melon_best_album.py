def get_melon_best_album(genre_array, play_array):
    n = len(genre_array)
    genre_total_play_dict = {}
    genre_index_play_array_dict = {}

    for i in range(n):
        genre = genre_array[i]
        play = play_array[i]

        if genre in genre_total_play_dict:
            genre_total_play_dict[genre] += play
            genre_index_play_array_dict[genre].append([i, play])
        else:
            genre_total_play_dict[genre] = play
            genre_index_play_array_dict[genre] = ([i, play])

    sorted_genre_play_array = sorted(genre_total_play_dict.items(), key=lambda item: item[1], reverse=True)

    result = []
    for genre, total_play in sorted_genre_play_array:
        sorted_genre_index_play_array = sorted(genre_index_play_array_dict[genre], key=lambda item: item[1],
                                               reverse=True)
        genre_song_count = 0
        for index, play in sorted_genre_index_play_array:
            if genre_song_count >= 2:
                break
            result.append(index)
            genre_song_count += 1
    return result


print("정답 = [4, 1, 3, 0] / 현재 풀이 값 = ",
      get_melon_best_album(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]))
print("정답 = [0, 6, 5, 2, 4, 1] / 현재 풀이 값 = ",
      get_melon_best_album(["hiphop", "classic", "pop", "classic", "classic", "pop", "hiphop"],
                           [2000, 500, 600, 150, 800, 2500, 2000]))
