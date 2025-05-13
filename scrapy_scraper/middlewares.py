# Middleware logic placeholder
import random

class RandomUserAgentMiddleware:
    def __init__(self, user_agents):
        self.user_agents = user_agents

    @classmethod
    def from_crawler(cls, crawler):
        return cls(user_agents=crawler.settings.get('USER_AGENTS_LIST', []))

    def process_request(self, request, spider):
        if self.user_agents:
            request.headers['User-Agent'] = random.choice(self.user_agents)


class ProxyMiddleware:
    def __init__(self, proxies):
        self.proxies = proxies

    @classmethod
    def from_crawler(cls, crawler):
        return cls(proxies=crawler.settings.get('PROXY_LIST', []))

    def process_request(self, request, spider):
        if self.proxies:
            request.meta['proxy'] = random.choice(self.proxies)
