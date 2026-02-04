import random
# ----------------------------------------------------------------------------------
from abc import ABC ,abstractmethod
class Runnnable(ABC):
    @abstractmethod
    def invoke(input_data):
        pass


# ----------------------------------------------------------------------------------
# create LLM class
class NakliLLM(Runnnable):
    def __init__(self):
        print("LLm create")

    def invoke(input_data):
        response_list = [
            "delhi is the captital of the india",
            "IPL is the cricket league",
            "Ai stands for the aritifical Intellgence"
        ]
        return {'response':random.choice(response_list)}

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
class NakliPromptTemplate(Runnnable):
    def __init__(self,template,input_variables):
        self.template = template
        self.input_varaibles = input_variables
    
    def invoke(self,input_dict):
        return self.template.format(**input_dict)

    def format(self,input_dict):
        return self.template.format(**input_dict)
    

class RunnableConnetor(Runnnable):
    def __init__(self,runnable_list):
        self.runnable_list = runnable_list

    def invoke(self,input_data):
        for runnable in self.runnable_list:
            input_data = runnable.invoke(input_data)

        return input_data
    
template = NakliPromptTemplate(
    template="write the {length} poem about the {topic}",
    input_variables=['topic']
)


llm = NakliLLM()

chain = RunnableConnetor([template,llm])

chain.invoke({'length':'long','topic':'india'})


