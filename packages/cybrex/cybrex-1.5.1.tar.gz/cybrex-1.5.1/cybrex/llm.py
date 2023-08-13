import logging


class LLMManager:
    def __init__(self, llm, prompter, config, max_prompt_chars):
        self.llm = llm
        self.prompter = prompter
        self.config = config
        self.max_prompt_chars = max_prompt_chars

    @property
    def context_length(self):
        return self.config['context_length']

    def process(self, prompt):
        logging.getLogger('statbox').info({'action': 'process', 'mode': 'llm', 'prompt': prompt})
        return self.llm(prompt)
