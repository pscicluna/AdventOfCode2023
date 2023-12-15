""" Advent of Code Day 2: Cube Conundrum

    --- Day 2: Cube Conundrum ---
    You're launched high into the atmosphere! The apex of your trajectory just barely reaches the surface of a large island floating in the sky. You gently land in a fluffy pile of leaves. It's quite cold, but you don't see much snow. An Elf runs over to greet you.

    The Elf explains that you've arrived at Snow Island and apologizes for the lack of snow. He'll be happy to explain the situation, but it's a bit of a walk, so you have some time. They don't get many visitors up here; would you like to play a game in the meantime?

    As you walk, the Elf shows you a small bag and some cubes which are either red, green, or blue. Each time you play this game, he will hide a secret number of cubes of each color in the bag, and your goal is to figure out information about the number of cubes.

    To get information, once a bag has been loaded with cubes, the Elf will reach into the bag, grab a handful of random cubes, show them to you, and then put them back in the bag. He'll do this a few times per game.

    You play several games and record the information from each game (your puzzle input). Each game is listed with its ID number (like the 11 in Game 11: ...) followed by a semicolon-separated list of subsets of cubes that were revealed from the bag (like 3 red, 5 green, 4 blue).

    For example, the record of a few games might look like this:

    Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
    Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
    Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
    Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
    Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
    In game 1, three sets of cubes are revealed from the bag (and then put back again). The first set is 3 blue cubes and 4 red cubes; the second set is 1 red cube, 2 green cubes, and 6 blue cubes; the third set is only 2 green cubes.

    The Elf would first like to know which games would have been possible if the bag contained only 12 red cubes, 13 green cubes, and 14 blue cubes?

    In the example above, games 1, 2, and 5 would have been possible if the bag had been loaded with that configuration. However, game 3 would have been impossible because at one point the Elf showed you 20 red cubes at once; similarly, game 4 would also have been impossible because the Elf showed you 15 blue cubes at once. If you add up the IDs of the games that would have been possible, you get 8.

    Determine which games would have been possible if the bag had been loaded with only 12 red cubes, 13 green cubes, and 14 blue cubes. What is the sum of the IDs of those games?

"""

from pathlib import Path
import numpy as np

targets = {"red": 12,
           "green": 13,
           "blue": 14}
col_inds = {"red": 0,
            "green": 1,
            "blue": 2}

test_input = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"""

if __name__ == "__main__":
    test = False
    input_file = Path(__file__).cwd().parent / "input.txt"
    with open(input_file, "r") as f:
        input_data = f.read()
    #print(test_input.split("\n").split(':').split(';'))
    games = test_input.split("\n") if test else input_data.split("\n")
    possible_games = np.ones(len(games), dtype=bool)
    #possible_games = []
    num_games = 0

    print("Part 1")
    for game in games:
        #print(game)
        if game == "":
            print(n)
            possible_games[int(n)] = False #use the last game number since indices are zero indexed but game numbers are not
            continue
        g = game.split(":")[0]
        num_games += 1
        #print(g)
        n = g.split(" ")[1]
        samples = game.split(":")[1].split(";")
        #print(g)
        for sample in samples:
            #print(sample)
            sample = sample.strip()
            #print(sample)
            colours = sample.split(",")
            for colour in colours:
                #print(colour)
                colour = colour.strip()
                #print(colour.split(" "))
                number = colour.split(" ")[0]
                #print(number)
                colour = colour.split(" ")[1]
                #print(colour)
                if int(number) > targets[colour]:
                    print("Game", n, "is impossible")
                    possible_games[int(n)-1] = False
                # else:
                #     possible_games.append(int(n))
    print(possible_games)
    # now get the indices of the possible games
    possible_games = np.where(possible_games)[0]+1
    print(possible_games)
    print(np.sum(possible_games))

    print("Part 2")
    # Now we need to find the minimum number of cubes that make the games possible
    minimum_cubes = np.zeros((3, num_games), dtype=int)
    for game in games:
        if game == "":
            continue
        g = game.split(":")[0]
        n = g.split(" ")[1]
        samples = game.split(":")[1].split(";")
        for sample in samples:
            sample = sample.strip()
            colours = sample.split(",")
            for colour in colours:
                colour = colour.strip()
                number = colour.split(" ")[0]
                colour = colour.split(" ")[1]
                if int(number) > minimum_cubes[col_inds[colour], int(n)-1]:
                    minimum_cubes[col_inds[colour], int(n)-1] = int(number)
    print(minimum_cubes)
    print(np.sum(np.prod(minimum_cubes, axis=0)))
    
            