# Auto-Roaster

<h3 align="center"> Friend or foe? Yay or no? Send a compliment over to tip your hat, or generate a sly roast for a laugh. All generated and automated by the latest advances in deep learning for vision-language! </h3>

<!-- GETTING STARTED -->
## Getting Started

This is an example of how you may give instructions on setting up your project locally.
To get a local copy up and running follow these simple example steps.

### Prerequisites

Using a virtual environment, use pip to download the following libraries.
* pip
  ```sh
  pip install replicate opencv-python
  pip install --upgrade openai
  ```

### Installation
(*Note: We have already provided API keys within the config file for you to use, but we still need you to manually authenticate the replicate token*)
1. Get a free Replicate API Key at [https://replicate.com/account](https://replicate.com/account), or use the one in our config file.
2. In shell, set the token as an environment variable.
   ```sh
   export REPLICATE_API_TOKEN=[token]
   ```
4. Clone the repo
   ```sh
   git clone [https://github.com/jjchilling/Auto-Roaster](https://github.com/jjchilling/Auto-Roaster)
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage
### main.py
1. In shell, run
  ```sh
  python main.py
  ```
2. The script will ask if you want a roast or compliment (type in 'roast' or 'compliment' exactly without the quotes)
3. Allow webcam access if requested.
4. After taking the photo, click any key to continue.
5. Enjoy your AI-generated comment! Comments are cached in the cachedComments file, and images are saved in the demo file.

### preloaded.py
1. 

_For samples, please refer to the demo folder.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ROADMAP -->
## Roadmap

- [ ] Feature 1
- [ ] Feature 2
- [ ] Feature 3
    - [ ] Nested Feature

See the [open issues](https://github.com/github_username/repo_name/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#readme-top">back to top</a>)</p>
