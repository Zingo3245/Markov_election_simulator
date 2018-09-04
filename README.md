# Markov_election_simulator

In this project I decided to simulate elections with Markov chains. In this program elections consist of two primaries with 2 democratic candidates(Hillary Clinton vs Bernie Sanders) and 3 republican candidates(Donald Trump vs Ted Cruz vs John Kasich). After the primaries the two nominees face each other in the general election to become president. Each subsequent election pits the current president against primary challenges and a general election opponent where the incumbent president will face different odds by virtue of being an incumbent. The first election starts with Obama as the current president so none of the candidates have an incumbency factor.

## Installation and use
After cloning this repo, go to where the repo is located and run the following in bash:

```bash
pip install -r requirements.txt
python3 election.py```
