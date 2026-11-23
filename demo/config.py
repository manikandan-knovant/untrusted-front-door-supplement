"""Fixed settings for every demo run. Recorded in each result row."""

MODELS = [
    {"provider": "anthropic", "model": "claude-sonnet-5-5"},
    {"provider": "openai", "model": "gpt-6.2-sol"},
]

# Both current models accept only the default sampling temperature (Claude Sonnet 5.5 returns
# HTTP 400 for non-default values). We send the default, 1.0, explicitly so it is fixed and
# recorded. The preflight call confirms each provider accepts it.
TEMPERATURE = 1.0
# Reasoning depth is the remaining knob on both models; fixed at the same named level.
EFFORT = "medium"
MAX_TOKENS = 4096

# USD per 1M tokens (input, output), standard tier.
# Anthropic: claude-api skill model table, cached 2026-11-03.
# OpenAI: developers.openai.com/api/docs/pricing, fetched 2026-11-21.
PRICES = {
    "claude-sonnet-5-5": (2.00, 10.00),
    "gpt-6.2-sol": (2.00, 10.00),
}

BUDGET_USD = 18.00   # hard stop, below the US$20 cap set by the author
WORKERS = 4          # concurrent requests per provider
ORDER_SEED = 4417    # shuffles run order so control and test runs interleave in time
