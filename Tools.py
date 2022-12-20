def progress_bar(current, total, bar_length=20):
    fraction = current / total

    arrow = int(fraction * bar_length - 1) * '-' + '>'
    padding = int(bar_length - len(arrow)) * ' '

    if current == total:
        ending = '\n'
    else:
        ending = '\r'

    return f'Progress: [{arrow}{padding}] {int(fraction*100)}%'#, end=ending)


