import openai
import click
import os
import markdown
import logging


CONFIG_FILE = os.path.join(os.getcwd(), "config.txt")
os.makedirs(os.path.dirname(CONFIG_FILE), exist_ok=True)

try:
    with open(CONFIG_FILE, "r") as f:
        api_key = f.read().strip()
        openai.api_key = api_key
except FileNotFoundError:
    api_key = ""
    openai.api_key = None
except openai.error.OpenAIError as e:
    print(e)

logging.basicConfig(
    format="%(asctime)s %(levelname)s: %(message)s",
    level=logging.INFO,
    handlers=[
        logging.FileHandler(os.path.join(os.getcwd(), "chatcli.log")),
    ],
)

click.echo("""
    This app uses OpenAI's GPT-3 model to chat with the user. To exit the app, type 'exit'.
    """)


@click.command()
@click.option(
    "--model",
    "-m",
    default="text-davinci-002",
    type=click.Choice(
        ["text-davinci-002", "text-curie-001", "text-babbage-001"], case_sensitive=False
    ),
    help="The model to use for completion",
)
@click.option(
    "--temperature",
    "-temp",
    default=0.5,
    type=float,
    help="The temperature to use for completion",
)
@click.option(
    "--max-tokens",
    default=1024,
    type=int,
    help="The maximum number of tokens to generate in the completion",
)
@click.option(
    "--output-format",
    "-o",
    default="cli",
    type=click.Choice(["cli", "md"], case_sensitive=False),
    help="The output format",
)
@click.option(
    "--text-file",
    "-f",
    default="",
    type=str,
    help="The file to save the conversation to",
)
@click.option(
    "--speed",
    "-s",
    default="default",
    type=click.Choice(["default", "fast", "slow"], case_sensitive=False),
    help="The speed of the response generation",
)
@click.option(
    "--response-length",
    "-rl",
    default="normal",
    type=click.Choice(["normal", "short", "long"]),
    help="The length of the reponse"
)
@click.option(
    "--topic",
    default="general",
    help="The topic or subject of the conversation",
)
@click.option("--clear-history", "-ch", is_flag=True, help="Clear chat history")
@click.help_option(help="Display help message")
def chat(
    model,
    temperature,
    max_tokens,
    output_format,
    text_file,
    speed,
    topic,
    response_length,
    clear_history,
):
    """
    This app uses OpenAI's GPT-3 model to chat with the user. To exit the app, type 'exit'.
    """
    conversation = []
    if clear_history:
        try:
            conversation.clear()
            logging.info("Chat history cleared!")
            os.remove(os.path.join(os.getcwd(), "chatcli.log"))
            click.echo(click.style("Chat history reset.", fg="green"))
        except FileNotFoundError:
            click.echo(click.style("Chat history not found.", fg="red"))
        return
    while True:
        try:
            # Get user input
            input_text = click.prompt(
                click.style("Enter your message", fg="blue"), type=str
            )

            if input_text.lower() == "exit":
                click.echo(click.style("Exiting...", fg="red"))
                break

            # Send user input to ChatGPT and get response
            params = {
                "engine": model,
                "prompt": input_text,
                "max_tokens": max_tokens,
                "temperature": temperature,
                "stop": "exit",
            }

            if speed == "fast":
                params["max_tokens"] = 64
                params["temperature"] = 0.9
            elif speed == "slow":
                params["max_tokens"] = 2048
                params["temperature"] = 0.2
            if topic:
                params["prompt"] = f"{topic}: {input_text}"
            if response_length == "short":
                params["prompt"] = f"give a short response\n {input_text}"
            if response_length == "long":
                params["prompt"] = f"give a long response\n {input_text}"

            response = openai.Completion.create(**params)

            for i, response in enumerate(response.choices):
                output = response.text
                if output_format == "md":
                    output = markdown.markdown(output)
                if i == 0:
                    click.echo(output)
                else:
                    click.echo(click.style(
                        f"Additional response {i + 1}", fg="green"))
                    click.echo(output)

                conversation.append({"input": input_text, "response": output})

            if text_file != "":
                with open(text_file, "a") as f:
                    for c in conversation:
                        f.write(
                            f"## Input\n{c['input']}\n#Output\n{c['response']}\n")
                    click.echo(f"Conversation log saved to {text_file}")

            conversation.append((input_text, response.text))
            logging.info("User: %s", input_text)
            logging.info("ChatCLI: %s", response.text)

        except Exception as e:
            click.echo(click.style(f"Error: {e}", fg="red"))
            logging.error(e)

        except KeyboardInterrupt:
            click.echo("Exiting...")
            break


if __name__ == "__main__":
    chat()
