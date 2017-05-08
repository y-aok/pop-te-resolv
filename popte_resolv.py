#!/usr/bin/env python

import base64
import lxml.html
import os
import os.path
import random
import requests
import sys


class pop_resolv(object):
    """Fetch POP-TEAM-EPIC randomly and download."""

    def __init__(self):
        self.urls  = ('http://mangalifewin.takeshobo.co.jp/rensai/popute/?',
                      'http://mangalifewin.takeshobo.co.jp/rensai/popute2/?')
        self.start = random.choice(self.urls)

    def gen_lxml(self, l):
        try:
            self.r = requests.get(l)
            self.r.encoding = self.r.apparent_encoding
            self.d = lxml.html.fromstring(self.r.text)
        except Exception:
            raise Exception('failed to requests.get from {}'.format(l))

    def write(self, d):
        with open(d, "wb") as f:
            f.write(self.img)

    def run(self):
        try:
            self.gen_lxml(self.start)
            es = self.d.xpath('//ul/li//td/a')
            self.choice = random.choice(es).attrib['href']

            self.gen_lxml(self.choice)
            self.e     = self.d.xpath('//img[@alt="comic"]')[0]
            self.src   = self.e.attrib['src']
            self.imb   = self.src.split("base64,")[1]
            self.img   = base64.b64decode(self.imb)
        except Exception:
            raise


def main():
    try:
        d = os.path.join(os.getcwd(), sys.argv[1])
    except IndexError:
        d = os.path.join(os.getcwd(), "record.jpg")

    p = pop_resolv()
    try:
        p.run()
        p.write(d)
        print("downloaded as {}".format(d))
    except Exception as e:
        print("failed: {}".format(e))
        sys.exit()

if __name__ == "__main__":
    main()
