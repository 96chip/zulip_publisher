import zulip
from elog import Logbook, LogbookMessageRejected, LogbookServerProblem
from loguru import logger as log


class Publisher:
    def __init__(self, config):
        self.origin_stream = config["TEST"]["origin-stream"]
        self.origin_topic = ["origin-topic"]
        self.destination_stream = ["destination-stream"]
        self.destination_topic = ["destination-topic"]
        self.zulip = zulip.Client(config_file=config["INFO"]["zulip-rc"])

    def get_subscriptions(self):
        result = self.zulip.get_subscriptions()
        print(result)
