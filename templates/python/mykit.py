"""
This program is where I will be writing my own kit of functions and classes which I use very often

Many classes and functions
"""

__author__ = 'John Rocha'
__date__ = '2024/09/25'


class Kit():
    """
    MyKit 
        Class contains class methods that are used as workhorses to perform functions that I use
        often

    """

    @staticmethod
    def get_str_input(msg: str) -> str:
        while True:
            response = input(msg).strip()
            if len(response) == 0:
                pass
            else:
                return response


def main():
    name = Kit.get_str_input('What is your name: ')
    print(name)


# > Call main ONLY when intended
if __name__ == '__main__':
    main()
