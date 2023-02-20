def simple():
    return True

class Jude:
    def __init__(self, name, sex, genitals):
        self.name = name
        self.sex = sex
        self.genitals = genitals

    def circumcision(self):
        if self.sex == 'male':
            self.genitals *= 0.9

    def __str__(self):
        return f'Hi, I am {self.name}!'


def trush_fuu(something):
    if type(something) != Jude:
        print(f'I am not jude, I am {type(something)}. Rabbi, get the fuck off me!')
    else:
        jude = something
        if jude.sex == 'male':
            jude = something
            before = jude.genitals
            jude.circumcision()
            after = jude.genitals
            print(jude, end=' ')
            print('This is my life story', end=': ')
            print(f'before: {before}  after: {after}')
        elif jude.sex == 'female':
            print('I am sorry, but I am a woman')
        else:
            print(f'{jude.name} is fucking queer!')


if __name__ == '__main__':
    trush_fuu(1488)
    sarah = Jude(name='Sarah', sex='female', genitals='vagina')
    trush_fuu(sarah)
    joseph = Jude(name='Joseph', sex='male', genitals=12)
    trush_fuu(joseph)
    anatoliy = Jude(name='Anatoliy', sex='gfds', genitals=None)
    trush_fuu(anatoliy)


