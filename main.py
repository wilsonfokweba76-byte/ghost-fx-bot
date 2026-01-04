import time

# --- CONFIGURATION ---
SYMBOL = "US30"
TIMEFRAME = "M15"
MA_FAST = 20
MA_SLOW = 50

def get_market_data():
    """
    Simulated function. In a live environment, this connects 
    to your broker's API or a data provider.
    """
    # For now, we use these dummy values to test the logic
    # In live trading, these update every minute
    return {
        "current_price": 38500.00,
        "ma20": 38510.00,
        "ma50": 38480.00
    }

def check_for_signals():
    data = get_market_data()
    ma20 = data['ma20']
    ma50 = data['ma50']
    
    print(f"Checking {SYMBOL}... MA20: {ma20} | MA50: {ma50}")

    # BUY LOGIC: Fast MA crosses above Slow MA
    if ma20 > ma50:
        return f"🚀 GHOST BUY SIGNAL: {SYMBOL} @ {data['current_price']}"
    
    # SELL LOGIC: Fast MA crosses below Slow MA
    elif ma20 < ma50:
        return f"🔻 GHOST SELL SIGNAL: {SYMBOL} @ {data['current_price']}"
    
    return None

def main():
    print("👻 GHOST FXWILSON 2.1 ENGINE STARTED...")
    while True:
        signal = check_for_signals()
        if signal:
            print(f"!!! SIGNAL DET
