import ast
import json
import logging
import os
import pathlib
import re

import requests

logger = logging.getLogger(__name__)


class LLMFunction:
    openai_endpoint = "https://api.openai.com/v1/chat/completions"

    def __init__(
        self,
        model: str,
        temperature: float,
        function_name: str,
        description: str,
        properties: dict,
        template: str,
        openai_api_key: str = None,
    ):
        self.model = model
        self.temperature = temperature
        self.function_name = function_name
        self.description = description
        self.properties = properties
        self.template = template
        self.fields = self._detect_template_fields(self.template)

        if openai_api_key:
            self.openai_api_key = openai_api_key
        else:
            self.openai_api_key = os.environ.get("OPENAI_API_KEY", None)

        if not self.openai_api_key:
            raise ValueError(
                "No OpenAI API key provided and none found in environment variables."
            )

    @classmethod
    def from_dir(
        cls,
        dir_path: str,
        openai_api_key: str = None,
        version: str = None,
    ):
        # Convert string dir_path to pathlib.Path object
        base_path = pathlib.Path(dir_path)

        # Determine the correct sub-directory to use
        if version:
            target_dir = base_path / version
        else:
            default_dir = base_path / "default"
            if default_dir.exists() and default_dir.is_dir():
                target_dir = default_dir
            else:
                target_dir = base_path

        # Verify if target directory exists
        if not target_dir.exists() or not target_dir.is_dir():
            raise FileNotFoundError(
                f"Directory '{target_dir}' does not exist or is not a directory."
            )

        # Load template.txt
        template_path = target_dir / "template.txt"
        if not template_path.exists():
            raise FileNotFoundError(f"File '{template_path}' not found.")

        with open(template_path, "r") as f:
            template = f.read()

        # Load args.json
        args_path = target_dir / "args.json"
        if not args_path.exists():
            raise FileNotFoundError(f"File '{args_path}' not found.")

        with open(args_path, "r") as f:
            args = json.loads(f.read())

        args["template"] = template

        return cls(openai_api_key=openai_api_key, **args)

    def __call__(self, **kwargs):
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.openai_api_key}",
        }
        prompt = self._format_prompt(**kwargs)
        payload = self._get_payload(prompt=prompt)
        response_json = self._fetch_openai_completion(payload=payload, headers=headers)
        prediction = self._parse_completion(response_json=response_json)
        return prediction

    def _format_prompt(self, **kwargs) -> str:
        # Check for missing fields
        missing_fields = [field for field in self.fields if field not in kwargs]

        # Raise an error if any fields are missing
        if missing_fields:
            raise ValueError(f"Missing fields: {', '.join(missing_fields)}")

        prompt = self.template.format(**kwargs)
        return prompt

    def _get_payload(self, prompt: str) -> dict:
        function_schema = {
            "name": self.function_name,
            "description": self.description,
            "parameters": {
                "type": "object",
                "properties": self.properties,
                "required": list(self.properties.keys()),
            },
        }

        return {
            "model": self.model,
            "messages": [{"role": "user", "content": prompt}],
            "functions": [function_schema],
            "function_call": {
                "name": self.function_name,
            },
            "temperature": self.temperature,
        }

    def _fetch_openai_completion(self, payload: dict, headers: dict) -> dict:
        try:
            response = requests.post(
                self.openai_endpoint, headers=headers, json=payload
            )
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            logger.error(f"Error from OpenAI request: {e}")
            return {}

    def _parse_completion(self, response_json: dict) -> dict:
        choices = response_json.get("choices")
        if choices:
            values = choices[0]["message"]["function_call"].pop("arguments")

            try:
                prediction = ast.literal_eval(values)
            except:
                try:
                    prediction = json.loads(values)
                except Exception as e:
                    logger.error(f"Error evaluating OpenAI JSON output: {e}")
                    return None

        return prediction

    @staticmethod
    def _detect_template_fields(template: str) -> list:
        """
        Extracts format fields from a string.
        """
        fields = re.findall(r"\{(.*?)\}", template)
        return fields
