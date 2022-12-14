from pico2d import *
import character
import background
import enemy
import game_framework
import game_world
import lobby
import stop
import item
import attack
import dead

running = None
font = None
play_time = None
minute = None
second = None
back = None
pause_image = None
def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.push_state(stop)
        else:
            character.handle_events(event)


def enter():
    global running, font, minute, second, back, pause_image
    running = True
    font = load_font('JejuHallasan.ttf', 32)
    pause_image = load_image('pause.png')
    minute, second = 0, 0
    character.enter()
    back = background.InfiniteBackground()
    game_world.add_object(back, 0)
    enemy.enter()
    item.enter()

def exit():
    pass

def draw():
    global minute, second
    clear_canvas()
    #background.draw()
    for game_object in game_world.all_objects():
        game_object.draw()

    font.draw(568, 850, f'{minute} : {second}', (0, 0, 0))
    pause_image.clip_draw(0, 0, 328, 328, 1160, 860, 80, 80)
    update_canvas()

def update():
    global play_time, minute, second
    play_time = get_time() - lobby.play_time
    minute = int(play_time // 60)
    second = int(play_time % 60)
   # background.update()
    for game_object in game_world.all_objects():
        game_object.update()

    collide()

    enemy.make_enemy()
    enemy.check_enemy()
    #delay(0.016)

def pause():
    pass

def resume():
    pass

def collide():
    for ene in enemy.enemys:
        if character.hit_time <= 0:
                if character.hero.rect.collide_rect_to_circle(ene.circle):
                    character.hero.hp -= enemy.enemy_damage
                    character.Hero.sound.play()
                    if character.hero.hp <= 0 and character.hero.die == False:
                        character.hero.die = True
                        character.hero.image_x = 40
                        character.hero.image_y = 70
                        character.hero.frame = 0
                        character.now_image = character.die_image
                    back.hit = True
                    back.hitcnt = 0
                    character.hit_time = 1.0
        if character.skill_e.circle.collide_circle_to_circle(ene.circle):
                ene.hp -= attack.skill_e_damage * game_framework.frame_time
    if character.hero.die == True and character.hero.frame >= 4:
        back.bgm.stop()
        game_framework.change_state(dead)

    for it in item.items[:]:
        if character.hero.rect.collide_rect_to_rect(it.rect):
            if character.hero.hp < character.hero_hp:
                character.hero.hp += 20
            if character.hero.hp > character.hero_hp:
                character.hero.hp = character.hero.hp
            item.items.remove(it)
            game_world.remove_object(it)
            
    for normal in character.normal_bullet[:]:
        if(normal.circle.x > character.hero.rect.x + 600
         or normal.circle.x < character.hero.rect.x - 600
          or normal.circle.y > character.hero.rect.y + 450
           or normal.circle.y < character.hero.rect.y - 450):
            character.normal_bullet.remove(normal)
            game_world.remove_object(normal) 
        else:
            for ene in enemy.enemys:
                if(normal.circle.collide_circle_to_circle(ene.circle)):
                    ene.hp -= attack.normal_bullet_damage
                    character.normal_bullet.remove(normal)
                    game_world.remove_object(normal)
                    break

    for q in character.skill_q[:]:
        if(q.circle.x > character.hero.rect.x + 600
         or q.circle.x < character.hero.rect.x - 600
          or q.circle.y > character.hero.rect.y + 450
           or q.circle.y < character.hero.rect.y - 450):
            character.skill_q.remove(q)
            game_world.remove_object(q)
        else:
            for ene in enemy.enemys:
                if(q.circle.collide_circle_to_circle(ene.circle)):
                    ene.hp -= attack.skill_q_damage
                    character.skill_q.remove(q)
                    game_world.remove_object(q)
                    break

    for w in character.skill_w[:]:
        if int(w.frame) >= 6:
            character.skill_w.remove(w)
            game_world.remove_object(w)
            continue


    for a in character.skill_r[:]:
        if a.move_rate_y >= a.circle.y and a.isexplo == False:
            attack.Skill_R.explosion_sound.play()
            a.circle.r = 300
            for ene in enemy.enemys:
                if a.circle.collide_circle_to_circle(ene.circle):
                    ene.hp -= attack.skill_r_damage
            a.frame = -1
            a.isexplo = True
        if not a.isuse:
            character.skill_r.remove(a)
            game_world.remove_object(a)
