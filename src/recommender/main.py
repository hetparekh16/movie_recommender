from recommender.config import BASE_PATH

def run():
    return BASE_PATH.as_posix()

if __name__ == "__main__":
    print(run())