import os

def main():
    count = 0
    path = input('\nEnter the full path to the directory: ')
    for filename in os.listdir(path):
        my_destination  = f'img{str(count)}.jpg'
        my_source = path + filename
        my_destination = path + my_destination
        os.rename(my_source, my_destination)
        count += 1
    
    print('\nBulk file renaming was successful!')

if __name__ == '__main__':
    main()
