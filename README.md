<br />
<div align="center">
  <h3 align="center">Chat with a webpage</h3>

  <p align="center">
    Simple application that allows you to obtain information from a specific web page in a conversational way.
    <!--<br />-->
    <!--<a href="https://github.com/luiyiAntony/chat_with_websites"><strong>Explore the docs »</strong></a>-->
    <!--<br />-->
    <!--<br />-->
    <!--<a href="https://github.com/luiyiAntony/chat_with_websites">View Demo</a>-->
    <!--·-->
    <!--<a href="https://github.com/luiyiAntony/chat_with_websites/issues/new?labels=bug&template=bug-report---.md">Report Bug</a>-->
    <!--·-->
    <!--<a href="https://github.com/luiyiAntony/chat_with_websites/issues/new?labels=enhancement&template=feature-request---.md">Request Feature</a>-->
  </p>
</div>

<!-- TABLE OF CONTENTS -->
<details>
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
    <!--<li><a href="#usage">Usage</a></li>-->
    <!--<li><a href="#roadmap">Roadmap</a></li>-->
    <!--<li><a href="#contributing">Contributing</a></li>-->
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <!--<li><a href="#acknowledgments">Acknowledgments</a></li>-->
  </ol>
</details>

<!-- ABOUT THE PROJECT -->

## About The Project

[![App Screen Shot][app-screenshot]](https://github.com/luiyiAntony/chat_with_websites)

Application that allows you to chat with a large language model to get information about any web page you provided to it. This application uses the OpenAI's API to use the gpt-3.5 language model in order to provide relevant information for user's questions about any web page.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Built With

<!--This section should list any major frameworks/libraries used to bootstrap your project. Leave any add-ons/plugins for the acknowledgements section. Here are a few examples.-->

<!--* [![Next][Next.js]][Next-url]-->
<!--* [![React][React.js]][React-url]-->
<!--* [![Vue][Vue.js]][Vue-url]-->
<!--* [![Angular][Angular.io]][Angular-url]-->
<!--* [![Svelte][Svelte.dev]][Svelte-url]-->
<!--* [![Laravel][Laravel.com]][Laravel-url]-->
<!--* [![Bootstrap][Bootstrap.com]][Bootstrap-url]-->
<!--* [![JQuery][JQuery.com]][JQuery-url]-->

- [![Python](https://img.shields.io/pypi/pyversions/streamlit)][Python-url]
- gpt-3.5 (OpenAI)
- ChromaDB
- LangChain

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- GETTING STARTED -->

## Getting Started

<!--This is an example of how you may give instructions on setting up your project locally.-->
<!--To get a local copy up and running follow these simple example steps.-->

### Prerequisites

<!--This is an example of how to list things you need to use the software and how to install them.-->

- python3 (UBUNTU)
  ```sh
  sudo apt update
  sudo apt install python3
  ```
- python3 (WINDOWS): visit the website https://www.python.org/downloads/

### Installation

<!--_Below is an example of how you can instruct your audience on installing and setting up your app. This template doesn't rely on any external dependencies or services._-->

1. Clone the repo
   ```sh
   git clone https://github.com/luiyiAntony/chat_with_websites.git
   ```
2. Create a virtual enviroment
   ```sh
   python -m venv .venv
   ```
3. Activate virtual enviroment
   ```sh
   source .venv/bin/activate
   ```
4. Install libraries
   ```sh
   pip install -r requisitos.txt
   ```
5. Get an OpenAI API Key at [https://platform.openai.com/api-keys](https://platform.openai.com/api-keys) (learn more about it on [here](https://platform.openai.com/docs/quickstart))
6. Create a .env file and paste your API KEY
   ```.env
   OPENAI_API_KEY= 'ENTER YOUR API';
   ```
7. Run the app using streamlit
   ```sh
   streamlit run src/app.py
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- USAGE EXAMPLES -->

## Usage

<!--Use this space to show useful examples of how a project can be used. Additional screenshots, code examples and demos work well in this space. You may also link to more resources.-->

1. Add a new URL or choose one in the side-bar.
2. Start asking.

<!--_For more examples, please refer to the [Documentation](https://example.com)_-->

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- ROADMAP -->
<!--## Roadmap-->

<!--- [x] Add Changelog-->
<!--- [x] Add back to top links-->
<!--- [ ] Add Additional Templates w/ Examples-->
<!--- [ ] Add "components" document to easily copy & paste sections of the readme-->
<!--- [ ] Multi-language Support-->
<!--    - [ ] Chinese-->
<!--    - [ ] Spanish-->

<!--See the [open issues](https://github.com/othneildrew/Best-README-Template/issues) for a full list of proposed features (and known issues).-->

<!--<p align="right">(<a href="#readme-top">back to top</a>)</p>-->

<!-- CONTRIBUTING -->
<!--## Contributing-->

<!--Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.-->

<!--If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".-->
<!--Don't forget to give the project a star! Thanks again!-->

<!--1. Fork the Project-->
<!--2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)-->
<!--3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)-->
<!--4. Push to the Branch (`git push origin feature/AmazingFeature`)-->
<!--5. Open a Pull Request-->

<!--<p align="right">(<a href="#readme-top">back to top</a>)</p>-->

<!-- LICENSE -->

## License

Distributed under the MIT License. <!--See `LICENSE.txt` for more information.-->

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CONTACT -->

## Contact

Luiyi Antony Quispe Palomino - luiyiantonyqp@gmail.com

Project Link: [https://github.com/luiyiAntony/chat_with_websites](https://github.com/luiyiAntony/chat_with_websites)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- ACKNOWLEDGMENTS -->
<!--## Acknowledgments-->

<!--Use this space to list resources you find helpful and would like to give credit to. I've included a few of my favorites to kick things off!-->

<!--* [Choose an Open Source License](https://choosealicense.com)-->
<!--* [GitHub Emoji Cheat Sheet](https://www.webpagefx.com/tools/emoji-cheat-sheet)-->
<!--* [Malven's Flexbox Cheatsheet](https://flexbox.malven.co/)-->
<!--* [Malven's Grid Cheatsheet](https://grid.malven.co/)-->
<!--* [Img Shields](https://shields.io)-->
<!--* [GitHub Pages](https://pages.github.com)-->
<!--* [Font Awesome](https://fontawesome.com)-->
<!--* [React Icons](https://react-icons.github.io/react-icons/search)-->

<!--<p align="right">(<a href="#readme-top">back to top</a>)</p>-->

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->

[contributors-shield]: https://img.shields.io/github/contributors/othneildrew/Best-README-Template.svg?style=for-the-badge
[contributors-url]: https://github.com/othneildrew/Best-README-Template/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/othneildrew/Best-README-Template.svg?style=for-the-badge
[forks-url]: https://github.com/othneildrew/Best-README-Template/network/members
[stars-shield]: https://img.shields.io/github/stars/othneildrew/Best-README-Template.svg?style=for-the-badge
[stars-url]: https://github.com/othneildrew/Best-README-Template/stargazers
[issues-shield]: https://img.shields.io/github/issues/othneildrew/Best-README-Template.svg?style=for-the-badge
[issues-url]: https://github.com/othneildrew/Best-README-Template/issues
[license-shield]: https://img.shields.io/github/license/othneildrew/Best-README-Template.svg?style=for-the-badge
[license-url]: https://github.com/othneildrew/Best-README-Template/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/othneildrew
[app-screenshot]: images/screenshot.png
[Next.js]: https://img.shields.io/badge/next.js-000000?style=for-the-badge&logo=nextdotjs&logoColor=white
[Next-url]: https://nextjs.org/
[React.js]: https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB
[React-url]: https://reactjs.org/
[Vue.js]: https://img.shields.io/badge/Vue.js-35495E?style=for-the-badge&logo=vuedotjs&logoColor=4FC08D
[Vue-url]: https://vuejs.org/
[Angular.io]: https://img.shields.io/badge/Angular-DD0031?style=for-the-badge&logo=angular&logoColor=white
[Angular-url]: https://angular.io/
[Svelte.dev]: https://img.shields.io/badge/Svelte-4A4A55?style=for-the-badge&logo=svelte&logoColor=FF3E00
[Svelte-url]: https://svelte.dev/
[Laravel.com]: https://img.shields.io/badge/Laravel-FF2D20?style=for-the-badge&logo=laravel&logoColor=white
[Laravel-url]: https://laravel.com
[Bootstrap.com]: https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white
[Bootstrap-url]: https://getbootstrap.com
[JQuery.com]: https://img.shields.io/badge/jQuery-0769AD?style=for-the-badge&logo=jquery&logoColor=white
[JQuery-url]: https://jquery.com
[Python-url]: https://www.python.org/
