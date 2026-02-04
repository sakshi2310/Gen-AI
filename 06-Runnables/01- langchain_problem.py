import random
# ----------------------------------------------------------------------------------

# create LLM class
class NakliLLM:
    def __init__(self):
        print("LLm create")

    def predict(self,prompt):
        response_list = [
            "delhi is the captital of the india",
            "IPL is the cricket league",
            "Ai stands for the aritifical Intellgence"
        ]
        return {'response':random.choice(response_list)}
    
llm = NakliLLM()

result = llm.predict("what is the captital of india")
print(result)

# -----------------------------------------------------------------------------

# create the prompttemplate class
class NakliPromptTemplate:
    def __init__(self,template,input_variables):
        self.template = template
        self.input_varaibles = input_variables

    def format(self,input_dict):
        return self.template.format(**input_dict)
    
template = NakliPromptTemplate(
    template="write the {length} poem about the {topic}",
    input_variables=['topic']
)

p_result = template.format({'length':'short','topic':'india'})
print(p_result)

# -----------------------------------------------------------------

# final both class work together 
prmopt = template.format({'length':'short','topic':'india'})

llm1 = NakliLLM()
final_result =  llm1.predict(prmopt)

print(final_result)

# -----------------------------------------------------------------

# create the chain class
class Naklichain:
    def __init__(self,llm,prompt):
        self.llm = llm
        self.prompt = prompt

    def run(self,input_dict):
        final_prompt = self.prompt.format(input_dict)
        result = self.llm.predict(final_prompt)

        return result['response']
    
template = NakliPromptTemplate(
    template="write the {length} poem about the {topic}",
    input_variables=['topic']
)
llm = NakliLLM()


chain = Naklichain(llm,template)
chian_resutl = chain.run({'length':'short','topic':'india'})

print("-----------------")
print(chian_resutl)