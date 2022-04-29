from turtle import color


print('Mad_lib_game')
print('--------------------------------------')
print('1. Me\n2. Myself\n3. Us')

choose_story = int(input('which stroy you want to part be:'))

if choose_story == 1:
    def story_1():
        animal = input('enter animal name: ')
        profession = input('enter profession name: ')
        cloth = input('enter cloth name: ')
        things = input('enter things name: ')
        name = input('enter your name: ')
        place = input('enter place name: ')
        verb = input('enter verb name: ')
        food = input('enter food name: ')

        print(f'''say {food}, the photographer said as the camera flashed! {name}
              and I had gone to {place} to get our photos taken on my birthday. The first
              photo we really wanted was a picture of us dressed as {animal} pretending
              to be a {profession}. when we saw the second photo, it was exactly what I
              wanted. We both looked like {things} wearing {cloth} and {verb} --exactly what I had in mind''')
    story_1()
elif choose_story == 2:
    def story_2():
        adjactive = input('enter adjective name: ')
        color = input('enter color name: ')
        things = input('enter things name: ')
        place = input('enter place name: ')
        person = input('enter person name: ')
        adjactive_1 = input('enter adjective_1 name: ')
        insect = input('enter insect name: ')
        food = input('enter food name: ')
        verb = input('enter verb name: ')

        print(f'''Last night I dreamed I was a {adjactive} butterfly with {color} 
            splocthes that looked like {things}.I flew to {place} with my bestfriend 
            and {person} who was a {adjactive_1} {insect}.We ate some {food} when we 
            got there and then decided to {verb} and the dream ended when I said --lets {verb}.''')
    story_2()

elif choose_story == 3:
    def story_3():
        person = input('enter person name: ')
        color = input('enter color name: ')
        food = input('enter food name: ')
        adjective = input('enter adjective name: ')
        thing = input('enter thing name: ')
        place = input('enter place name: ')
        verb = input('enter verb name: ')
        adverb = input('enter adverb name: ')
        food = input('enter food name: ')
        things = input('enter things name: ')

        print(f'''Today we picked apple from {person}'s Orchard. I had no idea 
            there were so many different varieties of apples. I ate "{color} 
            apples straight off the tree that tested like {food}. Then there 
            was a {adjective} apple that looked like a {thing}. When our bag 
            were full, we went on a free hay ride to {place} and back. It ended 
            at a hay pile where we got to {verb} {adverb}. I can hardly wait to 
            get home and cook with the apples. We are going to make appple {food} and {things} pies!.''')
    story_3()
else:
    print('\nchoose corret storyline')

input('\nPress any key to exit')
