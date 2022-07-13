with open('dataset_24465_4 (2).txt') as i, open('result.txt', 'w') as o:
    lines = [line.rstrip() for line in i]
    o.write('\n'.join(lines[::-1]))
