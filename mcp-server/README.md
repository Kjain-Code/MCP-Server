MCP Crypto Data Server (Python + FastAPI)

This project is a lightweight MCP (Model Context Protocol) server built using FastAPI.
It retrieves real-time and historical cryptocurrency market data using the CCXT library.

The server exposes endpoints for:
Live market prices
Historical OHLCV data
Basic health check
This project fulfills the requirements of the internship assignment by implementing a structured, reliable, and testable MCP server.



Features
✔ Real-time crypto price
Fetches latest price, bid, ask from supported exchanges.
✔ Historical OHLCV data
Provides candle data (open, high, low, close, volume).
✔ Error Handling
Graceful handling for:
   Invalid exchanges
   Wrong symbol
   API errors
✔ FastAPI Server
Clean and modular project structure using routers.
✔ Ready for MCP Integration
Built with endpoints and clean responses suitable for LLM/MCP usage.