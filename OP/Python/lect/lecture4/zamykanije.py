def say_setnence(name: str, what: str) -> None:
    def beautify(sentence: str) -> str:
        return f'{name.title()}: {sentence.lower().capitalize()}'
    print(beautify(what))

say_setnence("carl", "hello, world!")
say_setnence("gleb zernov", "you are expelled, have a nice day.")