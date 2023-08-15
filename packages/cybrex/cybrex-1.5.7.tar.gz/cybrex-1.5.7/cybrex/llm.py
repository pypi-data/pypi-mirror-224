import logging


class LLMManager:
    def __init__(self, llm, prompter, config, max_prompt_chars, tokenizer=None):
        self.llm = llm
        self.prompter = prompter
        self.config = config
        self.max_prompt_chars = max_prompt_chars
        self.tokenizer = tokenizer

    @property
    def context_length(self):
        return self.config['context_length']

    def process(self, prompt):
        logging.getLogger('statbox').info({'action': 'process', 'mode': 'llm', 'prompt': prompt})
        if self.tokenizer:
            input_ids = self.tokenizer(prompt, return_tensors="pt")["input_ids"]
            outputs = self.llm.generate(input_ids, max_new_tokens=self.config['max_new_tokens'])
            return self.tokenizer.decode(outputs[0])
        else:
            return self.llm(prompt)
