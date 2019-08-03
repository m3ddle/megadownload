import pyperclip
import os

# test_urls = "https://mega.nz/#!7t80kACA!qsmXHvLWE8eq-J5_MSqMKXTced7ur7Djm9CeVmLIdm4 , ''https://mega.nz/#!uxFCWaxR!qfe2sFlvnBxS74NOlmfE7K5SFpfjASL0wn1iaH64YzM"
# test_urls = " +++= 'https://mega.nz/#!7t80kACA!qsmXHvLWE8eq-J5_MSqMKXTced7ur7Djm9CeVmLIdm4 'https://mega.nz/#!uxFCWaxR!qfe2sFlvnBxS74NOlmfE7K5SFpfjASL0wn1iaH64YzM"


def html_clipboard_extract():
    # Scans clipboard for mega.co urls. Did my best to remove any extra non-alphanumeric characters. Could definitely be better in that regard.
    clipboard_contents = pyperclip.paste().split()
    output_string = ""
    output_urls = []
    start_location = 0
    for string in clipboard_contents:
        if "mega." in string:
            last_dash = string.rfind("-")
            for char in string:
                if char == "H":
                    start_location = string.index("H")
                elif char == "h":
                    start_location = string.index("h")

            output_string = string[start_location:]

            output_string1 = string.replace('"', "")
            output_string2 = output_string1.replace("'", "")
            output_string3 = output_string2.replace("\"", "")
            output_urls.append(output_string3)

    return output_urls


def downloader(url_list):
    # Takes a list of urls, uses them as argumets for Megatools' megadl command which will download them one by one.
    for url in url_list:
        os.system(f"megadl '{url}'")


def main():
    downloader(html_clipboard_extract())


if __name__ == "__main__":
    main()
