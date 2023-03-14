import urllib.request


def main():
    URL = 'https://upload.wikimedia.org/wikipedia/commons/thumb/4/49/Seeman_Newton_1726.jpg/250px-Seeman_Newton_1726.jpg'
    FILENAME = 'image1.jpg'
    with urllib.request.urlopen(URL) as response:
        image = response.read()
        with open(FILENAME, 'wb') as output_file:
            output_file.write(image)


if __name__ == '__main__':
    main()
