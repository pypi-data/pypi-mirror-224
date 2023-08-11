import os
import json
import typer
from loguru import logger

from ..api_cli import APIClient, InferenceClient
from .utils import get_inf_client, do_login
from ..config import settings

app = typer.Typer()

def process_inputs(inputs: dict) -> dict:
    mods = {}
    for k,v in inputs.items():
       if v.startswith("file:"):
          v = v.replace("file:","")
          with open(v, "r") as fp:
             v = "".join(fp.readlines())
          mods[k] = v
    inputs.update(mods)
    return inputs

def assemble_template(system_msg:str , template_file:str , input_file:str) -> str:
    template_str = ""
    inputs = {}
    
    if not os.path.exists(template_file):
        logger.error("Template file %s does not exist!"%template_file)
        raise RuntimeError("Template file %s does not exist!"%template_file)

    with open(template_file, "r") as fp:
        template_str = "".join(fp.readlines())

    if input_file:
      if not os.path.exists(input_file):
        logger.error("Inputs file %s does not exist!"%input_file)
        raise RuntimeError("Inputs file %s does not exist!"%input_file)
      
      with open(input_file, "r") as fp:
        inputs.update( json.loads( "".join(fp.readlines() )))

      inputs = process_inputs(inputs)

      msg = "\n\n".join([
         system_msg,
        template_str.format(**inputs)
      ])

      return msg

@app.callback(invoke_without_command=True)
def send_message(
    msg:str ,
    model: str,
    chat_id: str = "",
    interactive: bool = False,
    collection: str = "",
    endpoint: str = typer.Option(default=settings.INFERENCE_ENDPOINT),
    inference_url: str = typer.Option(default=settings.INFERENCE_API_PATH),
    access_key: str = typer.Option(default=settings.INFERENCE_API_KEY),
    override_prompt: bool = typer.Option(default=False),
    model_temperature: float = typer.Option(default=1.0),
    template_file: str = typer.Option(default=""),
    inputs_file: str = typer.Option(default=""),
):
    """
    Send a message MSG to a MODEL

    Use --interactive to enter in a conversation loop with the agent
    Use --collection <CID> to add documents in the collection to the context of the chat

    Use --endpoint http(s)://URL:PORT to set the base endpoint url for the service
    Use --inference-url to add to the base endpoint url in case the server is not on /

    Use --access-key <TOKEN> to set the TOKEN for authorized API access

    """
    if override_prompt and template_file:
      msg = assemble_template(msg, template_file, inputs_file)

    client = get_inf_client(endpoint, inference_url)

    if not do_login(access_key, client):
        logger.error("Login failed!")
        typer.Exit(-1)

    if chat_id:
        chat_id = client.continue_chat(chat_id)
    else:
        chat_id = client.create_chat()

    logger.info(f"Chat ID: {chat_id}")

    events = client.send_message(msg, model, collection=collection, temp=model_temperature)

    print()
    print("You: %s"%(msg))
    print()
    print("Assistant: ", end="", flush=True)
    ass_reply = []
    for event in events:
        print(event, end="", flush=True)
        ass_reply.append(event)
    print()
    return ass_reply


if __name__ == "__main__":
    app()
