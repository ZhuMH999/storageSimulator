import pygame
import storageSim
from storageSim.constants import GRASS, CRATE, FONT, FONT2, FONT3, UNLOAD_FLOOR
import time
import random

WIDTH, HEIGHT = 800, 800
SQUARE_WIDTH = 75

MAP_X = 31
MAP_Y = 22

game_map = ['8', '8', '8', '8', '8', '8', '8', '8', '8', '8', '8', '8', '8', '8', '8', '8', '8', '8', '8', '8', '8', '8', '8', '8', '8', '8', '8', '8', '8', '8', '8',
            '8', '8', '8', '8', '8', '8', '8', '8', '8', '8', '8', '8', '8', '8', '8', '8', '8', '8', '8', '8', '8', '8', '8', '8', '8', '8', '8', '8', '8', '8', '8',
            '0', '0', '0;W3TLC,9', '0;W3H2,9', '0;W3H2,9', '0;W3H2,9', '0;W3TLC,8;W3H2,9', '0;W3H2,8', '0;W3H2,8', '0;W3H2,8', '0;W3H2,8', '0;W3H2,8', '0;W3R3,8', '2', '2', '9', '9', '9', '9', '2', '2', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0',
            '0', '0', '0;W3V2,9', '0;1,9', '0;1,9', '0;1,9', '0;W3V2,8;1,9', '0;1,8', '0;1,8', '0;1,8', '0;1,8', '0;1,8', '0;1,8', '2', '2', '9', '9', '9', '9', '2', '2', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0',
            '0', '0', '0;W3V2,9', '0;1,9', '0;1,9', '0;1,9', '0;W3V2,8;1,9', '0;1,8', '0;1,8', '0;1,8', '0;1,8', '0;1,8', '0;1,8', '2', '2', '2', '2', '2', '2', '2', '2', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0',
            '0', '0', '0;W3V2,9', '0;1,9', '0;1,9', '0;1,9', '0;W3V2,8;1,9', '0;1,8', '0;1,8', '0;1,8', '0;1,8', '0;1,8', '0;W3T3,8', '2', '2', '2', '2', '2', '2', '2', '2', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0',
            '0', '0', '0;W3V2,9', '0;1,9', '0;1,9', '0;1,9', '0;W3TLC,6;W3RUD,8;W3L3,9', '0;W3H2,6', '0;W3H2,6', '0;W3TLC,5;W3H2,6', '0;W3H2,5', '0;W3H2,5', '0;W3H2,5;W3LRU,8', 'W3TLC;W3LRD,5', 'W3H2', 'W3R3', '1', '1', 'W3L3', 'W3H2', 'W3TRC;W3H2,1', '0;W3H2,1', '0;W3H2,1', '0;W3H2,1', '0;W3TRC,1', '0', '0', '0', '0', '0', '0',
            '0', '0', '0;W3V2,9', '0;1,9', '0;1,9', '0;1,9', '0;W3V2,6;1,9', '0;1,6', '0;1,6', '0;W3V2,5;1,6', '0;1,5', '0;1,5', '0;1,5', 'W3V2;W3B3,5', '1', '1', '1', '1', '1', '1', 'W3V2;1,1', '0;1,1', '0;1,1', '0;1,1', '0;W3V2,1', '0', '0', '0', '0', '0', '0',
            '0', '0', '0;W3V2,9', '0;1,9', '0;1,9', '0;1,9', '0;W3V2,6;1,9', '0;1,6', '0;1,6', '0;W3V2,5;1,6', '0;1,5', '0;1,5', '0;1,5', 'W3V2;1,5', '1', '1', '1', '1', '1', '1', 'W3V2;1,1', '0;1,1', '0;1,1', '0;1,1', '0;W3V2,1', '0', '0', '0', '0', '0', '0',
            '0', '0', '0;W3BLC,9', '0;W3H2,9', '0;W3H2,9', '0;W3H2,9', '0;W3V2,6;W3TRC,9', '0;1,6', '0;1,6', '0;W3V2,5;1,6', '0;1,5', '0;1,5', '0;1,5', 'W3V2;1,5', '1', '1', '1', '1', '1', '1', 'W3V2;W3TLC,1;W3T3,3', '0;W3H2,1;1,3', '0;W3H2,1;1,3', '0;W3H2,1;1,3', '0;W3BRC,1;W3V2,3', '0', '0', '0', '0', '0', '0',
            '0', '0', '0', '0', '0', '0', '0;W3V2,6', '0;1,6', '0;1,6', '0;W3V2,5;1,6', '0;1,5', '0;1,5', '0;1,5', 'W3V2;W3T3,5', '1', '1', '1', '1', '1', '1', 'W3V2', '0;1,3', '0;1,3', '0;1,3', '0;W3V2,3', '0', '0', '0', '0', '0', '0',
            '0', '0', '0', '0', '0', '0', '0;W3V2,6', '0;1,6', '0;1,6', '0;W3V2,5;1,6', '0;1,5', '0;1,5', '0;1,5', 'W3V2', '1', '1', '1', '1', '1', '1', 'W3V2', '0;1,3', '0;1,3', '0;1,3', '0;W3V2,3', '0', '0', '0', '0', '0', '0',
            '0', '0', '0', '0', '0', '0', '0;W3BLC,6;W3V2,7', '0;W3H2,6;1,7', '0;W3H2,6;1,7', '0;W3BLC,5;W3H2,6;1,7', '0;W3H2,5;1,7', '0;W3H2,5;1,7', '0;W3H2,5;1,7', 'W3BLC;W3LRU,5;W3BLC,7', 'W3H2;W3TRC,2;W3R3,7', 'W3H2;1,2', 'W3H2;1,2', 'W3H2;1,2', 'W3H2;W3TLC,2;W3L3,4', 'W3H2', 'W3BRC;W3LRU,3;W3BRC,4', '0;W3H2,3;1,4', '0;W3H2,3;1,4', '0;W3H2,3;1,4', '0;W3BRC,3;W3V2,4', '0', '0', '0', '0', '0', '0',
            '0', '0', '0', '0', '0', '0', '0;W3V2,7', '0;1,7', '0;1,7', '0;1,7', '0;1,7', '0;1,7', '0;1,7', '0;1,7', '0;W3V2,2;1,7', '0;1,2', '0;1,2', '0;1,2', '0;W3V2,2;1,4', '0;1,4', '0;1,4', '0;1,4', '0;1,4', '0;1,4', '0;W3V2,4', '0', '0', '0', '0', '0', '0',
            '0', '0', '0', '0', '0', '0', '0;W3V2,7', '0;1,7', '0;1,7', '0;1,7', '0;1,7', '0;1,7', '0;1,7', '0;1,7', '0;W3V2,2;1,7', '0;1,2', '0;1,2', '0;1,2', '0;W3V2,2;W3T3,4', '0;1,4', '0;1,4', '0;1,4', '0;1,4', '0;1,4', '0;W3V2,4', '0', '0', '0', '0', '0', '0',
            '0', '0', '0', '0', '0', '0', '0;W3BLC,7', '0;W3H2,7', '0;W3H2,7', '0;W3H2,7', '0;W3H2,7', '0;W3H2,7', '0;W3H2,7', '0;W3H2,7', '0;W3BLC,2;W3H2,7', '0;W3H2,2', '0;W3H2,2', '0;W3H2,2', '0;W3BRC,2;W3LRU,4', '0;W3H2,4', '0;W3H2,4', '0;W3H2,4', '0;W3H2,4', '0;W3H2,4', '0;W3BRC,4', '0', '0', '0', '0', '0', '0',
            '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0',
            '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0',
            '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0',
            '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0',
            '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0',
            '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0']

game_map_price = [490, 490, 490, 1280, 1280, 1300, 4800, 9000, 10000]


class View:
    def __init__(self, window, player, boxes):
        self.window = window
        self.player = player
        self.boxes = boxes

    def draw(self):
        self.window.fill('black')
        for i in range(MAP_Y):
            for j in range(MAP_X):
                if -100 < ((j - self.player.xpos)*SQUARE_WIDTH)+362.5 < 900 and -100 < ((i - self.player.ypos)*SQUARE_WIDTH)+362.5 < 900:
                    item_to_load = ''
                    if len(game_map[i*MAP_X + j].split(';')) == 1:
                        item_to_load = game_map[i*MAP_X + j]
                    else:
                        for item in range(len(game_map[i*MAP_X + j].split(';'))):
                            if item == 0:
                                item_to_load = game_map[i*MAP_X + j].split(';')[item]
                            else:
                                if int(game_map[i*MAP_X + j].split(';')[item].split(',')[1]) <= self.player.current_map:
                                    item_to_load = game_map[i*MAP_X + j].split(';')[item].split(',')[0]

                    if item_to_load == '0':
                        self.window.blit(GRASS, (((j - self.player.xpos)*SQUARE_WIDTH)+362.5, ((i - self.player.ypos)*SQUARE_WIDTH)+362.5))
                    elif item_to_load == '1':
                        pygame.draw.rect(self.window, (150, 150, 150), (((j - self.player.xpos)*SQUARE_WIDTH)+362.5, ((i - self.player.ypos)*SQUARE_WIDTH)+362.5, SQUARE_WIDTH, SQUARE_WIDTH))
                    elif '3' in item_to_load:
                        self.window.blit(getattr(storageSim.constants, item_to_load), (((j - self.player.xpos)*SQUARE_WIDTH)+362.5, ((i - self.player.ypos)*SQUARE_WIDTH)+362.5))
                    elif item_to_load == '2':
                        pygame.draw.rect(self.window, (120, 120, 120), (((j - self.player.xpos) * SQUARE_WIDTH) + 362.5, ((i - self.player.ypos) * SQUARE_WIDTH) + 362.55, SQUARE_WIDTH, SQUARE_WIDTH))
                    elif item_to_load == '8':
                        pygame.draw.rect(self.window, (0, 0, 0), (((j - self.player.xpos)*SQUARE_WIDTH)+362.5, ((i - self.player.ypos)*SQUARE_WIDTH)+362.5, SQUARE_WIDTH, SQUARE_WIDTH))
                    elif item_to_load == '9':
                        self.window.blit(UNLOAD_FLOOR, (((j - self.player.xpos)*SQUARE_WIDTH)+362.5, ((i - self.player.ypos)*SQUARE_WIDTH)+362.5))

        for box in range(len(self.boxes.box)):
            if self.boxes.box[box][3]:
                self.window.blit(CRATE, (((self.boxes.box[box][0] - self.player.xpos) * SQUARE_WIDTH) + 362.5, ((self.boxes.box[box][1] - self.player.ypos) * SQUARE_WIDTH) + 362.5))
                widget = FONT.render(str(box+1), True, pygame.Color('white'))
                font_rect = widget.get_rect()
                font_rect.center = (((self.boxes.box[box][0] - self.player.xpos) * SQUARE_WIDTH) + 400, ((self.boxes.box[box][1] - self.player.ypos) * SQUARE_WIDTH) + 400)
                self.window.blit(widget, font_rect)

        for b in range(len(self.boxes.boxes_to_take)):
            self.window.blit(CRATE, (715, 10 + (80*b)))
            widget = FONT.render(str(self.boxes.boxes_to_take[b]), True, pygame.Color('white'))
            font_rect = widget.get_rect()
            font_rect.center = (715 + 37.5, 10 + (80*b) + 37.5)
            self.window.blit(widget, font_rect)

        if self.player.direction is not None:
            if self.player.direction == 'TOP':
                pygame.draw.rect(self.window, (255, 0, 0), (362.5+15, 362.5, 15, 15))
                pygame.draw.rect(self.window, (255, 0, 0), (362.5+45, 362.5, 15, 15))
            elif self.player.direction == 'BOTTOM':
                pygame.draw.rect(self.window, (255, 0, 0), (362.5+15, 362.5+60, 15, 15))
                pygame.draw.rect(self.window, (255, 0, 0), (362.5+45, 362.5+60, 15, 15))
            elif self.player.direction == 'LEFT':
                pygame.draw.rect(self.window, (255, 0, 0), (362.5, 362.5+15, 15, 15))
                pygame.draw.rect(self.window, (255, 0, 0), (362.5, 362.5+45, 15, 15))
            elif self.player.direction == 'RIGHT':
                pygame.draw.rect(self.window, (255, 0, 0), (362.5+60, 362.5+15, 15, 15))
                pygame.draw.rect(self.window, (255, 0, 0), (362.5+60, 362.5+45, 15, 15))

        widget = FONT2.render('Money: ' + str(self.player.money), True, pygame.Color('white'))
        self.window.blit(widget, (10, 5))

        pygame.draw.rect(self.window, (100, 100, 100), (10, 55, 200, 55))

        if self.player.current_map < 9:
            widget = FONT3.render('Next map cost: ' + str(game_map_price[self.player.current_map]), True, pygame.Color('white'))
        else:
            widget = FONT3.render('Max map bought!', True, pygame.Color('white'))
        font_rect = widget.get_rect()
        font_rect.center = (110, 82.5)
        self.window.blit(widget, font_rect)

        pygame.draw.rect(self.window, (255, 0, 0), (362.5+7, 362.5+7, SQUARE_WIDTH-15, SQUARE_WIDTH-15))

class Boxes:
    def __init__(self):
        self.box = []
        self.boxes_to_take = []
        self.timer = time.time() + 3
        self.boxes_to_spawn = []

    def handle_boxes(self, playerx, playery, player):
        def check_for_delivery_overlap(xpos, ypos):
            for boxe in self.boxes_to_spawn:
                if xpos == boxe[0] and ypos == boxe[1]:
                    return False
            return True

        def choose_number_to_take():
            check = False
            number = 0
            while not check:
                tempvar = 0
                number = random.randint(1, len(self.box))
                for boxes in self.boxes_to_take:
                    if boxes != number:
                        tempvar += 1
                check = (tempvar == len(self.boxes_to_take))

            return number

        if not self.boxes_to_spawn and not self.boxes_to_take:
            x = 0
            mode = 'Normal'

            for i in range(len(game_map)):
                if (player.return_current_map(i) == '2') or ('3' in player.return_current_map(i)):
                    x += 1

            if (len(self.box) / x) * 100 > 65:
                mode = 'Takeaway'
            elif (len(self.box) / x) * 100 < 30:
                mode = 'Give'

            print(mode)

            if mode == 'Normal':
                print('ya')
                for i in range(random.randint(1, 5)):
                    checked = False
                    while not checked:
                        x, y = random.randint(15, 18), random.randint(2, 3)
                        checked = check_for_delivery_overlap(x, y)

                    self.boxes_to_spawn.append([x, y])

                temp = random.randint(0, 3)
                if (temp == 0) and len(self.box) >= 2:
                    for i in range(random.randint(1, 2)):
                        self.boxes_to_take.append(choose_number_to_take())

            elif mode == 'Give':
                for i in range(random.randint(2, 6)):
                    checked = False
                    while not checked:
                        x, y = random.randint(15, 18), random.randint(2, 3)
                        checked = check_for_delivery_overlap(x, y)

                    self.boxes_to_spawn.append([x, y])

            elif mode == 'Takeaway':
                for i in range(random.randint(3, 6)):
                    self.boxes_to_take.append(choose_number_to_take())

            for box in self.box:
                box[2] += 5

        for box in self.boxes_to_spawn:
            x, y = self.check_for_box(box[0], box[1], playerx, playery)
            if x != 0 and y != 0:
                self.boxes_to_spawn.remove(box)
                self.box.append([x, y, 5, True])

        for _ in self.boxes_to_take:
            if 14 < self.box[_-1][0] < 19 and 1 < self.box[_-1][1] < 4:
                self.box[_-1][3] = False
                self.boxes_to_take.remove(_)

                player.money += self.box[_-1][2]
                player.grabbing = None
                player.direction = None

    def check_for_box(self, xcor, ycor, playerx, playery):
        for box in self.box:
            if xcor == box[0] and ycor == box[1] and box[3]:
                return self.brute_force_check_for_box(playerx, playery)
        if playerx == xcor and playery == ycor:
            return self.brute_force_check_for_box(playerx, playery)
        return xcor, ycor

    def brute_force_check_for_box(self, playerx, playery):
        x, y = 15, 2
        for i in range(2, 4):
            for j in range(15, 19):
                temp = 0

                for box in self.box:
                    if (box[0] == x and box[1] == y and box[3]) or (playerx == x and playery == y):
                        continue
                    else:
                        temp += 1

                if temp == len(self.box):
                    return x, y
                x += 1
            x -= 4
            y += 1
        return 0, 0


class Player:
    def __init__(self, boxes):
        self.xpos = 16
        self.ypos = 5
        self.boxes = boxes
        self.grabbing = None
        self.direction = None
        self.current_map = 0
        self.money = 0

    def return_current_map(self, index):
        if len(game_map[index].split(';')) == 1:
            return game_map[index]
        else:
            thing_to_return = ''
            for i in range(len(game_map[index].split(';'))):
                if i == 0:
                    thing_to_return = game_map[index].split(';')[0]
                else:
                    if self.current_map >= int(game_map[index].split(';')[i].split(',')[1]):
                        thing_to_return = game_map[index].split(';')[i].split(',')[0]

            return thing_to_return

    def check_for_map_collision(self, side, step=0):
        if side == 'TOP':
            if (self.return_current_map((self.ypos-1-step)*MAP_X + self.xpos) != '0') and ('3' not in self.return_current_map((self.ypos-1-step)*MAP_X + self.xpos)) and (self.return_current_map((self.ypos-1-step)*31 + self.xpos) != '8'):
                return True
            else:
                return False

        elif side == 'BOTTOM':
            if self.return_current_map((self.ypos+1+step)*MAP_X + self.xpos) != '0' and '3' not in self.return_current_map((self.ypos+1+step)*MAP_X + self.xpos) and self.return_current_map((self.ypos+1+step)*31 + self.xpos) != '8':
                return True
            else:
                return False

        elif side == 'LEFT':
            if self.return_current_map(self.ypos*MAP_X + (self.xpos-1-step)) != '0' and '3' not in self.return_current_map(self.ypos*MAP_X + (self.xpos-1-step)) and self.return_current_map(self.ypos*31 + (self.xpos-1-step)) != '8':
                return True
            else:
                return False

        else:
            if self.return_current_map(self.ypos*MAP_X + (self.xpos+1+step)) != '0' and '3' not in self.return_current_map(self.ypos*MAP_X + (self.xpos+1+step)) and self.return_current_map(self.ypos*31 + (self.xpos+1+step)) != '8':
                return True
            else:
                return False

    def check_for_box_collision(self, side, step=0):
        if side == 'TOP':
            for _ in range(len(self.boxes.box)):
                if self.boxes.box[_][0] == self.xpos and self.boxes.box[_][1] == self.ypos-1-step and self.boxes.box[_][3]:
                    if self.grabbing == _ and self.check_for_box_collision(side, 1):
                        break
                    self.direction = side
                    self.grabbing = _
                    return False
            return True

        elif side == 'BOTTOM':
            for _ in range(len(self.boxes.box)):
                if self.boxes.box[_][0] == self.xpos and self.boxes.box[_][1] == self.ypos+1+step and self.boxes.box[_][3]:
                    if self.grabbing == _ and self.check_for_box_collision(side, 1):
                        break
                    self.direction = side
                    self.grabbing = _
                    return False
            return True

        elif side == 'LEFT':
            for _ in range(len(self.boxes.box)):
                if self.boxes.box[_][0] == self.xpos-1-step and self.boxes.box[_][1] == self.ypos and self.boxes.box[_][3]:
                    if self.grabbing == _ and self.check_for_box_collision(side, 1):
                        break
                    self.direction = side
                    self.grabbing = _
                    return False
            return True

        else:
            for _ in range(len(self.boxes.box)):
                if self.boxes.box[_][0] == self.xpos+1+step and self.boxes.box[_][1] == self.ypos and self.boxes.box[_][3]:
                    if self.grabbing == _ and self.check_for_box_collision(side, 1):
                        break
                    self.direction = side
                    self.grabbing = _
                    return False
            return True

    def handle_ungrabbing(self, view):
        if self.grabbing is not None:
            if (self.xpos != self.boxes.box[self.grabbing][0] and self.ypos != self.boxes.box[self.grabbing][1]) or not self.boxes.box[self.grabbing][3]:
                self.direction = None
                self.grabbing = None
                view.draw()

    def handle_grabbing(self, side):
        if self.grabbing is not None:
            if side == 'TOP' and (self.direction == 'BOTTOM' or self.direction == 'TOP'):
                self.boxes.box[self.grabbing][1] -= 1

            elif side == 'BOTTOM' and (self.direction == 'BOTTOM' or self.direction == 'TOP'):
                self.boxes.box[self.grabbing][1] += 1

            elif side == 'LEFT' and (self.direction == 'LEFT' or self.direction == 'RIGHT'):
                self.boxes.box[self.grabbing][0] -= 1

            elif side == 'RIGHT' and (self.direction == 'LEFT' or self.direction == 'RIGHT'):
                self.boxes.box[self.grabbing][0] += 1

class Controller:
    def __init__(self):
        self.WIN = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption('Storage Simulator')

        self.boxes = Boxes()
        self.player = Player(self.boxes)
        self.view = View(self.WIN, self.player, self.boxes)
        self.spawned = True

    def run(self):
        run = True
        clock = pygame.time.Clock()

        while run:
            clock.tick(60)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = pygame.mouse.get_pos()
                    if self.player.current_map < 9 and 10 <= x <= 210 and 55 <= y <= 110 and self.player.money >= game_map_price[self.player.current_map]:
                        self.player.current_map += 1
                        self.player.money -= game_map_price[self.player.current_map-1]

                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_w:
                        if (self.player.check_for_map_collision('TOP') and self.player.check_for_box_collision('TOP') and self.player.direction != 'TOP') or (self.player.check_for_map_collision('TOP', 1) and self.player.check_for_map_collision('TOP') and self.player.check_for_box_collision('TOP') and self.player.grabbing is not None):
                            self.player.ypos -= 1
                            self.player.handle_ungrabbing(self.view)
                            self.player.handle_grabbing('TOP')

                    elif event.key == pygame.K_a:
                        if (self.player.check_for_map_collision('LEFT') and self.player.check_for_box_collision('LEFT') and self.player.direction != 'LEFT') or (self.player.check_for_map_collision('LEFT', 1) and self.player.check_for_map_collision('LEFT') and self.player.check_for_box_collision('LEFT') and self.player.grabbing is not None):
                            self.player.xpos -= 1
                            self.player.handle_ungrabbing(self.view)
                            self.player.handle_grabbing('LEFT')

                    elif event.key == pygame.K_s:
                        if (self.player.check_for_map_collision('BOTTOM') and self.player.check_for_box_collision('BOTTOM') and self.player.direction != 'BOTTOM') or (self.player.check_for_map_collision('BOTTOM', 1) and self.player.check_for_map_collision('BOTTOM') and self.player.check_for_box_collision('BOTTOM') and self.player.grabbing is not None):
                            self.player.ypos += 1
                            self.player.handle_ungrabbing(self.view)
                            self.player.handle_grabbing('BOTTOM')

                    elif event.key == pygame.K_d:
                        if (self.player.check_for_map_collision('RIGHT') and self.player.check_for_box_collision('RIGHT') and self.player.direction != 'RIGHT') or (self.player.check_for_map_collision('RIGHT', 1) and self.player.check_for_map_collision('RIGHT') and self.player.check_for_box_collision('RIGHT') and self.player.grabbing is not None):
                            self.player.xpos += 1
                            self.player.handle_ungrabbing(self.view)
                            self.player.handle_grabbing('RIGHT')

                    elif event.key == pygame.K_SPACE:
                        self.player.direction = None
                        self.player.grabbing = None

            if self.boxes.timer < time.time():
                self.boxes.handle_boxes(self.player.xpos, self.player.ypos, self.player)
                if not self.boxes.boxes_to_spawn and not self.boxes.boxes_to_take:
                    self.boxes.timer = time.time() + 10

            self.view.draw()
            pygame.display.update()

        pygame.quit()

if __name__ == '__main__':
    c = Controller()
    c.run()
