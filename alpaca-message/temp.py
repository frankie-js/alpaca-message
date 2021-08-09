from fuzzywuzzy import fuzz, process

import alpaca

print(
    fuzz.ratio(
        alpaca.generate_string("Test"),
        r"""
   ' ' ' ' '
 /\,/"`"`"\`\ /\,
 | `         ` |
 `  ⌒       ⌒  `
 (  ◉  ❤︎   ◉   )
 (      ⌣       ) ----- Test
 (             )
  (           )
  (           )
  (           )
 (             )"`"``"`(``)
 (                        )
(                         )
(                         )
(                        )
 (     )`(     )((      )
  \, ,/   \, ,/   \  \ /
    ⌣      ⌣      ⌣ ⌣
""",
    )
)
