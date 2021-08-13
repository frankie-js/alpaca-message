import click


def generate_string(inputString):
    inputLength = len(inputString)

    if inputLength > 25:
        splitStr = inputString.split(" ")
        lineOne = splitStr[:inputLength]
        lineTwo = splitStr[inputLength:]

        output = r"""   ' ' ' ' '
 /\,/"`"`"\`\ /\,
 | `         ` |
 `  ⌒       ⌒  `
 (  ◉  ❤︎   ◉   )
 (      ⌣       ) ----- %s
 (             )        %s
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
    ⌣      ⌣      ⌣ ⌣""" % (
            " ".join(lineOne),
            " ".join(lineTwo),
        )
    else:
        output = (
            r"""   ' ' ' ' '
 /\,/"`"`"\`\ /\,
 | `         ` |
 `  ⌒       ⌒  `
 (  ◉  ❤︎   ◉   )
 (      ⌣       ) ----- %s
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
            % inputString
        )
    return output


def print_message(inputString):
    print(generate_string(inputString) + "\n", end="")


def main():
    print_message("Test String")
    print_message("This is one example of a extremely long string")


if __name__ == "__main__":
    main()
