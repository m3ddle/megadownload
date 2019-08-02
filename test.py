import os

test_urls = ["https://mega.nz/#!7t80kACA!qsmXHvLWE8eq-J5_MSqMKXTced7ur7Djm9CeVmLIdm4",
             "https://mega.nz/#!uxFCWaxR!qfe2sFlvnBxS74NOlmfE7K5SFpfjASL0wn1iaH64YzM"]

# os.system('ls') <- Use this to execute script once written


def downloader(url_list):
    for url in url_list:
        os.system(f"megadl '{url}'")


downloader(test_urls)
