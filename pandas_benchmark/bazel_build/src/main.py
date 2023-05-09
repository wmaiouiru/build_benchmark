import fire
import pandas as pd

class Runner:
    """Runner """

    @staticmethod
    def run():
        d = {'col1': [1, 4], 'col2': [3, 4], 'col3': [1, 5]}
        df = pd.DataFrame(data=d)
        return 0
if __name__ == '__main__':
  fire.Fire(Runner)