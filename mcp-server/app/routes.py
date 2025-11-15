from fastapi import APIRouter, HTTPException
import ccxt

router = APIRouter()

# Global exchange instances
exchanges = {
    "binance": ccxt.binance(),
    "kraken": ccxt.kraken(),
    "coinbase": ccxt.coinbase()
}

@router.get("/price")
def get_price(symbol: str, exchange: str = "binance"):
    try:
        if exchange not in exchanges:
            raise HTTPException(status_code=400, detail="Exchange not supported")
        
        ticker = exchanges[exchange].fetch_ticker(symbol)
        return {
            "exchange": exchange,
            "symbol": symbol,
            "last_price": ticker["last"],
            "bid": ticker["bid"],
            "ask": ticker["ask"],
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/history")
def get_history(symbol: str, exchange: str = "binance", timeframe: str = "1h", limit: int = 50):
    try:
        if exchange not in exchanges:
            raise HTTPException(status_code=400, detail="Exchange not supported")
        
        exchange_client = exchanges[exchange]
        ohlcv = exchange_client.fetch_ohlcv(symbol, timeframe=timeframe, limit=limit)

        return {
            "exchange": exchange,
            "symbol": symbol,
            "timeframe": timeframe,
            "candles": ohlcv
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
