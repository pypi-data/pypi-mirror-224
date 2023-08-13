#!/usr/bin/env python3
import argparse
import json
import os
import readline

from atksh_utils.openai import OpenAI

blue = "\033[34m"
green = "\033[32m"
red = "\033[31m"
bold = "\033[1m"
reset = "\033[0m"


def cb(chunk, message):
    if chunk["choices"][0]["finish_reason"] is not None:
        if chunk["choices"][0]["finish_reason"] == "stop":
            print("\n")
        else:
            info = chunk["choices"][0]
            if info["finish_reason"] == "function_call":
                function_name = message["function_call"]["name"]
                function_call_args = json.loads(message["function_call"]["arguments"])
                pretty_args = []
                for arg, value in function_call_args.items():
                    if "\n" not in value:
                        pretty_args.append(f"\t{arg}={value}")
                    else:
                        pretty_args.append(f'\t{arg}=\n"""\n{value}\n"""')
                pretty_args = ",\n".join(pretty_args)
                text = f"{function_name}(\n{pretty_args}\n)"
                print(f"{bold}{blue}function_call:{reset}{blue}")
                print(text + reset)
                print()
        return
    token = chunk["choices"][0]["delta"].get("content", "")
    if token:
        print(f"{green}{token}{reset}", end="")


def setup_ai(use_gpt4: bool = False) -> OpenAI:
    key = os.getenv("OPENAI_API_KEY")
    ai = OpenAI(key, "gpt-4" if use_gpt4 else "gpt-3.5-turbo")
    ai.set_browser_functions()
    ai.set_exec_python_code_function()
    return ai


def ask():
    parser = argparse.ArgumentParser()
    parser.add_argument("query", type=str, help="The query to ask to the AI.")
    parser.add_argument("--disable-gpt4", action="store_true", help="Disable GPT-4.")
    args = parser.parse_args()
    ai = setup_ai(use_gpt4=not args.disable_gpt4)
    messages, _ = ai(args.query, stream_callback=cb, is_question=True)
    while True:
        user_prompt = input("Continue the conversation or press :q! to quit:\n>>> ")
        if user_prompt == ":q!":
            break
        print()
        messages.append({"role": "user", "content": user_prompt})
        ai.try_call(user_prompt, stream_callback=cb, messages=messages)
