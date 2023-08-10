
from cursive import Cursive, cursive_function

@cursive_function()    
def add(a: int, b: int) -> int:
    """Add two numbers together"""
    return a + b


def main():
    cursive = Cursive(
        openai={ 'api_key': '' }
    )

    answer = cursive.ask(
        prompt='Add numbers 3 and 4',
        functions=[
            add
        ]
    )

    for k, v in answer.__dict__.items():
        print(f'{k}: {v}')
    
    answer = answer.conversation.ask(
        prompt='And whats the result of that + 543543543?',
        functions=[add]
    )

    for k, v in answer.__dict__.items():
        print(f'{k}: {v}')

if __name__ == '__main__':
    main()