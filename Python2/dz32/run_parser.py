from parser2 import Parser


def main():
    for i in range(1, 3):
        pars = Parser(f"https://www.sport-express.ru/football/transfers/news/page{i}/", 'news.txt')
        pars.run()


if __name__ == '__main__':
    main()

