# Chess.com-ReadME

<div align="center">
<h1 align="center">
<img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-markdown-open.svg" width="100" />
<br>
Chess.com-Readme
</h1>
<h3 align="center">📍 Share your Chess.com Elo on your GitHub Readme page
<h3 align="center">🚀 Developed with the software and tools below.</h3>
<p align="center">

<img src="https://img.shields.io/badge/JSON-000000.svg?style=for-the-badge&logo=JSON&logoColor=white" alt="" />
<img src="https://img.shields.io/badge/AIOHTTP-2C5BB4.svg?style=for-the-badge&logo=AIOHTTP&logoColor=white" alt="click" />
<img src="https://img.shields.io/badge/Flask-000000.svg?style=for-the-badge&logo=Flask&logoColor=white" alt="txt" />
<img src="https://img.shields.io/badge/Markdown-000000.svg?style=for-the-badge&logo=Markdown&logoColor=white" alt="frozenlist" />
<img src="https://img.shields.io/badge/Python-3776AB.svg?style=for-the-badge&logo=Python&logoColor=white" alt="itsdangerous" />
<img src="https://img.shields.io/badge/Jinja-B41717.svg?style=for-the-badge&logo=Jinja&logoColor=white" alt="chess.com" />
</p>

</div>

---
## 📚 Table of Contents
- [📚 Table of Contents](#-table-of-contents)
- [📍Overview](#-introdcution)
- [⚙️ Project Structure](#project-structure)
- [🧩 Modules](#modules)
- [🏎💨 Getting Started](#-getting-started)
- [🤝 Contributing](#-contributing)
- [🪪 License](#-license)
---

## 📍Overview

The Chess.com-Readme project creates a badge for your github readme with your chess.com elo rating on it.

---

<img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-github-open.svg" width="80" />

## ⚙️ Project Structure

```bash
repo
├── app.py
├── LICENSE
├── __pycache__
│   ├── app.cpython-311.pyc
│   └── app.cpython-39.pyc
├── README.md
├── requirements.txt
├── templates
│   └── card.html.j2
└── vercel.json

2 directories, 8 files
```
---

<img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-src-open.svg" width="80" />

## 💻 Modules
<details closed><summary>Root</summary>

| File      | Summary                                                                                                                                                                                                                                                | Module    |
|:----------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:----------|
| app.py    | This code creates a web application using Flask that generates a card displaying a user 's rating on Chess.com for a specified time control . It uses the chessdotcom library to access the user 's stats and the dotenv library to access environment | app.py    |

</details>

<details closed><summary>Templates</summary>

| File         | Summary                                                                                                                                                                                                     | Module                 |
|:-------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-----------------------|
| card.html.j2 | This code creates an SVG graphic with two rectangles , one in # 555 and one in # 007ec6 , and two text elements displaying the values of the variables " time_control " and " elo " . The graphic is 139x20 | templates/card.html.j2 |

</details>
<hr />

## 🚀 Getting Started

### ✅ Prerequisites

Before you begin, ensure that you have the following prerequisites installed:
> `Register for a vercel account`

### 💻 Installation

1. Fork this repo
<img width="149" alt="Screenshot 2023-06-10 at 04 41 18" src="https://github.com/KenWuqianghao/Chess.com-Readme/assets/20444505/fbe851f9-a95f-47ad-a15d-a7e5b75deca5">

2. Go to vercel and create a new project using the forked repo
<img width="1512" alt="Screenshot 2023-06-10 at 04 41 30" src="https://github.com/KenWuqianghao/Chess.com-Readme/assets/20444505/6a59f0fe-1125-4f5e-893e-00a354f0fb91">
<img width="1512" alt="Screenshot 2023-06-10 at 04 41 41" src="https://github.com/KenWuqianghao/Chess.com-Readme/assets/20444505/2bff6c3b-5498-4970-9d98-7d2a1ad61044">

3. Specify the environment variables username and time_control, time_control has options chess_bullet, chess_blitz and chess_rapid
<img width="1512" alt="Screenshot 2023-06-10 at 04 42 08" src="https://github.com/KenWuqianghao/Chess.com-Readme/assets/20444505/fee0208a-7d3a-49d0-9103-b910941d551c">

### 🤖 Using Chess.com-Readme

```sh
<img src="link-to-your-vercel-app/?">
```

---

## 🤝 Contributing
Contributions are always welcome! Please follow these steps:
1. Fork the project repository. This creates a copy of the project on your account that you can modify without affecting the original project.
2. Clone the forked repository to your local machine using a Git client like Git or GitHub Desktop.
3. Create a new branch with a descriptive name (e.g., `new-feature-branch` or `bugfix-issue-123`).
```sh
git checkout -b new-feature-branch
```
4. Make changes to the project's codebase.
5. Commit your changes to your local branch with a clear commit message that explains the changes you've made.
```sh
git commit -m 'Implemented new feature.'
```
6. Push your changes to your forked repository on GitHub using the following command
```sh
git push origin new-feature-branch
```
7. Create a pull request to the original repository.
Open a new pull request to the original project repository. In the pull request, describe the changes you've made and why they're necessary.
The project maintainers will review your changes and provide feedback or merge them into the main branch.

---

## 🪪 License

This project is licensed under the `MIT` License. See the [LICENSE](https://docs.github.com/en/communities/setting-up-your-project-for-healthy-contributions/adding-a-license-to-a-repository) file for additional info.

---
