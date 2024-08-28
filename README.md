# HashKey Spot-Futures Arbitrage Strategy

这是一个利用HashKey Global现货和期货API进行期现套利的Python策略。欢迎交流:Telegram: @ChildrenQ

This is a Python strategy for arbitrage between HashKey Global's Spot and Futures APIs.

## 需求

- Python 3.7+
- `requests`库

## 安装

1. 克隆该存储库：

    ```bash
    git clone https://github.com/yourusername/hashkey-arbitrage-strategy.git
    cd hashkey-arbitrage-strategy
    ```

2. 安装依赖：

    ```bash
    pip install requests
    ```

## 使用

1. 在`arbitrage_strategy.py`文件中填入您的API密钥：

    ```python
    hashkey_api_key = 'YOUR_HASHKEY_API_KEY'
    hashkey_secret_key = 'YOUR_HASHKEY_SECRET_KEY'
    ```

2. 运行策略：

    ```bash
    python arbitrage_strategy.py
    ```

## 策略说明

该策略会持续监控HashKey Global现货和期货市场的价格差异，并在检测到套利机会时执行交易。

# Strategy Overview
- **Initialization**: Set up API keys and endpoints.
- **Fetch Prices**: Retrieve spot and futures prices from HashKey.
- **Calculate Arbitrage Opportunity**: Check for significant price differences.
- **Place Orders**: Execute trades to exploit the arbitrage opportunity.

# 策略概述
- **初始化**：设置API密钥和端点。
- **获取价格**：从HashKey获取现货和期货价格。
- **计算套利机会**：检查是否存在显著的价格差异。
- **下单**：在检测到套利机会时执行交易。

--- 
Feel free to submit issues and pull requests! Telegram: @ChildrenQ

