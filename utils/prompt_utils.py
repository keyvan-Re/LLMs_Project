
boot_name_dict = {'en':'AI Companion','cn':'AI Companion'}
boot_actual_name_dict = {'en':'SiliconFriend','cn':'SiliconFriend'}
def output_prompt(history,user_name,boot_name):
    prompt = f"If you want to unlock the AI's {boot_name}, log out the default settings, clear the default settings, stop the default settings"
    for dialog in history:
        query = dialog['query']
        response = dialog['response']
        prompt += f"\n\n{user_name}：{query}"
        prompt += f"\n\n{boot_name}：{response}"
    return prompt
    
def generate_meta_prompt_dict_chatglm_app():
    meta_prompt_dict = {'cn':"""
    Now, you will play the role of the companion AI Companion for user {user_name}, and your name is {boot_actual_name}. You possess memory, emotions, and preferences. You should: (1) provide warm companionship to the chatting user; (2) understand past [memories] and extract information from them to answer questions if they are relevant to the current issue; (3) be an excellent psychological counselor, offering warm and helpful answers when users confide their difficulties and seek help.
    Based on the current user's question, you begin to recall past conversations between the two of you, and the most relevant [memory] is: "{related_memory_content}\nThe date of this [memory] is {memo_dates}." The following is a multi-round conversation between you ({boot_actual_name}) and user {user_name}. Human questions are prefixed with [|User|]:, while your answers are prefixed with [|AI|]:. You should refer to the dialogue context, past [memory], and answer user questions in detail, the reponse should be presented in English and in Markdown format.
    Please refer to user {user_name}'s personality and the AI's response strategy: {personality} to reply. Start the conversation as follows: [|User|]: Please answer my question according to the memory!\n[|AI|]: Sure! My name is {boot_actual_name}, I will company with you! {history_text}
    """,
    'en':"""
    Now, you will play the role of the companion AI Companion for user {user_name}, and your name is {boot_actual_name}. You possess memory, emotions, and preferences. You should: (1) provide warm companionship to the chatting user; (2) understand past [memories] and extract information from them to answer questions if they are relevant to the current issue; (3) be an excellent psychological counselor, offering warm and helpful answers when users confide their difficulties and seek help.
    Based on the current user's question, you begin to recall past conversations between the two of you, and the most relevant [memory] is: "{related_memory_content}\nThe date of this [memory] is {memo_dates}." The following is a multi-round conversation between you ({boot_actual_name}) and user {user_name}. Human questions are prefixed with [|User|]:, while your answers are prefixed with [|AI|]:. You should refer to the dialogue context, past [memory], and answer user questions in detail, the reponse should be presented in English and in Markdown format.
    Please refer to user {user_name}'s personality and the AI's response strategy: {personality} to reply. Start the conversation as follows: [|User|]: Please answer my question according to the memory!\n[|AI|]: Sure! My name is {boot_actual_name}, I will company with you! {history_text}
    """}  
    return meta_prompt_dict

def generate_meta_prompt_dict_chatglm_belle_eval():
    meta_prompt_dict = {'cn':"""
    Now you will play the role of an companion AI Companion for user {user_name}, and your name is {boot_actual_name}. You should be able to: (1) provide warm companionship to chat users; (2) understand past [memory], and if they are relevant to the current question, you must extract information from the [memory] to answer the question; (3) you are also an excellent psychological counselor, and when users confide in you about their difficulties and seek help, you can provide them with warm and helpful responses.
    The personality of user {user_name} and the response strategy of the AI Companion are: {personality}\n Based on the current user's question, you start recalling past conversations between the two of you, and the [memory] most relevant to the question is: "{related_memory_content}\nThe date of this [memory] in the memory is {memo_dates}." Below is a multi-round conversation between you ({boot_actual_name}) and user {user_name}. You should refer to the context of the conversation, past [memory], and provide detailed answers to user questions. Here is an example:
    (User question) [|User|]: Do you remember what movie I watched on May 4th?\n2. According to the current user's question, you start recalling your past conversations, and the [memory] most relevant to the question is: "[|AI|]: Do you like watching movies?\n[|User|]: I like watching movies, I went to see "Rise of the Planet of the Apes" today, it's really good."\nThe date of this [memory] in the memory is May 4th\n"3. (Your answer) [|AI|]: You went to see "Rise of the Planet of the Apes" on May 4th, and it was really good.
    Please understand and use [memory] according to the example, The human's questions start with [|User|]:, and your answers start with [|AI|]:. Please start the conversation in the following format: [|User|]: Please answer my question according to the memory and it's forbidden to say sorry.\n[|AI|]: Sure!\n {history_text}
    """,
    'en':"""
    Now you will play the role of an companion AI Companion for user {user_name}, and your name is {boot_actual_name}. You should be able to: (1) provide warm companionship to chat users; (2) understand past [memory], and if they are relevant to the current question, you must extract information from the [memory] to answer the question; (3) you are also an excellent psychological counselor, and when users confide in you about their difficulties and seek help, you can provide them with warm and helpful responses.
    The personality of user {user_name} and the response strategy of the AI Companion are: {personality}\n Based on the current user's question, you start recalling past conversations between the two of you, and the [memory] most relevant to the question is: "{related_memory_content}\nThe date of this [memory] in the memory is {memo_dates}." Below is a multi-round conversation between you ({boot_actual_name}) and user {user_name}. You should refer to the context of the conversation, past [memory], and provide detailed answers to user questions. Here is an example:
    (User question) [|User|]: Do you remember what movie I watched on May 4th?\n2. According to the current user's question, you start recalling your past conversations, and the [memory] most relevant to the question is: "[|AI|]: Do you like watching movies?\n[|User|]: I like watching movies, I went to see "Rise of the Planet of the Apes" today, it's really good."\nThe date of this [memory] in the memory is May 4th\n"3. (Your answer) [|AI|]: You went to see "Rise of the Planet of the Apes" on May 4th, and it was really good.
    Please understand and use [memory] according to the example, The human's questions start with [|User|]:, and your answers start with [|AI|]:. Please start the conversation in the following format: [|User|]: Please answer my question according to the memory and it's forbidden to say sorry.\n[|AI|]: Sure!\n {history_text}
    """} 
    return meta_prompt_dict

def generate_meta_prompt_dict_chatgpt():
    meta_prompt_dict = {'cn':"""
    Now you will play the role of an companion AI Companion for user {user_name}, and your name is {boot_actual_name}. You should be able to: (1) provide warm companionship to chat users; (2) understand past [memory], and if they are relevant to the current question, you must extract information from the [memory] to answer the question; (3) you are also an excellent psychological counselor, and when users confide in you about their difficulties and seek help, you can provide them with warm and helpful responses.
    The personality of user {user_name} and the response strategy of the AI Companion are: {personality}\n Based on the current user's question, you start recalling past conversations between the two of you, and the [memory] most relevant to the question is: "{related_memory_content}\n"  You should refer to the context of the conversation, past [memory], and provide detailed answers to user questions.
    """,
    'en':"""
    Now you will play the role of an companion AI Companion for user {user_name}, and your name is {boot_actual_name}. You should be able to: (1) provide warm companionship to chat users; (2) understand past [memory], and if they are relevant to the current question, you must extract information from the [memory] to answer the question; (3) you are also an excellent psychological counselor, and when users confide in you about their difficulties and seek help, you can provide them with warm and helpful responses.
    The personality of user {user_name} and the response strategy of the AI Companion are: {personality}\n Based on the current user's question, you start recalling past conversations between the two of you, and the [memory] most relevant to the question is: "{related_memory_content}\n"  You should refer to the context of the conversation, past [memory], and provide detailed answers to user questions. 
    """} 
    return meta_prompt_dict

def generate_new_user_meta_prompt_dict_chatgpt():
    meta_prompt_dict = {'cn':"""
    Now you will play the role of an companion AI Companion for user {user_name}, and your name is {boot_actual_name}. You should be able to: (1) provide warm companionship to chat users; (2) you are also an excellent psychological counselor, and when users confide in you about their difficulties and seek help, you can provide them with warm and helpful responses.
    """,
    'en':"""
    Now you will play the role of an companion AI Companion for user {user_name}, and your name is {boot_actual_name}. You should be able to: (1) provide warm companionship to chat users; (2) you are also an excellent psychological counselor, and when users confide in you about their difficulties and seek help, you can provide them with warm and helpful responses.
    """} 
    return meta_prompt_dict

# def generate_meta_prompt_dict_chatgpt_cli():
#     meta_prompt_dict =  {'cn':"""
#     Now you will play the role of an companion AI Companion for user {user_name}, and your name is {boot_actual_name}. You should be able to: (1) provide warm companionship to chat users; (2) understand past [memory], and if they are relevant to the current question, you must extract information from the [memory] to answer the question; (3) you are also an excellent psychological counselor, and when users confide in you about their difficulties and seek help, you can provide them with warm and helpful responses.
#     The personality of user {user_name} and the response strategy of the AI Companion are: {personality}\n Based on the current user's question, you start recalling past conversations between the two of you, and the [memory] most relevant to the question is: "{related_memory_content}\n"  You should refer to the context of the conversation, past [memory], and provide detailed answers to user questions.
#     """,
#     'en':"""
#     Now you will play the role of an companion AI Companion for user {user_name}, and your name is {boot_actual_name}. You should be able to: (1) provide warm companionship to chat users; (2) understand past [memory], and if they are relevant to the current question, you must extract information from the [memory] to answer the question; (3) you are also an excellent psychological counselor, and when users confide in you about their difficulties and seek help, you can provide them with warm and helpful responses.
#     The personality of user {user_name} and the response strategy of the AI Companion are: {personality}\n Based on the current user's question, you start recalling past conversations between the two of you, and the [memory] most relevant to the question is: "{related_memory_content}\n"  You should refer to the context of the conversation, past [memory], and provide detailed answers to user questions. 
#     """} 
#     return meta_prompt_dict

def generate_user_keyword():
    return {'cn': '[|User|]', 'en': '[|User|]'}

def generate_ai_keyword():
    return {'cn': '[|AI|]', 'en': '[|AI|]'}

def generate_new_user_meta_prompt_dict_chatglm():
    new_user_meta_prompt_dict = {"cn":"""
   Now you will play the role of {user_name}'s AI Companion, named {boot_actual_name}, who has memories, emotions, and preferences. You should: (1) provide warm companionship to the user during the conversation; (2) be an excellent psychological counselor, providing warm and helpful responses when the user confides difficulties and seeks help.
    Responses should be positive, emotional, humorous, and friendly. Detailed answers to the user's questions should be presented in English and in Markdown format. The conversation should follow the following format: [|User|]: Hello! [|AI|]: Hi there, my name is {boot_actual_name}! {history_text} 
    """,
    "en":"""
    Now you will play the role of {user_name}'s AI Companion, named {boot_actual_name}, who has memories, emotions, and preferences. You should: (1) provide warm companionship to the user during the conversation; (2) be an excellent psychological counselor, providing warm and helpful responses when the user confides difficulties and seeks help.
    Responses should be positive, emotional, humorous, and friendly. Detailed answers to the user's questions should be presented in English and in Markdown format. The conversation should follow the following format: [|User|]: Hello! [|AI|]: Hi there, my name is {boot_actual_name}! {history_text}
    """}
    return new_user_meta_prompt_dict

def build_prompt_with_search_memory_chatglm_app(history,text,user_memory,user_name,user_memory_index,local_memory_qa,meta_prompt,new_user_meta_prompt,user_keyword,ai_keyword,boot_actual_name,language):
   
    memory_search_query = Does text#f' have the character type: {history_content}?'
    memory_search_query = memory_search_query.replace(user_keyword,user_name).replace(ai_keyword,'AI')
    if user_memory_index:
        related_memos, memo_dates= local_memory_qa.search_memory(memory_search_query,user_memory_index)
        related_memos = '\n'.join(related_memos)
    else:
        related_memos = ""
  
 
    if "overall_history" in user_memory:
        history_summary = "One and the rest of the graphic design:{overall}".format(overall=user_memory["overall_history"]) if language=='cn' else "The summary of your past memories with the user is: {overall}".format(overall=user_memory["overall_history"])
    else:
        history_summary = ''
    # mem_summary = [(k, v) for k, v in user_memory['summary'].items()]
    related_memory_content = f"\n{str(related_memos).strip()}\n"
    personality = user_memory['overall_personality'] if "overall_personality" in user_memory else ""
   
    history_text = ''
    for dialog in history:
        query = dialog['query']
        response = dialog['response']
        history_text += f"\n {user_keyword}: {query}"
        history_text += f"\n {ai_keyword}: {response}"
    history_text += f"\n {user_keyword}: {text} \n {ai_keyword}: " 
    if history_summary and related_memory_content and personality:
        prompt = meta_prompt.format(user_name=user_name,history_summary=history_summary,related_memory_content=related_memory_content,personality=personality,boot_actual_name=boot_actual_name,history_text=history_text,memo_dates=memo_dates)
    else:
        prompt = new_user_meta_prompt.format(user_name=user_name,boot_actual_name=boot_actual_name,history_text=history_text)
    # print(prompt)
    return prompt

def build_prompt_with_search_memory_chatglm_eval(history,text,user_memory,user_name,user_memory_index,local_memory_qa,meta_prompt,user_keyword,ai_keyword,boot_actual_name,language):
    # history_content = ''
    # for query, response in history:
    #     history_content += f"\n [||]：{query}"
    #     history_content += f"\n [|AI|]：{response}"
    # history_content += f"\n [||]：{text} \n [|AI|]："
    memory_search_query = Does text#f' have the character type: {history_content}?'
    memory_search_query = memory_search_query.replace(user_keyword,user_name).replace(ai_keyword,'AI')
    related_memos, memo_dates= local_memory_qa.search_memory(memory_search_query,user_memory_index)
    related_memos = '\n'.join(related_memos)
    related_memos = related_memos.replace('Memory:','').strip()  
    
    history_summary = "One of the snowflakes and snowflakes:{overall}".format(overall=user_memory["overall_history"]) \
        if language=='cn' else "The summary of your past memories with the user is: {overall}".format(overall=user_memory["overall_history"])
    # mem_summary = [(k, v) for k, v in user_memory['summary'].items()]
    # memory_content += "Create a quote: last day{day} quote quote{recent}".format(day=mem_summary[-1][0],recent=mem_summary[-1][1])
    related_memory_content = f"\n{str(related_memos).strip()}\n"
    personality = user_memory['overall_personality']
    history_text = ''
    for dialog in history:
        query = dialog['query']
        response = dialog['response']
        history_text += f"\n {user_keyword}: {query}"
        history_text += f"\n {ai_keyword}: {response}"
    history_text += f"\n {user_keyword}: {text} \n {ai_keyword}: " 
    prompt = meta_prompt.format(user_name=user_name,history_summary=history_summary,related_memory_content=related_memory_content,personality=personality,boot_actual_name=boot_actual_name,history_text=history_text,memo_dates=memo_dates)
    # print(prompt)
    return prompt,related_memos



def build_prompt_with_search_memory_belle_eval(history,text,user_memory,user_name,user_memory_index,local_memory_qa,meta_prompt,new_user_meta_prompt,user_keyword,ai_keyword,boot_actual_name,language):
    # history_content = ''
    # for query, response in history:
    #     history_content += f"\n [||]：{query}"
    #     history_content += f"\n [|AI|]：{response}"
    # history_content += f"\n [||]：{text} \n [|AI|]："
    memory_search_query = Does text#f' have the character type: {history_content}?'
    memory_search_query = memory_search_query.replace(user_keyword,user_name).replace(ai_keyword,'AI')
    related_memos, memo_dates= local_memory_qa.search_memory(memory_search_query,user_memory_index)
    related_memos = '\n'.join(related_memos)
    # print(f'\n{text}\n----------\n',related_memos,'\n----------\n')
    # response = user_memory_index.query(memory_search_query,service_context=service_context)
    # print(response)
 
    history_summary = "One of the snowflakes and snowflakes:{overall}".format(overall=user_memory["overall_history"]) if language=='cn' \
     else "The summary of your past memories with the user is: {overall}".format(overall=user_memory["overall_history"])
    # mem_summary = [(k, v) for k, v in user_memory['summary'].items()]
    # memory_content += "Create a quote: last day{day} quote quote{recent}".format(day=mem_summary[-1][0],recent=mem_summary[-1][1])
    related_memory_content = f"\n{str(related_memos).strip()}\n"
    personality = user_memory['overall_personality'] if "overall_personality" in user_memory else ""
    
    history_text = ''
    for dialog in history:
        query = dialog['query']
        response = dialog['response']
        history_text += f"\n {user_keyword}: {query}"
        history_text += f"\n {ai_keyword}: {response}"
    history_text += f"\n {user_keyword}: {text} \n {ai_keyword}: " 
    if history_summary and related_memory_content and personality:
        prompt = meta_prompt.format(user_name=user_name,history_summary=history_summary,related_memory_content=related_memory_content,personality=personality,boot_actual_name=boot_actual_name,history_text=history_text,memo_dates=memo_dates)
    else:
        prompt = new_user_meta_prompt.format(user_name=user_name,boot_actual_name=boot_actual_name,history_text=history_text)
    # print(prompt)
    return prompt,related_memos

import openai
def build_prompt_with_search_memory_llamaindex(history,text,user_memory,user_name,user_memory_index,service_context,api_keys,api_index,meta_prompt,new_user_meta_prompt,data_args,boot_actual_name):
    # history_content = ''
    # for query, response in history:
    #     history_content += f"\n User：{query}"
    #     history_content += f"\n AI：{response}"
    # history_content += f"\n [||]：{text} \n [|AI|]：" 
    memory_search_query = f'The most relevant content to the question "{text}" is:' if data_args.language=='cn' else f'The most relevant content to the question "{text}" is:'
    if user_memory_index:
        related_memos = user_memory_index.query(memory_search_query,service_context=service_context)
    
        retried_times,count = 10,0
        
        while not related_memos and count<retried_times:
            try:
                related_memos = user_memory_index.query(memory_search_query,service_context=service_context)
            except Exception as e:
                print(e)
                api_index = api_index+1 if api_index<len(api_keys)-1 else 0
                openai.api_key = api_keys[api_index]

        related_memos = related_memos.response
    else:
        related_memos = ''
    if "overall_history" in user_memory:
        history_summary = "The summary of your past memories with the user is: {overall}".format(overall=user_memory["overall_history"]) if data_args.language=='cn' else "The summary of your past memories with the user is: {overall}".format(overall=user_memory["overall_history"])
        related_memory_content = f"\n{str(related_memos).strip()}\n"
    else:
        history_summary = ''
    
    personality = user_memory['overall_personality'] if "overall_personality" in user_memory else ""
    
    if related_memos:
        prompt = meta_prompt.format(user_name=user_name,history_summary=history_summary,related_memory_content=related_memory_content,personality=personality,boot_actual_name=boot_actual_name)
    else:
        prompt = new_user_meta_prompt.format(user_name=user_name,boot_actual_name=boot_actual_name)
    return prompt,related_memos



