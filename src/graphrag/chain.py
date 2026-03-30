from langchain_core.prompts import PromptTemplate
from langchain_classic.chains import LLMChain

from src.graphrag.config import get_llm
from src.graphrag.graph import get_graph
from src.graphrag.prompts import CYPHER_QUERY_TEMPLATE,ANSWER_GENERATION_PROMPT,GRAPH_SCHEMA

# Initialize
llm = get_llm()
graph = get_graph()

# Prompt templates
cypher_prompt = PromptTemplate(
    input_variables=['schema','question'],
    template=CYPHER_QUERY_TEMPLATE
    )

answer_prompt = PromptTemplate(
    input_variables=['question','result'],
    template=ANSWER_GENERATION_PROMPT,
)

cypher_chain = LLMChain(llm=llm,prompt=cypher_prompt)
answer_chain = LLMChain(llm=llm,prompt=answer_prompt)

def ask_question(question:str):

    print(f"\nQuestion: {question}")

    # Step1: Generate Cypher
    cypher_result = cypher_chain.invoke({
        'schema':GRAPH_SCHEMA,
        'question': question
    })
    
    cypher_query = cypher_result if isinstance(cypher_result, str) else cypher_result.get('text', str(cypher_result))
    cypher_query = cypher_query.strip()

    # Remove markdown code blocks if present
    if cypher_query.startswith('```'):
        cypher_query = cypher_query.split('```')[1]
        if cypher_query.startswith('cypher'):
            cypher_query = cypher_query[7:]  # Remove 'cypher' from start
        cypher_query = cypher_query.strip()

    print(f'\nGenerated Cypher:\n{cypher_query}')

    #Step2: Execute
    try:
        result = graph.query(cypher_query)
    except Exception as e:
        return f"Error:{str(e)}"
    
    print(f'\nRaw Result:\n{result}')

    #Step3: Answer
    answer_result = answer_chain.invoke({
        'question':question,
        'result':str(result),
    })
    
    answer = answer_result if isinstance(answer_result, str) else answer_result.get('text', str(answer_result))

    return answer.strip()
    



