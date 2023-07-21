# Doppelwürfel
Transposition cipher with two different keywords, also known as Doppelwürfel or UBCHI. With this little program you can decode and encode Strings.

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
The chiffre would look like this "rotpi romed mlisl ous".

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
