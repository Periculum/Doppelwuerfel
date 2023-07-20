# Doppelwuerfel
Transposition cipher with two different keywords, also known as Doppelwürfel or UBCHI. With this little program you can decode and encode Strings.

# Usage

There are a total of four parameters that the programme can take. d/e for decode or encode, followed by the text and the keywords.
```
python3 doppelwuerfel.py <d/e> <text> <keyword1> <keyword2>
```

If you want to encode the text "loremipsum" with the keywords "ct" and "magazine", the command would look like this:
```
python3 doppelwuerfel.py e loremipsum ct magazine
```

# Copyright

Copyright ©️ 2023 Wilhelm Drehling, Heise Medien GmbH & Co. KG

This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with this program. If not, see https://www.gnu.org/licenses/.
