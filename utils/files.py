import datetime
import random


def users_content_file_name(instance, filename):
    ext = filename.split('.')[-1]
    filename = "user/%s_%s_%s.%s" % (
        random.randint(0, 999999999), datetime.datetime.now().day, datetime.datetime.now().second, ext)
    return filename


def content_file_name(instance, filename):
    ext = filename.split('.')[-1]
    filename = "content/%s_%s_%s.%s" % (
        random.randint(0, 999999999), datetime.datetime.now().day, datetime.datetime.now().second, ext)
    return filename
