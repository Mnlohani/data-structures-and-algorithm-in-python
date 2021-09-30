def draw_line(tick_length, tick_label=''):
    '''Draw one linw with given tick length'''
    line = '-' * tick_length
    if tick_label:
        line += ' ' + tick_label
    print(line)

def draw_level(center_length):
    '''draw level in ruler with center tick'''
    if center_length > 0:
        draw_level(center_length - 1)
        draw_line(center_length)
        draw_level(center_length - 1)

def draw_ruler(num_length):
    ''' draw a ruler with length of num_length'''
    draw_line(tick_length=num_length, tick_label= '0')
    for i in range(1, num_length + 1):
        draw_level(num_length - 1)
        draw_line(num_length, str(i))

if __name__ == '__main__':
    draw_ruler(3)