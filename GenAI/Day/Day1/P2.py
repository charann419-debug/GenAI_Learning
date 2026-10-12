#functions:
def build_prompt(topic:str,word_limit:int=150)->str:
    return f"write about {topic},with under {word_limit} words"

print(build_prompt("gen ai"))
print(build_prompt("prompt engineering",word_limit=300))

#brushup following concepts:
#*args,**kwargs
#list comprehension,dict comprehension