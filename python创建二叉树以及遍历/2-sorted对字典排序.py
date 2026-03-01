def sort_dict01():
    mydict = {'Li': ['M', 7],
              'Zhang': ['E', 2],

              'Wang': ['P', 3],

              'Du': ['C', 2],

              'Ma': ['C', 9],

              'Zhe': ['H', 7]}
    print(sorted(mydict.items(), key=lambda x: x[1][1]))  # 匿名函数”就是没有函数名的函数，通常用于实现简单的、一次性的功能。


def sort_dict02():
    gameresult = [
        {"name": "Bob", "wins": 10, "losses": 3, "rating": 75.00},
        {"name": "David", "wins": 3, "losses": 5, "rating": 57.00},
        {"name": "Carol", "wins": 4, "losses": 5, "rating": 57.00},
        {"name": "Patty", "wins": 9, "losses": 3, "rating": 71.48}]
    print(sorted(gameresult, key=lambda x: x["rating"]))


if __name__ == '__main__':
    #sort_dict01()
    sort_dict02()