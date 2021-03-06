#!/usr/bin/python
import sys
from subprocess import call
from jinja2 import Environment, FileSystemLoader

class Host(object):

    def __init__(self, ip):
        parts = ip.split(':')
        self.ip = parts[0]
        if len(parts) > 1:
            self.port = parts[1]
        else:
            self.port = "80"


class Generator(object):

    def __init__(self):
        self.env = Environment(loader=FileSystemLoader('/root/opt/payload_generator/templates/'))

    def make(self, template, context):
        template = self.env.get_template(template)
        return template.render(context)


def list_payloads():
    print "The following payloads are available..."
    call(['tree', '/root/opt/payload_generator/templates/'])


def main():
    if "-l" in sys.argv:
         list_payloads()
         sys.exit()
    if len(sys.argv) < 3:
        print "[!] Arguments missing"
        print "[*] python generate.py <template_name> <ip_address:port>"
        sys.exit()


    gen = Generator()
    host = Host(sys.argv[2])
    print gen.make(sys.argv[1], {'host': host})


if __name__ == "__main__":
    main()

