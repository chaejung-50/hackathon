import json, requests
#, "6. Tokyo Ghoul", "7. Boku no Hero Academia","8. Naruto", "9. Steins;Gate", "10. No Game No Life", "11. Kimi no Na wa",
#"12. Hunter x Hunter", "13. Angel Beats!", "14. Code Geass", "15. Toradora!
def getTopAnime():
    most_popular = ["1. Death Note", "2. Shingeki no Kyojin", "3. Fullmetal Alchemist: Brotherhood",
                    "4. Sword Art Online", "5. One Punch Man"]

    final = "The top 5 animes of all time:\n"
    for i in most_popular:
        final += i + "\n"

    return final