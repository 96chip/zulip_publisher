__version__ = "0.1.0"

import tomli
import publisher


def main():
    with open("config.toml", mode="rb") as fp:
        config = tomli.load(fp)
    return config


test = publisher.Publisher(main()).get_subscriptions()
print(test)
