import pytube
import os
import sys
try:
    url = input("Enter the Url of Youtube Video\n:")


    print(f'Options For Quality =>')
    yt = pytube.YouTube(url)
    stream = yt.streams.filter(only_audio=True)
    j = 0

    for i in range(len(stream)):
        j += 1
        tmp = stream[i].abr
        print(f'{j}){tmp}')
    choice = int(input('Input your Choice\n:'))

    if choice > len(stream):
        print('Invalid Choice')
        sys.exit()
    a = stream[choice-1].itag
    
    stream = stream.get_by_itag(a)
    print('Downloading...')

    stream.download()
    os.rename(stream.default_filename, f"{stream.default_filename.split('.')[0]}.mp3")
    print('Downloaded')
except KeyboardInterrupt:
    print('Download Cancelled')
    sys.exit()
except:
    print('Download Failed')

    



