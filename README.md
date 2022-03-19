# spotify-nfc-radio
Retro-futuristic radio project based on NFC chips and spotify

## Hardware Components:
 - [Raspberry](https://thepihut.com/products/raspberry-pi-3-model-b?src=raspberrypi)
 - [NFC tag](https://www.amazon.co.uk/Programmable-TimesKey-Circular-Compatible-Devices-40PCS/dp/B07MNQMVCL)
 - [NFC reader](https://www.amazon.co.uk/ARCELI-Module-13-56MHz-Arduino-Raspberry/dp/B07J2R8RZW/ref=sr_1_6?crid=39ZJ39L17GJ5T&keywords=NFC+UART+kit+raspberry&qid=1647724410&s=electronics&sprefix=nfc+uart+kit+raspberry%2Celectronics%2C89&sr=1-6)

## Software Libraries:
 - [Spotipy](https://spotipy.readthedocs.io/en/2.19.0/)

## Functionalities:
 - [ ] write mode: write data to a tag containing a url to a spotifiy song/album/playlist.
 - [ ] Read data from tag and plays the acccording song/album/playlist.
 - [ ] Volume setting? 

## Setup:
 1. You need to download and install [Spotipy](https://spotipy.readthedocs.io/en/2.19.0/). Follow their guidlines. 
 2. From the [Spotipy](https://spotipy.readthedocs.io/en/2.19.0/) create a dev space then an spotify app. Connect with your account details. Get the `client ID` number and `Client Secret` and export them either to a file or immitidatly as environment variable:
    ```
        export SPOTIPY_CLIENT_ID=$(client ID)
        export SPOTIPY_CLIENT_SECRET=$(client secret)
    ```
 3. Lastly you need to add a redirect uri in the spotify app. For that go on the app dashboard, edit settings then enter 
    ```
        http://localhost
    ```
    Save and exit.
 4. export the redirect uri `export SPOTIPY_REDIRECT_URI="http://localhost"`
 4. Run the test code: `python test_setup.py`. The first time running a web page will open, ask for some permissions and crash. Take the generated url and type it in the terminal prompt.
 
### Troubleshooting:
  If you generate a "NO_ACTIVE_DEVICE" error, it's because the code api hasn't seen the spotify client app in action. Turn on the app and play a random song. Restart the program and it should work.

# TODO:

## Hardware setup:
 - [ ] buy chip.
 - [ ] buy reader.
 - [ ] Setup the raspberry.
 - [ ] Install spotify client.
 - [ ] setup wire.

## Code setup
 - [X] interact with spotify api.
 - [ ] interact with a NFC chip in python.
 - [ ] desing code architecture. 
 - [ ] setup callback for NFC chip.
 - [ ] play around with the API.

## Other useless ideas:
 - [ ] a music visualizer with a small led screen showing some retro stilyish music paterns.