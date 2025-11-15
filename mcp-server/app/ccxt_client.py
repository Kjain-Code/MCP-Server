import ccxt

exchange_cache = {}

def get_exchange(name: str):
    if name not in exchange_cache:
        exchange_cache[name] = getattr(ccxt, name)({'enableRateLimit': True})
    return exchange_cache[name]


def get_ticker(exchange: str, symbol: str):
    exch = get_exchange(exchange)
    return exch.fetch_ticker(symbol)
