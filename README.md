# Doppelwürfel
Transposition cipher with two different keywords, also known as [Doppelwürfel or UBCHI](https://en.wikipedia.org/wiki/Transposition_cipher#Double_transposition). With this little program you can decode and encode Strings.

An article on this cipher appeared in the german c't-magazin 22/2023 p.128. An online version can be found on [heise online](https://www.heise.de/hintergrund/Programmieren-mit-Python-Doppelwuerfel-Verschluesselung-verstehen-und-umsetzen-9279040.html) behind the PayWall.

## Usage

There are a total of four parameters that the program can take. d/e for decode or encode, followed by the text and the keywords. Note: The program removes all spaces and turns it into one with only lowercase letters.
```
python3 doppelwuerfel.py <d/e> <text> <keyword1> <keyword2>
```

### Encoding
If you want to encode the text "Lorem ipsum dolor sit" with the keywords "ct" and "magazine", the command would look like this:
```
python3 doppelwuerfel.py e "Lorem ipsum dolor sit" ct magazine
```
It will return "rotpi romed mlisl ous".

### Decoding
If you want to decode "rotpi romed mlisl ous" with the same keywords "ct" and "magazine", the command would look like this:
```
python3 doppelwuerfel.py d "rotpi romed mlisl ous" ct magazine
```
The output is "loremipsumdolorsit" again.


## Copyright

Copyright ©️ 2023 Wilhelm Drehling, Heise Medien GmbH & Co. KG

This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with this program. If not, see https://www.gnu.org/licenses/.
