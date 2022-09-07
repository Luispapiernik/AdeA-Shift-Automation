from udea_shift_automation.bot import Bot


def main():
    bot = Bot()

    bot.search_on_youtube(query="RIsas de bebe rmix")
    bot.close()


if __name__ == "__main__":
    main()
