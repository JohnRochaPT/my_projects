"""
A eDX assignment.

This file shows how modules work

"""

__author__ = 'John Rocha'
__date__ = '2024/09/21'

# .Original Requirements:
#: It turns out that (most) YouTube videos can be embedded in other websites, just like the above.
#: For instance, if you visit https://youtu.be/xvFZjo5PgG0 on a laptop or desktop, click Share, and
#: then click Embed, you’ll see HTML (the language in which web pages are written) like the below,
#: which you could then copy into your own website’s source code, wherein iframe is an HTML
#: “element,” and src is one of several HTML “attributes” therein, the value of which, between
#: quotes, is https://www.youtube.com/embed/xvFZjo5PgG0.
#:
#:      <iframe width="560" height="315" src="https://www.youtube.com/embed/xvFZjo5PgG0"
#:       title="YouTube video player" frameborder="0" allow="accelerometer; autoplay;
#:       clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
#:
#: Because some HTML attributes are optional, you could instead minimally embed just the below.
#:
#:      <iframe src="https://www.youtube.com/embed/xvFZjo5PgG0"></iframe>
#:
#: Suppose that you’d like to extract the URLs of YouTube videos that are embedded in pages (e.g.,
#: https://www.youtube.com/embed/xvFZjo5PgG0), converting them back to shorter, shareable youtu.be
#: URLs (e.g., https://youtu.be/xvFZjo5PgG0) where they can be watched on YouTube itself.
#:
#: In a program called "watch.py", implement a function called "parse" that expects a str of HTML
#: as input, extracts any YouTube URL that’s the value of a src attribute of an iframe element
#: therein, and returns its shorter, shareable youtu.be equivalent as a str. Expect that any such
#: URL will be in one of the formats below. Assume that the value of src will be surrounded by
#: double quotes. And assume that the input will contain no more than one such URL. If the input
#: does not contain any such URL at all, return None.
#:
#:          http://youtube.com/embed/xvFZjo5PgG0
#:          https://youtube.com/embed/xvFZjo5PgG0
#:          https://www.youtube.com/embed/xvFZjo5PgG0
#:
#: Structure watch.py as follows, wherein you’re welcome to modify main and/or implement other
#: functions as you see fit, but you may not import any other libraries. You’re welcome, but not
#: required, to use re and/or sys.
#:
#:              import re
#:              import sys
#:
#:
#:              def main():
#:                  print(parse(input("HTML: ")))
#:
#:
#:              def parse(s):
#:                  ...
#:
#:
#:                  ...
#:
#:
#:              if __name__ == "__main__":
#:                  main()
#:
#:


# .Hints:
#: 1.- Recall that the re module comes with quite a few functions, per
#:     docs.python.org/3/library/re.html, including search.
#:
#: 2.- Recall that regular expressions support quite a few special characters, per
#:     docs.python.org/3/library/re.html#regular-expression-syntax.
#:
#: 3.- Because backslashes in regular expressions could be mistaken for escape sequences (like \n),
#:     best to use Python’s raw string notation for regular expression patterns. Just as format
#:     strings are prefixed with f, so are raw strings prefixed with r. For instance, instead of
#:     "harvard\.edu", use r"harvard\.edu".
#:
#: 4.- Note that re.search, if passed a pattern with “capturing groups” (i.e., parentheses),
#:     returns a “match object,” per docs.python.org/3/library/re.html#match-objects, wherein
#:     matches are 1-indexed, which you can access individually with group, per
#:     docs.python.org/3/library/re.html#re.Match.group, or collectively with groups, per
#:     docs.python.org/3/library/re.html#re.Match.groups.
#:
#: 5.- Note that * and + are “greedy,” insofar as “they match as much text as possible,” per
#:     docs.python.org/3/library/re.html#regular-expression-syntax. Adding ? immediately after
#:     either, a la *? or +?, “makes it perform the match in non-greedy or minimal fashion; as
#:     few characters as possible will be matched.”
#:


# .My pseudo code approach:
#: 1.- Use "re" library
#:
#: 2.- Sample string:
#:          <iframe width="560" height="315" src="https://www.youtube.com/embed/xvFZjo5PgG0"
#:           title="YouTube video player" frameborder="0" allow="accelerometer; autoplay;
#:           clipboard-write; encrypted-media; gyroscope; picture-in-picture"
#:           allowfullscreen></iframe>
#:
#: 2.- Prompt the user with "HTML: " and accept the user's input. If the user does not enter
#:     an input, continue to ask.
#:
#: 3.- Write a function called "parse()" which accepts a string and reads the value for "src"
#:     and then extracts the last portions ".../embed/..." of that url
#:
#: 4.- Then, write another function called "new_url()" which accepts the string url from
#:     the function parse() and returns the new formatted url
#:
#: 5.- Print to the screen the new formatted url.
#:

import re


def get_input() -> str:
    """
    get_input
        Function asks the user for an input with message "HTML: ".  It will then confirm
        that the user entered something.  If the user did not enter anything, it will keep
        asking.  If the user entered a string, it returns that string

    Returns:
        Returns the inputted string.
    """
    while True:
        response = input('HTML :').strip()
        if len(response) > 0:
            return response


def parse(response: str) -> str:
    """
    parse
        Function parse accepts a complex inputted string, searches the string for a specific
        pattern and and then forms a new string.

        The function looks at he inputted string searches for "src" and then it obtains the
        value for src.  It then extracts from the value anything after "/embed/".  Once it
        has that portion, it will append to a constant https://www.youtube.com/

    Arguments:
        response -- A non empty string containing a tag called "src"

    Preconditions:
        The string needs to be an <iframe/> format.

    Returns:
        Returns a Valid string if it is able to or None if could not do it.
    """
    match = re.search(r'<iframe.*?src="(.*?)".*?>', response)
    if match:
        # /* print(f'Found {match.group(1)}')
        old_str = match.group(1)

        # > Check to make sure the url is a youtube url
        if 'youtub' in old_str:
            pass
        else:
            return None

        # > Now get the last portion of the url
        last_slash = old_str.rfind('/')
        new_str = old_str[last_slash+1:]

        # > Now build the new url
        tgt_url = 'https://youtu.be/' + new_str
        return tgt_url
    else:
        return None


def main():
    # > Get the string containing the url from the user
    response = get_input()

    # > For testing purposes, I am setting response to a known variable
    # /* response = '<iframe width="560" height="315" src="https://www.youtube.com/embed/xvFZjo5PgG0" '
    # /* response += 'title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; '
    # /* response += 'clipboard-write; encrypted-media; gyroscope; picture-in-picture"'
    # /* response += 'allowfullscreen></iframe>'
    # /* Now pass the response to the parse() function so it can be processed

    # /* response = '<iframe src="https://cs50.harvard.edu/python"></iframe>'

    final_url = parse(response)
    print(final_url)


# > Call main ONLY when intended
if __name__ == '__main__':
    main()
