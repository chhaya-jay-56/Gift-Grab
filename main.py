import pygame
import random
import pygame_gui
import cx_Oracle
import string

# Checking Connectvity to Oracle SQL
conn = cx_Oracle.connect('SYSTEM/CE25@//localhost:1521/xe')

print(conn.version)

# Initialize pygame
pygame.init()

# Define button properties
button_text = "PLAY"
button_width, button_height = 200, 50
button_color = (127 , 255 , 212) 
hover_color = (255, 255, 255)
button_position = (77, 240)
font = pygame.font.Font(None, 36)

# Create a Rect for the button
button_rect = pygame.Rect(button_position[0], button_position[1], button_width, button_height)

# Shadow properties
shadow_offset = 5  # Adjust the offset for the shadow
shadow_color = (100, 100, 100, 100)  # RGBA color for the shadow

# SECOND STORE BUTTON ------------------------------------------------------------------------------------------------------------------------------

# Define button properties
button_text2 = "STORE"
button_width2, button_height2 = 200, 50
button_color2 = (127 , 255 , 212) 
hover_color2 = (255, 255, 255)
button_position2 = (77, 310)
font2 = pygame.font.Font(None, 36)

# Create a Rect for the button
button_rect2 = pygame.Rect(button_position2[0], button_position2[1], button_width2, button_height2)

# Shadow properties
shadow_offset2 = 5  # Adjust the offset for the shadow
shadow_color2 = (100, 100, 100, 100)  # RGBA color for the shadow

# THIRD BUTTON ---------------------------------------------------------------------------------------------------------------------------------------

button_text3 = "EQUIP"
button_width3, button_height3 = 200, 50
button_color3 = (124 , 252 , 0) 
hover_color3 = (255, 255, 255)
button_position3 = (77, 540)
font3 = pygame.font.Font(None, 36)

# Create a Rect for the button
button_rect3 = pygame.Rect(button_position3[0], button_position3[1], button_width3, button_height3)

# FOURTH BUTTON -------------------------------------------------------------------------------------------------------------------------------------

button_text4 = "PLAY"
button_width4, button_height4 = 200, 50
button_color4 = (124 , 252 , 0) 
hover_color4 = (255, 255, 255)
button_position4 = (77, 613)
font4 = pygame.font.Font(None, 36)

# Create a Rect for the button
button_rect4 = pygame.Rect(button_position4[0], button_position4[1], button_width4, button_height4)

# FIFTH BUTTON -------------------------------------------------------------------------------------------------------------------------------------

button_text5 = "ACCOUNT"
button_width5, button_height5 = 200, 50
button_color5 = (127 , 255 , 212) 
hover_color5 = (255, 255, 255)
button_position5 = (77, 380)
font5 = pygame.font.Font(None, 36)

# Create a Rect for the button
button_rect5 = pygame.Rect(button_position5[0], button_position5[1], button_width5, button_height5)

# Shadow properties
shadow_offset5 = 5  # Adjust the offset for the shadow
shadow_color5 = (100, 100, 100, 100)  # RGBA color for the shadow

# SIXTH BUTTON -------------------------------------------------------------------------------------------------------------------------------------

button_text6 = "PLAY NOW"
button_width6, button_height6 = 200, 50
button_color6 = (124 , 252 , 0) 
hover_color6 = (255, 255, 255)
button_position6 = (77, 600)
font6 = pygame.font.Font(None, 36)

# Create a Rect for the button
button_rect6 = pygame.Rect(button_position6[0], button_position6[1], button_width6, button_height6)

# The screen W*H
screen = pygame.display.set_mode((360, 700))

# Background image
background = pygame.image.load('bg.png')

# Changing window name and icon
pygame.display.set_caption("GIFT-GRAB")
icon = pygame.image.load('charity.png')
pygame.display.set_icon(icon)

# Main hand and coordinates
main_hand = pygame.image.load('santa_hand.png')
hand_x = 120
hand_y = 300
hand_change_x = 0
hand_change_y = 0
bg_x = 0
bg_y = 0
points = 0
can_point_left = True
can_point_right = True

# Iron hand
start_time = pygame.time.get_ticks()
duration = 3000

def hand_1(x, y):
    screen.blit(main_hand, (hand_x, hand_y))

# Left hand and coordinates
left_hand = pygame.image.load('left_hand.png')
left_hand_x = -110
left_hand_y = random.randint(-200, -110)
left_change = 0

def left(x, y):
    screen.blit(left_hand, (left_hand_x, left_hand_y))

# Right hand and coordinates
right_hand = pygame.image.load('right_hand.png')
right_hand_x = 110
right_hand_y = random.randint(-500, -300)
right_change = 0

def right(x, y):
    screen.blit(right_hand, (right_hand_x, right_hand_y))

# Gift
gift = pygame.image.load('gift.png')
gift_x = 200
gift_y = 340
gift_change_x = 0
gift_change_y = 0

gift_2 = pygame.image.load('gift_fake.png')
gift_2_x = 200
gift_2_y = 340
gift_change_x_2 = 0
gift_change_y_2 = 0

def chris_gift(x, y):
    screen.blit(gift, (gift_x, gift_y))

# Starting screen
press = pygame.image.load('press_any_key.png')
press_x = 0
press_y = 503

grab = pygame.image.load('gift-grab.png')
grab_x = 30
grab_y = 250

hold = pygame.image.load('holding_gift.png')
hold_x = 0
hold_y = 20

score = pygame.image.load('scoreboard.png')
score_x = 120
score_y = 30

# arrow exit
left_arrow = pygame.image.load('left-arrow.png')
left_x = 20
left_y = 620

cutter_line = pygame.image.load('cutter.png')
cutter_x = 50
cutter_y = 620

cutter_line_2 = pygame.image.load('cutter_line_2.png')
cutter_2_x = 0
cutter_2_y = 420

cutter_line_3 = pygame.image.load('cutter_line_3.png')
cutter_3_x = -50
cutter_3_y = 220

# arrow play
right_arrow = pygame.transform.rotate(left_arrow , -180)
right_x = 280
right_y = 15

rotating_saw = pygame.image.load('rotating_saw_01.png')
rotate_x = 75
rotate_y = 640

rotating_saw_2 = pygame.image.load('rotating_saw_02.png')
rotate_x_2 = -30
rotate_y_2 = 440

shop_1_hand = pygame.image.load('shop_1_hand.png')
shop_1_x = 120
shop_1_y = 200

shop_2_hand = pygame.image.load('shop_2_hand.png')
shop_2_x = -200
shop_2_y = 200

right_side = pygame.image.load('right.png')
right_side_x = 260
right_side_y = 300

left_side = pygame.image.load('left.png')
left_side_x = 40
left_side_y = 300

glow_hand = pygame.image.load('glow_hand.png')
glow_x = -200
glow_y = 200

home = pygame.image.load('home-button.png')
home_x = 150
home_y = 25

left_hand_count = True
right_hand_count = True

count = 0

# angle of saw
rotation_angle = 0

# first window
first = False

# intial window
intial = True

# store window
store = False

# main window
running = False

# Start window
starting = False

# Exit window
exiting = False

# main loop
outer = True

global_search_item = None
global_score_h = None

rotation_angle_2 = 0

def rotate_image(image, angle):
    rotated_image = pygame.transform.rotate(image, angle)
    return rotated_image

def rotate_image_2(image, angle):
    rotated_image_2 = pygame.transform.rotate(image, angle)
    return rotated_image_2

def generate_unique_code():
    characters = string.ascii_letters + string.digits  # Include letters and digits
    unique_code = ''.join(random.choice(characters) for _ in range(6))
    return unique_code

# Create Rect objects for left hand and gift
left_hand_rect = left_hand.get_rect()
# gift_rect = gift.get_rect()
gift_2_rect = gift_2.get_rect()
right_hand_rect = right_hand.get_rect()
main_hand_rect = main_hand.get_rect()
rotating_saw_rect = rotating_saw.get_rect()
rotating_saw_rect_2 = rotating_saw_2.get_rect()

font = pygame.font.Font(None, 36)  # Choose a font and size
font_2 = pygame.font.Font(None, 43) 
font_3 = pygame.font.Font(None, 37)

# INPUT NI MATHA ---- KUT 

clock = pygame.time.Clock()

input1 = pygame_gui.UIManager((300, 700))
text_input1 = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((120, 120), (250, 35)), manager=input1, object_id='#main_text_entry1')

input2 = pygame_gui.UIManager((300, 700))
text_input2 = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((120, 170), (190, 35)), manager=input2, object_id='#main_text_entry2')

input3 = pygame_gui.UIManager((300, 700))
text_input3 = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((120, 510), (190, 35)), manager=input3, object_id='#main_text_entry3')

current_shop = 1

while outer:

    while first:

        screen.fill((0, 255, 0))
        screen.blit(background, (bg_x, bg_y))
        screen.blit(hold, (hold_x, hold_y + 230))

        UI_REFRESH_RATE = clock.tick(60)/1000

        text_7 = font_3.render(str("ACCOUNT CREATION"), True, (0,0,0))  # Render the text
        text_7_rect = text_7.get_rect()
        text_7_rect.center = (180, 58)

        text_8 = font.render(str("SELECT ACCOUNT"), True, (0,0,0))  # Render the text
        text_8_rect = text_8.get_rect()
        text_8_rect.center = (180, 450)

        text_9 = font.render(str("NAME"), True, (0,0,0))  # Render the text
        text_9_rect = text_9.get_rect()
        text_9_rect.center = (60, 140)

        text_10 = font.render(str("AGE"), True, (0,0,0))  # Render the text
        text_10_rect = text_10.get_rect()
        text_10_rect.center = (60, 190)

        text_11 = font.render(str("NAME"), True, (0,0,0))  # Render the text
        text_11_rect = text_11.get_rect()
        text_11_rect.center = (60, 530)

        # Draw the button
        color = hover_color6 if button_rect6.collidepoint(pygame.mouse.get_pos()) else button_color6
        pygame.draw.rect(screen, color, button_rect6, border_radius=20)
        pygame.draw.rect(screen, (0, 0, 0), button_rect6, 4 , border_radius=20)  # Border width
        text = font6.render(button_text6, True, (0, 0, 0))
        text_rect = text.get_rect(center=button_rect6.center)
        screen.blit(text, text_rect)

        screen.blit(text_7, text_7_rect)
        screen.blit(text_8, text_8_rect)
        screen.blit(text_9, text_9_rect)
        screen.blit(text_10, text_10_rect)
        screen.blit(text_11, text_11_rect)
        
        for event in pygame.event.get():

            if event.type == pygame.QUIT:

                outer = False
                first = False

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_RIGHT:
                
                    starting = True
                    first = False

                if event.key == pygame.K_h:

                    intial = True
                    first = False

            if button_rect6.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:

                starting = True
                first = False


            if (event.type == pygame_gui.UI_TEXT_ENTRY_FINISHED and event.ui_object_id == '#main_text_entry2'):
                
                code = generate_unique_code()
                try:           
                    cur = conn.cursor()

                        # Generate a new table name
                    table_name = f'PLAYER{code}'
                    # Create the table
                    sql_create = f"""CREATE TABLE {table_name} (
                                            PLAYER_CODE VARCHAR2(50),
                                            PLAYER_AGE INT,
                                            PLAYER_NAME VARCHAR(50),
                                            PLAYER_SCORE INT
                                        )"""
                    cur.execute(sql_create)
                    # This line has an issue, use text_input1.get_text() and text_input2.get_text() to get the entered values
                    name = text_input1.get_text()
                    age = text_input2.get_text()
                        
                    p_score = 0
                    # Insert a row into the table
                    sql_insert_acc = f"INSERT INTO player_accounts (PLAYER_CODE, PLAYER_TABLE_NAME , PLAYER_NAME, PLAYER_AGE) VALUES ('{code}', '{table_name}', '{name}', '{age}')"
                    cur.execute(sql_insert_acc)

                    # Insert a row into the table
                    sql_insert = f"INSERT INTO {table_name} (PLAYER_CODE, PLAYER_NAME, PLAYER_AGE , PLAYER_SCORE) VALUES ('{code}', '{name}', '{age}' , '{p_score}')"
                    cur.execute(sql_insert)

                    # Commit the changes
                    conn.commit()
                except Exception as err:  
                
                    print("ERROR OCCURRED:", err)
                        # Rollback the transaction in case of an error
                    conn.rollback()
                else:
                    
                    print(f"YOUR ACCOUNT WAS CREATED")
                finally:
                        # Close the cursor and connection in a finally block to ensure proper cleanup
                    cur.close()
                    conn.close()


            if (event.type == pygame_gui.UI_TEXT_ENTRY_FINISHED and event.ui_object_id == '#main_text_entry3'):

                try:

                    with conn.cursor() as cur:

                        global_search_item = text_input3.get_text()

                        cur.execute(f"SELECT PLAYER_TABLE_NAME FROM player_accounts WHERE PLAYER_NAME = '{global_search_item}'")
                        player_t_1 = cur.fetchone()[0]  # Fetch the result

                        cur.execute(f"SELECT PLAYER_CODE FROM player_accounts WHERE PLAYER_NAME = '{global_search_item}'")
                        player_c_1 = cur.fetchone()[0]

                        cur.execute(f"SELECT PLAYER_AGE FROM player_accounts WHERE PLAYER_NAME = '{global_search_item}'")
                        player_a_1 = cur.fetchone()[0]

                    # Insert a row into the table
                        sql_insert_acc = f"INSERT INTO {player_t_1} (PLAYER_CODE, PLAYER_NAME, PLAYER_AGE) VALUES ('{player_c_1}', '{global_search_item}', '{player_a_1}')"
                        cur.execute(sql_insert_acc)

                        # Commit the changes
                        conn.commit()

                except Exception as err:
                        
                    print("ERROR OCCURRED:", err)
                        # Rollback the transaction in case of an error
                    conn.rollback()

                else:
                    print(f"{global_search_item}'s Account Selected")


            input1.process_events(event)
            input2.process_events(event)
            input3.process_events(event)
            
        input1.update(UI_REFRESH_RATE)
        input2.update(UI_REFRESH_RATE)
        input3.update(UI_REFRESH_RATE)

        input1.draw_ui(screen)
        input2.draw_ui(screen)
        input3.draw_ui(screen)

        pygame.display.update()

    while intial:

        screen.fill((0, 255, 0))
        screen.blit(background, (bg_x, bg_y)) 
        screen.blit(home, (home_x, home_y))

        pos = pygame.mouse.get_pos()
    
        clicked = False

        for event in pygame.event.get():

            if event.type == pygame.QUIT:

                outer = False
                intial = False

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_RIGHT:
                
                    starting = True
                    intial = False

        # Draw the shadow
        shadow_rect = button_rect.move(shadow_offset, shadow_offset)
        pygame.draw.rect(screen, shadow_color, shadow_rect, border_radius=20)

        # Draw the button
        color = hover_color if button_rect.collidepoint(pygame.mouse.get_pos()) else button_color
        pygame.draw.rect(screen, color, button_rect, border_radius=20)
        pygame.draw.rect(screen, (0, 0, 0), button_rect, 4 , border_radius=20)  # Border width
        text = font.render(button_text, True, (0, 0, 0))
        text_rect = text.get_rect(center=button_rect.center)
        screen.blit(text, text_rect)

        # Check for button click
        if button_rect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:

            starting = True
            intial = False

        # SECOND BUTTON------------------------------------------------------------------------------------------------------------------------------

        # Draw the shadow
        shadow_rect2 = button_rect2.move(shadow_offset2, shadow_offset2)
        pygame.draw.rect(screen, shadow_color2, shadow_rect2, border_radius=20)

        # Draw the button
        color = hover_color2 if button_rect2.collidepoint(pygame.mouse.get_pos()) else button_color2
        pygame.draw.rect(screen, color, button_rect2, border_radius=20)
        pygame.draw.rect(screen, (0, 0, 0), button_rect2, 4 , border_radius=20)  # Border width
        text = font2.render(button_text2, True, (0, 0, 0))
        text_rect = text.get_rect(center=button_rect2.center)
        screen.blit(text, text_rect)

        # SIXTH BUTTON------------------------------------------------------------------------------------------------------------------------------

        # Draw the shadow
        shadow_rect5 = button_rect5.move(shadow_offset5, shadow_offset5)
        pygame.draw.rect(screen, shadow_color5, shadow_rect5, border_radius=20)

        # Draw the button
        color = hover_color5 if button_rect5.collidepoint(pygame.mouse.get_pos()) else button_color5
        pygame.draw.rect(screen, color, button_rect5, border_radius=20)
        pygame.draw.rect(screen, (0, 0, 0), button_rect5, 4 , border_radius=20)  # Border width
        text = font5.render(button_text5, True, (0, 0, 0))
        text_rect = text.get_rect(center=button_rect5.center)
        screen.blit(text, text_rect)

        # Check for button click
        if button_rect2.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:

            store = True
            intial = False

        # Check for button click
        if button_rect5.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:

            first = True
            intial = False

        pygame.display.update()

    while store:

        count_remain = 0

        screen.fill((0, 255, 0))
        screen.blit(background, (bg_x, bg_y))
        screen.blit(shop_1_hand , (shop_1_x , shop_1_y))
        screen.blit(shop_2_hand , (shop_2_x , shop_2_y))
        screen.blit(right_side , (right_side_x , right_side_y))
        screen.blit(left_side , (left_side_x , left_side_y))

        if current_shop == 1:

            text_4 = font_3.render("SANTA HAND", True, (0, 0, 0))
            text_4_rect = text_4.get_rect()
            text_4_rect.center = (180, 465)

            text_5 = font_3.render("", True, (0, 0, 0))  # Empty text for shop_2
            text_5_rect = text_5.get_rect()
            text_5_rect.center = (660, 465)

        elif current_shop == 2:
        
            text_4 = font_3.render("", True, (0, 0, 0))  # Empty text for shop_1
            text_4_rect = text_4.get_rect()
            text_4_rect.center = (140, 465)

            text_5 = font_3.render("GLOVES HAND", True, (0, 0, 0))
            text_5_rect = text_5.get_rect()
            text_5_rect.center = (185, 465)

        screen.blit(text_4, text_4_rect)
        screen.blit(text_5, text_5_rect)

        for event in pygame.event.get():

            if event.type == pygame.QUIT:

                outer = False
                store = False

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_RIGHT:

                    current_shop = 2
                    shop_1_x = -200
                    shop_2_x = 110

                if event.key == pygame.K_h:

                    intial = True
                    store = False 

                if event.key == pygame.K_LEFT:
                    current_shop = 1
                    shop_1_x = 120
                    shop_2_x = -200

                if event.key == pygame.K_SPACE:

                    starting = True
                    store = False

        # Draw the button
        color = hover_color3 if button_rect3.collidepoint(pygame.mouse.get_pos()) else button_color3
        pygame.draw.rect(screen, color, button_rect3, border_radius=20)
        pygame.draw.rect(screen, (0, 0, 0), button_rect3, 4 , border_radius=20)  # Border width
        text = font3.render(button_text3, True, (0, 0, 0))
        text_rect = text.get_rect(center=button_rect3.center)
        screen.blit(text, text_rect)

        # Check for button click
        if button_rect3.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:

            if current_shop == 2:

                hand_x = -200
                glow_x = 100

            elif current_shop == 1:

                glow_x = -200
                hand_x = 100

        # Draw the button
        color = hover_color4 if button_rect4.collidepoint(pygame.mouse.get_pos()) else button_color4
        pygame.draw.rect(screen, color, button_rect4, border_radius=20)
        pygame.draw.rect(screen, (0, 0, 0), button_rect4, 4 , border_radius=20)  # Border width
        text = font4.render(button_text, True, (0, 0, 0))
        text_rect = text.get_rect(center=button_rect4.center)
        screen.blit(text, text_rect)

        # Check for button click
        if button_rect4.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:

            starting = True
            store = False

        pygame.display.update()

    while starting:

        count = 0

        screen.fill((0, 255, 0))
        screen.blit(background, (bg_x, bg_y))
        screen.blit(press, (press_x, press_y))
        screen.blit(grab, (grab_x, grab_y))
        screen.blit(hold, (hold_x, hold_y))

        for event in pygame.event.get():

            if event.type == pygame.QUIT:

                outer = False
                starting = False

            if event.type == pygame.KEYDOWN:

                left_hand_x = -110
                left_hand_y = random.randint(-200, -110)

                right_hand_x = 110
                right_hand_y = random.randint(-500, -300)

                rotate_x = 75
                rotate_y = 640

                rotate_x_2 = -30
                rotate_y_2 = 440

                running = True
                starting = False

        pygame.display.update()

    while running:

        # BG color
        screen.fill((0, 255, 0))
        
        # BG iterate
        screen.blit(background, (bg_x, bg_y))
        bg_change = -0.5

        screen.blit(cutter_line , (cutter_x , cutter_y))

        screen.blit(cutter_line_2 , (cutter_2_x , cutter_2_y))

        screen.blit(cutter_line_3 , (cutter_3_x , cutter_3_y))

        # Main hand function call
        screen.blit(main_hand, (hand_x, hand_y))

        screen.blit(glow_hand , (glow_x , glow_y))

        # Rotate the half cutter image
        rotated_cutter_image = rotate_image(rotating_saw, rotation_angle)

        rotated_cutter_image_rect = rotated_cutter_image.get_rect()

        rotated_cutter_image_rect.center = (rotate_x , rotate_y)

        # Draw the rotated image at the specified (rotate_x, rotate_y) position
        screen.blit(rotated_cutter_image, rotated_cutter_image_rect)

        # Increase the rotation angle
        rotation_angle += -0.6   # Adjust the rotation speed as needed

        # 2 cutter 
        rotated_cutter_image_2 = rotate_image_2(rotating_saw_2, rotation_angle_2)

        rotated_cutter_image_rect_2 = rotated_cutter_image_2.get_rect()

        rotated_cutter_image_rect_2.center = (rotate_x_2 , rotate_y_2)

        screen.blit(rotated_cutter_image_2, rotated_cutter_image_rect_2)

        # Increase the rotation angle 2
        rotation_angle_2 += -0.9

        left(left_hand_x, left_hand_y)
        right(right_hand_x, right_hand_y)

        screen.blit(score, (score_x, score_y))

        text = font.render(str(count), True, (0, 0, 0))  # Render the text
        text_rect = text.get_rect()
        text_rect.center = (187, 61)  # Center the text on the screen

        screen.blit(text, text_rect)

        dice = random.randint(0, 1)

        # speed control for hands
        if dice == 0:

            left_change = 0.45

        else:

            right_change = 0.35

        screen.blit(gift_2 , (gift_2_x , gift_2_y))

        chris_gift(gift_x, gift_y)

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                
                running = False
                outer = False

            # mouse co-ordinates assign to gift
            mouse_x, mouse_y = pygame.mouse.get_pos()

            gift_x = mouse_x - 38
            gift_y = mouse_y - 38

            gift_2_x = mouse_x - 20
            gift_2_y = mouse_y - 20

            if current_shop == 2:
            
                glow_x = gift_x - 25
                glow_y = gift_y - 32

            else:

                hand_x = gift_x - 20
                hand_y = gift_y - 23

                

        bg_y += bg_change

        if left_hand_y > 700:

            randomygen = random.randint(-160, -110)
            left_hand_y = randomygen
            left_hand_count = True

        if right_hand_y > 700:

            randomygen = random.randint(-600, -550)
            right_hand_y = randomygen
            right_hand_count = True

        if bg_y == -580:

            bg_y = 0

        left_hand_y += left_change
        right_hand_y += right_change

        if current_shop == 2:

            if glow_x <= -55:
                glow_x = -55

            elif glow_x >= 270:
                glow_x = 270

            if glow_y >= 620:
                glow_y = 620

            elif glow_y <= 202:
                glow_y = 202

        # Main hand

        elif current_shop == 1:

            if hand_x <= -55:
                hand_x = -55

            elif hand_x >= 270:
                hand_x = 270

            if hand_y >= 620:
                hand_y = 620

            elif hand_y <= 202:
                hand_y = 202

        # Gift

        if gift_x <= -37:
            gift_x = -37

        elif gift_x >= 290:
            gift_x = 290

        if gift_y >= 643:
            gift_y = 643

        elif gift_y <= 220:
            gift_y = 220

        # fake gift

        if gift_2_x <= -37:
            gift_2_x = -37

        elif gift_2_x >= 310:
            gift_2_x = 310

        if gift_2_y >= 660:
            gift_2_y = 660

        elif gift_2_y <= 250:
            gift_2_y = 250

        left_hand_rect.topleft = (left_hand_x - 10, left_hand_y)
        # gift_rect.topleft = (gift_x + 30, gift_y + 22)

        right_hand_rect.topleft = (right_hand_x + 70, right_hand_y + 30)

        gift_2_rect.topleft = (gift_2_x + 15, gift_2_y - 5)

        rotated_cutter_image_rect.topleft = (rotate_x - 40, rotate_y - 60)
        rotated_cutter_image_rect_2.topleft = (rotate_x_2 - 40, rotate_y_2 - 60)

        main_hand_rect.topleft = (hand_x, hand_y)

        if left_hand_y > hand_y and left_hand_count:
            count += 1
            left_hand_count = False

        if right_hand_y > hand_y and right_hand_count:
            count += 1
            right_hand_count = False
            screen.blit(text, text_rect)

        first = True

        rotate_x += 0.1
        rotate_x_2 += 0.075

        if rotate_x > 390 and first:

            rotate_x = -30
            rotate_y = 240
            first = False

        elif rotate_x > 320 and rotate_y == 240:

            rotate_x = 75
            rotate_y = 640

        if rotate_x_2 > 400:

            rotate_x_2 = -40

        global_score_h = count

        if left_hand_rect.colliderect(gift_2_rect) or right_hand_rect.colliderect(gift_2_rect):

            try:

                with conn.cursor() as cur:

                    cur.execute(f"SELECT PLAYER_TABLE_NAME FROM player_accounts WHERE PLAYER_NAME = '{global_search_item}'")
                    player_t_1 = cur.fetchone()[0]  # Fetch the result

                    cur.execute(f"SELECT PLAYER_CODE FROM player_accounts WHERE PLAYER_NAME = '{global_search_item}'")
                    player_c_1 = cur.fetchone()[0]

                    cur.execute(f"SELECT PLAYER_AGE FROM player_accounts WHERE PLAYER_NAME = '{global_search_item}'")
                    player_a_1 = cur.fetchone()[0]
                        
                        # Insert a row into the table
                    sql_insert = f"INSERT INTO {player_t_1} (PLAYER_CODE, PLAYER_NAME, PLAYER_AGE , PLAYER_SCORE) VALUES ('{player_c_1}', '{global_search_item}', '{player_a_1}' , '{global_score_h}')"
                    cur.execute(sql_insert)

                
                        # Commit the changes
                    conn.commit()

            except Exception as err:
                        
                print("ERROR OCCURRED:", err)
                        # Rollback the transaction in case of an error
                conn.rollback()

            else:

                pass

            running = False
            exiting = True
            
        if gift_2_rect.colliderect(rotated_cutter_image_rect_2) or gift_2_rect.colliderect(rotated_cutter_image_rect):

            try:

                with conn.cursor() as cur:

                    cur.execute(f"SELECT PLAYER_TABLE_NAME FROM player_accounts WHERE PLAYER_NAME = '{global_search_item}'")
                    player_t_1 = cur.fetchone()[0]  # Fetch the result

                    cur.execute(f"SELECT PLAYER_CODE FROM player_accounts WHERE PLAYER_NAME = '{global_search_item}'")
                    player_c_1 = cur.fetchone()[0]

                    cur.execute(f"SELECT PLAYER_AGE FROM player_accounts WHERE PLAYER_NAME = '{global_search_item}'")
                    player_a_1 = cur.fetchone()[0]
                        
                        # Insert a row into the table
                    sql_insert = f"INSERT INTO {player_t_1} (PLAYER_CODE, PLAYER_NAME, PLAYER_AGE , PLAYER_SCORE) VALUES ('{player_c_1}', '{global_search_item}', '{player_a_1}' , '{global_score_h}')"
                    cur.execute(sql_insert)

                        # Commit the changes
                    conn.commit()

            except Exception as err:
                        
                print("ERROR OCCURRED:", err)
                        # Rollback the transaction in case of an error
                conn.rollback()

            else:
                
                pass

            running = False
            exiting = True

        pygame.display.update()

    # exit loop
    while exiting:

        screen.fill((0, 255, 0))
        screen.blit(background, (bg_x, bg_y))

        screen.blit(score, (score_x, score_y + 245))

        text = font.render(str(count), True, (0, 0, 0))  # Render the text
        text_rect = text.get_rect()
        text_rect.center = (187, 305)  # Center the text on the screen

        screen.blit(left_arrow , (left_x , left_y))

        screen.blit(right_arrow , (right_x , right_y))

        screen.blit(text, text_rect)

        # score text
        text_2 = font_2.render(str("YOUR SCORE"), True, (0,0,0))  # Render the text
        text_2_rect = text.get_rect()
        text_2_rect.center = (95, 380) 

        screen.blit(text_2, text_2_rect)

        text_3 = font_3.render(str("EXIT"), True, (0,0,0))  # Render the text
        text_3_rect = text.get_rect()
        text_3_rect.center = (106, 652) 

        screen.blit(text_3, text_3_rect)

        text_4 = font_3.render(str("PLAY"), True, (0,0,0))  # Render the text
        text_4_rect = text.get_rect()
        text_4_rect.center = (210, 50) 

        screen.blit(text_4, text_4_rect)

        for event in pygame.event.get():

            if event.type == pygame.QUIT:

                outer = False
                exiting = False

            if event.type == pygame.KEYDOWN:
                
                starting = True
                exiting = False

                if event.key == pygame.K_LEFT:
                
                    outer = False

                if event.key == pygame.K_RIGHT:

                    starting = True
                    exiting = False

                if event.key == pygame.K_h:

                    intial = True
                    exiting = False

            pygame.display.update()
