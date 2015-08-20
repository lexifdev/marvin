import config
import marvin


def main():
    bot = marvin.Marvin(config.TOKEN)
    bot.start()


if __name__ == "__main__":
    main()

