<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Thanks again! Now go create something AMAZING! :D
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]


<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/larstel/MinecraftTelegramBot">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">Minecraft Telegram Bot</h3>

  <p align="center">
    Documentation
    <br />
    <a href="https://github.com/larstel/MinecraftTelegramBot"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/larstel/MinecraftTelegramBot">View Demo</a>
    ·
    <a href="https://github.com/larstel/MinecraftTelegramBot/issues">Report Bug</a>
    ·
    <a href="https://github.com/larstel/MinecraftTelegramBot/issues">Request Feature</a>
  </p>
</p>



<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgements">Acknowledgements</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

It's a bot.

### Built With

* [Python](https://python.org)


<!-- GETTING STARTED -->
## Getting Started

### Prerequisites

### Installation

1. Get a free API Key at [https://core.telegram.org/bots#6-botfather](https://core.telegram.org/bots#6-botfather)
2. Clone the repo
   ```sh
   git clone https://github.com/larstel/MinecraftTelegramBot.git
   ```
3. Install Python packages
  * [Python-Telegram-Bot](https://pypi.org/project/python-telegram-bot/)
  * [McRcon](https://pypi.org/project/mcrcon/)
4. Enter your API in `telegram_bot.py`
   ```PY
   updater = Updater("TELEGRAM_TOKEN", use_context=True)
   ```
5. Enter Minecraft Server IP-Address in `telegram_bot.py`
   ```PY
   mc_server_ip = "IP_ADDRESS"
   ```
6. Enter rcon password in `telegram_bot.py`
   ```PY
   mc_rcon_password = "PASSWORD"
   ```

<!-- USAGE EXAMPLES -->
## Usage
```sh
python3 telegram_bot.py
```

<!-- ROADMAP -->
## Roadmap

See the [open issues](https://github.com/larstel/MinecraftTelegramBot/issues) for a list of proposed features (and known issues).



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.



<!-- CONTACT -->
## Contact

Project Link: [https://github.com/larstel/MinecraftTelegramBot](https://github.com/larstel/MinecraftTelegramBot)






<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/larstel/MinecraftTelegramBot.svg?style=for-the-badge
[contributors-url]: https://github.com/larstel/MinecraftTelegramBot/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/larstel/MinecraftTelegramBot.svg?style=for-the-badge
[forks-url]: https://github.com/larstel/MinecraftTelegramBot/network/members
[stars-shield]: https://img.shields.io/github/stars/larstel/MinecraftTelegramBot.svg?style=for-the-badge
[stars-url]: https://github.com/larstel/MinecraftTelegramBot/stargazers
[issues-shield]: https://img.shields.io/github/issues/larstel/MinecraftTelegramBot.svg?style=for-the-badge
[issues-url]: https://github.com/larstel/MinecraftTelegramBot/issues
[license-shield]: https://img.shields.io/github/license/larstel/MinecraftTelegramBot.svg?style=for-the-badge
[license-url]: https://github.com/larstel/MinecraftTelegramBot/blob/master/LICENSE.txt
