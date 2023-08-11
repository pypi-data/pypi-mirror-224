import re
import asyncio


class Gpt:
    def __init__(self):
        pass

    @classmethod
    def extract_code_blocks(cls, message: str) -> list:
        """Extract code blocks embraced by ``` code ```

        Args:
            message:

        Returns:
            List of the dictionary with the following structure:
                * type: code type  (like python, json or might be empty)
                * body: code body  (Code)
        """
        # Regular expression pattern to find code blocks
        pattern = r"```(.*?)\n(.*?)```"

        # Find all matches in the markdown_text
        matches = re.findall(pattern, message, re.DOTALL)

        # Create a list of dictionaries from the matches
        code_blocks = [{'type': match[0], 'body': match[1]} for match in matches]

        return code_blocks

    @classmethod
    def build_request(cls, system: str, message: str, context: list = None):
        built_request = [{"role": "system", "content": system}]
        context = [] if not context else context
        for dialog in context:
            built_request.append({"role": "user", "content": dialog["user"]})
            built_request.append({"role": "user", "content": dialog["assistant"]})
        built_request.append({"role": "user", "content": message})
        return built_request

    def chat_complete(self, system: str, message: str, context: list = None, **kwargs):
        """Give the context and

        Args:
            system: System Roles
            context: chat context
            message: message to be sent
            **kwargs: other parameters
        """

    async def chat_complete_stream(self, system: str, message: str, context: list = None, **kwargs):
        """Give the context and

        Args:
            system: System Roles
            context: chat context
            message: message to be sent
            **kwargs: other parameters
        """