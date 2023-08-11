import os
import openai
from xia_gpt import Gpt


class OpenaiGpt(Gpt):
    gpt_engine = openai
    gpt_engine_name = "openai"
    gpt_engine.api_key = os.environ.get("OPENAI_API_KEY")
    gpt_engine_model = "gpt-3.5-turbo"

    def chat_complete(self, system: str, message: str, context: list = None, **kwargs):
        """Give the context and

        Args:
            system: System Roles
            message: User message to be sent
            context: previous dialog to be passed as parameters as a list of conversion.
                each conversion contains user and assistant part, like: {"user": "Hello", "assistant": "World"}
            **kwargs: other parameters

        Returns:
            result and the job results
        """
        built_request = self.build_request(system=system, message=message, context=context)
        job_result = openai.ChatCompletion.create(model=self.gpt_engine_model, messages=built_request, **kwargs)
        choices = job_result.pop("choices")
        return choices[0].message["content"], job_result

    async def chat_complete_stream(self, system: str, message: str, context: list = None, **kwargs):
        """Give the context and

        Args:
            system: System Roles
            context: chat context
            message: message to be sent
            **kwargs: other parameters
        """
        built_request = self.build_request(system=system, message=message, context=context)
        total_chunks = []
        total_messages = []

        streamed_result = await openai.ChatCompletion.acreate(
            model=self.gpt_engine_model,
            messages=built_request,
            stream=True,
            **kwargs
        )
        # create variables to collect the stream of chunks
        async for chunk in streamed_result:
            total_chunks.append(chunk)
            chunk_message = chunk['choices'][0]['delta']
            total_messages.append(chunk_message)
            if "content" in chunk_message:
                print(chunk_message["content"], end="")
        print()
        full_reply_content = ''.join([m.get('content', '') for m in total_messages])
        return full_reply_content, {}


class OpenaiGpt4(OpenaiGpt):
    gpt_engine_model = "gpt-4"


if __name__ == '__main__':
    gpt_agent = OpenaiGpt()
    result, job_status = gpt_agent.chat_complete(
        "You are a helpful assistant.",
        "Where was it played?",
        [{"user": "Who won the world series in 2020?",
         "assistant": "The Los Angeles Dodgers won the World Series in 2020."}]
    )
    print(result)
    print(job_status)
