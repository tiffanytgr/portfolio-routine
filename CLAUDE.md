# Portfolio Routine

This repo powers a scheduled Claude Code routine that produces a daily portfolio rundown.

## Telegram Delivery

After generating the rundown, send it to Telegram using:

```bash
python send_telegram.py "message text here"
```

Requires environment variables `TELEGRAM_BOT_TOKEN` and `TELEGRAM_CHAT_ID`.
Requires `api.telegram.org` in the network egress allowlist.

## Environment Setup

The environment should run `pip install requests` as a setup step.
