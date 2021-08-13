import click


def split_list(a_list):
    half = len(a_list)//2
    return a_list[:half], a_list[half:]


def generate_string(inputString):
    inputLength = len(inputString)

    if inputLength > 25:
        splitStr = inputString.split(" ")
        lineOne, lineTwo = split_list(splitStr)

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


@click.command()
@click.argument("message", default="")
def main(message):
    click.echo(generate_string(message))


if __name__ == "__main__":
    main()
