Your Command Line ChatGPT.

# Setup

1. clone this repo
2. pip3 install -U -r requirements.txt
3. get your apikey from <https://platform.openai.com/account/api-keys> and put it in `config.txt`

# Run
```sh
~/chatcli$ python3 main.py --help

Options:
  -m, --model [text-davinci-002|text-curie-001|text-babbage-001]
                                  The model to use for completion
  -temp, --temperature FLOAT      The temperature to use for completion
  --max-tokens INTEGER            The maximum number of tokens to generate in
                                  the completion
  -o, --output-format [cli|md]    The output format
  -f, --text-file TEXT            The file to save the conversation to
  -s, --speed [default|fast|slow]
                                  The speed of the response generation
  -rl, --response-length [normal|short|long]
                                  The length of the reponse
  --topic TEXT                    The topic or subject of the conversation
  -ch, --clear-history            Clear chat history
  --help                          Display help message 
```

# Feature

- [x] Model selection
- [x] Output format Selection
- [x] Text file saving
- [x] Chat history clearing
- [x] Response length


# LINK

- https://platform.openai.com/docs/introduction
- https://platform.openai.com/docs/api-reference/completions
- https://platform.openai.com/account/api-keys
