import click


# TODO: Move to template strings
def generate_string(inputString):
    if len(inputString) > 50:
        pass
    else:
        output = (
            r"""   ' ' ' ' '
 /\,/"`"`"\`\ /\,
 | `         ` |
 `  ⌒       ⌒  `
 (  ◉  ❤︎   ◉   )
 (      ⌣       ) ----- """
            + inputString
            + r"""
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
    ⌣      ⌣      ⌣ ⌣"""
        )
    return output


def print_message(inputString):
    print(generate_string(inputString) + "\n", end="")


def main():
    print_message("Test")


if __name__ == "__main__":
    main()
