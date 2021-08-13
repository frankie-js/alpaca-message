from fuzzywuzzy import fuzz, process

import alpaca


# Sanity Check
def test_always_passes():
    assert True


# Uses perfect fuzzy matching due to non-viewable errors
def test_one_line():
    assert (
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
        == 100
    )


def test_two_line():
    assert (
        fuzz.ratio(
            alpaca.generate_string("This is a extremely long test message"),
            r"""
   ' ' ' ' '
 /\,/"`"`"\`\ /\,
 | `         ` |
 `  ⌒       ⌒  `
 (  ◉  ❤︎   ◉   )
 (      ⌣       ) ----- This is a
 (             )        extremely long test message
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
        == 100
    )
