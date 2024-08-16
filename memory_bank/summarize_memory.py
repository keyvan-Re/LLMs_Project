# -*- coding: utf-8 -*-
import sys 
sys.path.append('../memory_bank')
# from azure_client import LLMClientSimple
import openai, json, os
import argparse
import copy

class LLMClientSimple:

    def __init__(self,gen_config=None):
        
        openai.api_key = os.getenv("OPENAI_API_KEY")
        
        self.disable_tqdm = False
        self.gen_config = gen_config 

    def generate_text_simple(self,prompt,prompt_num,language='en'):
        self.gen_config['n'] = prompt_num
        retry_times,count = 5,0
        response = None
        while response is None and count<retry_times:
            try:
                request = copy.deepcopy(self.gen_config)
                # print(prompt)
                if language=='cn':
                     message = [
                    {"role": "system", "content": "Below is a transcript of a conversation between a human and an AI assistant that is intelligent and knowledgeable in psychology."},
                    {"role": "user", "content": "Hello! Please help me summarize the content of the conversation."},
                    {"role": "system", "content": "Sure, I will do my best to assist you."},
                    {"role": "user", "content": f"{prompt}"}]
                else:
                    message = [
                    {"role": "system", "content": "Below is a transcript of a conversation between a human and an AI assistant that is intelligent and knowledgeable in psychology."},
                    {"role": "user", "content": "Hello! Please help me summarize the content of the conversation."},
                    {"role": "system", "content": "Sure, I will do my best to assist you."},
                    {"role": "user", "content": f"{prompt}"}]
                response = openai.ChatCompletion.create(
                    **request, messages=message)
                # print(prompt)
            except Exception as e:
                print(e)
                if 'This model\'s maximum context' in str(e):
                        cut_length = 1800-200*(count)
                        print('max context length reached, cut to {}'.format(cut_length))
                        prompt = prompt[-cut_length:]
                        response=None
                count+=1
        if response:
            task_desc = response['choices'][0]['message']['content'] #[response['choices'][i]['text'] for i in range(len(response['choices']))]
        else:
            task_desc = ''
        return task_desc
    

chatgpt_config = {"model": "gpt-3.5-turbo",
        "temperature": 0.7,
        "max_tokens": 400,
        "top_p": 1.0,
        "frequency_penalty": 0.4,
        "presence_penalty": 0.2, 
        "stop": ["<|im_end|>", "¬People¬"]
        }

llm_client = LLMClientSimple(chatgpt_config)

def summarize_content_prompt(content,user_name,boot_name,language='en'):
    prompt = 'Please summarize the following dialogue as concisely as possible, extracting the main themes and key information. If there are multiple key events, you may summarize them separately. Dialogue content:\n' if language=='cn' else 'Please summarize the following dialogue as concisely as possible, extracting the main themes and key information. If there are multiple key events, you may summarize them separately. Dialogue content:\n'
    for dialog in content:
        query = dialog['query']
        response = dialog['response']
        # prompt += f"\n用户：{query.strip()}"
        # prompt += f"\nAI：{response.strip()}"
        prompt += f"\n{user_name}：{query.strip()}"
        prompt += f"\n{boot_name}：{response.strip()}"
    prompt += ('\nSummarization：' if language=='cn' else '\nSummarization：')
    return prompt

def summarize_overall_prompt(content,language='en'):
    prompt = 'Please provide a highly concise summary of the following event, capturing the essential key information as succinctly as possible. Summarize the event:\n' if language=='cn' else "Please provide a highly concise summary of the following event, capturing the essential key information as succinctly as possible. Summarize the event:\n"
    for date,summary_dict in content:
        summary = summary_dict['content']
        prompt += (f"At {date}, the events are {summary.strip()}" if language=='cn' else f"At {date}, the events are {summary.strip()}")
    prompt += ('\nSummarization：' if language=='cn' else '\nSummarization：')
    return prompt

def summarize_overall_personality(content,language='en'):
    prompt = 'The following are the user's exhibited personality traits and emotions throughout multiple dialogues, along with appropriate response strategies for the current situation:\n' if language=='cn' else "The following are the user's exhibited personality traits and emotions throughout multiple dialogues, along with appropriate response strategies for the current situation:"
    for date,summary in content:
        prompt += (f"At {date}, the analysis shows {summary.strip()}" if language=='cn' else f"At {date}, the analysis shows {summary.strip()}")
    prompt += ('\nPlease provide a highly concise and general summary of the user's personality and the most appropriate response strategy for the AI lover, summarized as:' if language=='cn' else "Please provide a highly concise and general summary of the user's personality and the most appropriate response strategy for the AI lover, summarized as:")
    return prompt

def summarize_person_prompt(content,user_name,boot_name,language):
    prompt = f"Based on the following dialogue, please summarize {user_name}'s personality traits and emotions, and devise response strategies based on your speculation. Dialogue content:\n' if language=='cn' else f"Based on the following dialogue, please summarize {user_name}'s personality traits and emotions, and devise response strategies based on your speculation. Dialogue content:\n"
    for dialog in content:
        query = dialog['query']
        response = dialog['response']
        # prompt += f"\n用户：{query.strip()}"
        # prompt += f"\nAI：{response.strip()}"
        prompt += f"\n{user_name}：{query.strip()}"
        prompt += f"\n{boot_name}：{response.strip()}"

    prompt += (f"\n{user_name}'s personality traits, emotions, and {boot_name}'s response strategy are:' if language=='cn' else f"\n{user_name}'s personality traits, emotions, and {boot_name}'s response strategy are:")
    return prompt



def summarize_memory(memory_dir,name=None,language='cn'):
    boot_name = 'AI'
    gen_prompt_num = 1
    memory = json.loads(open(memory_dir,'r',encoding='utf8').read())
    all_prompts,all_his_prompts, all_person_prompts = [],[],[]
    for k,v in memory.items():
        if name != None and k != name:
            continue
        user_name = k
        print(f'Updating memory for user {user_name}')
        if v.get('history') == None:
            continue
        history = v['history']
        if v.get('summary') == None:
            memory[user_name]['summary'] = {}
        if v.get('personality') == None:
            memory[user_name]['personality'] = {}
        for date, content in history.items():
            # print(f'Updating memory for date {date}')
            his_flag = False if (date in v['summary'].keys() and v['summary'][date]) else True
            person_flag = False if (date in v['personality'].keys() and v['personality'][date]) else True
            hisprompt = summarize_content_prompt(content,user_name,boot_name,language)
            person_prompt = summarize_person_prompt(content,user_name,boot_name,language)
            if his_flag:
                his_summary = llm_client.generate_text_simple(prompt=hisprompt,prompt_num=gen_prompt_num,language=language)
                memory[user_name]['summary'][date] = {'content':his_summary}
            if person_flag:
                person_summary = llm_client.generate_text_simple(prompt=person_prompt,prompt_num=gen_prompt_num,language=language)
                memory[user_name]['personality'][date] = person_summary
        
        overall_his_prompt = summarize_overall_prompt(list(memory[user_name]['summary'].items()),language=language)
        overall_person_prompt = summarize_overall_personality(list(memory[user_name]['personality'].items()),language=language)
        memory[user_name]['overall_history'] = llm_client.generate_text_simple(prompt=overall_his_prompt,prompt_num=gen_prompt_num,language=language)
        memory[user_name]['overall_personality'] = llm_client.generate_text_simple(prompt=overall_person_prompt,prompt_num=gen_prompt_num,language=language)
 
    with open(memory_dir,'w',encoding='utf8') as f:
        print(f'Sucessfully update memory for {name}')
        json.dump(memory,f,ensure_ascii=False)
    return memory

if __name__ == '__main__':
    summarize_memory('../memories/eng_memory_cases.json',language='en')


                


