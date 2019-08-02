import pyperclip as pyclip
import os

# test_urls = "https://mega.nz/#!7t80kACA!qsmXHvLWE8eq-J5_MSqMKXTced7ur7Djm9CeVmLIdm4 , ''https://mega.nz/#!uxFCWaxR!qfe2sFlvnBxS74NOlmfE7K5SFpfjASL0wn1iaH64YzM"
# test_urls = " +++= 'https://mega.nz/#!7t80kACA!qsmXHvLWE8eq-J5_MSqMKXTced7ur7Djm9CeVmLIdm4 'https://mega.nz/#!uxFCWaxR!qfe2sFlvnBxS74NOlmfE7K5SFpfjASL0wn1iaH64YzM"


def html_clipboard_extract():
    clipboard_contents = pyclip.paste().split()
    output_string = ""
    output_urls = []
    start_location = 0
    for string in clipboard_contents:
        if "mega." in string:
            last_dash = string.rfind("-")
            last_url_char = string.rfind("-")
            for char in string:
                if char == "H":
                    start_location = string.index("H")
                elif char == "h":
                    start_location = string.index("h")
            output_string = string[start_location:]
# save the location of the last occurance of / then
# scan the rest for numbers and letters then stop at the first non
# letter or int
            for char in string[last_dash:]:
                if char.isalpha() == False and char.isdigit() == False:
                    last_url_char = string.index(char)
                    break
            output_string1 = string.replace('"', "")
            output_string2 = output_string1.replace("'", "")
            output_string3 = output_string2.replace("\"", "")
            output_urls.append(output_string3)

    return output_urls


def downloader(url_list):
    for url in url_list:
        os.system(f"megadl '{url}'")


def main():
    downloader(html_clipboard_extract())


if __name__ == "__main__":
    main()
