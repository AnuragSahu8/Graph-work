# from src.graphrag.graph import get_graph
from src.graphrag.chain import ask_question

# graph = get_graph()

# result = graph.query("MATCH (n) RETURN  count(n) as total")
# print(result)

def main():
    while True:
        q = input("\n Ask (type 'exit'):")
        if q.lower()=='exit':
            break

        answer = ask_question(q)
        print('\n',answer)

if __name__ == "__main__":
    main()

