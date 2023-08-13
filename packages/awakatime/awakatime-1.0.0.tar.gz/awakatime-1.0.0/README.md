<div align="center">
    <h1>🔃 Awakatime</h1>
    <p>An asynchronous API wrapper for Wakatime</p>
    <a href="https://wakatime.com/badge/github/controlado/awakatime">
        <img src="https://wakatime.com/badge/github/controlado/awakatime.svg" alt="wakatime">
    </a>
    <a href="https://discordapp.com/users/854886148455399436">
        <img src="https://dcbadge.vercel.app/api/shield/854886148455399436?style=flat" alt="discord">
    </a>
    <br>
    <img src="https://img.shields.io/badge/Documentation-gray" alt="documentation">
    <img src="https://img.shields.io/badge/English-blue" alt="english">
    <img src="https://img.shields.io/badge/Português%20Brasileiro-blue" alt="português">
</div>

## Installation

```bash
pip install awakatime
```

## Usage

```python
import asyncio

from awakatime import Awakatime


async def main():
    async with Awakatime("your_api_key") as awakatime:
        await awakatime.get_all_time("your_projet")


if __name__ == "__main__":
    coro = main()
    asyncio.run(coro)
```
