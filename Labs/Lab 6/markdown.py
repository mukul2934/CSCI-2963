import fileinput
import sys
import re

def convertStrong(line):
  line = re.sub(r'\*\*(.*)\*\*', r'<strong>\1</strong>', line)
  line = re.sub(r'__(.*)__', r'<strong>\1</strong>', line)
  return line

def convertEm(line):
  line = re.sub(r'\*(.*)\*', r'<em>\1</em>', line)
  line = re.sub(r'_(.*)_', r'<em>\1</em>', line)
  return line


def handleOneHash(line):
    line_array = line.split(' ')
    if line_array[0] == '#':
        tag = "<h1>"
        line_array[0] = tag;
        line_array.append("</h1>")
        line = ""
        for i in range(0, len(line_array)):
            if i == 0 or i == len(line_array) - 2:
                line += line_array[i]
            elif i == len(line_array) - 1:
                line += line_array[i]
            else:
                x = line_array[i] + ' '
                line += x
        print line
        return line
    return line

def handleTwoHash(line):
    line_array = line.split(' ')
    if line_array[0] == "##":
        tag = "<h2>"
        line_array[0] = tag;
        line_array.append("</h2>")
        line = ""
        for i in range(0, len(line_array)):
            if i == 0 or i == len(line_array) - 2:
                line += line_array[i]
            elif i == len(line_array) - 1:
                line += line_array[i]
            else:
                x = line_array[i] + ' '
                line += x
        print line
        return line
    return line

def handleThreeHash(line):
    line_array = line.split(' ')
    if line_array[0] == "###":
        tag = "<h3>"
        line_array[0] = tag;
        line_array.append("</h3>")
        line = ""
        for i in range(0, len(line_array)):
            if i == 0 or i == len(line_array) - 2:
                line += line_array[i]
            elif i == len(line_array) - 1:
                line += line_array[i]
            else:
                x = line_array[i] + ' '
                line += x

        print line
        return line
    return line

def blockQuote(lines):
    ret = "<blockquote>\n"

    for i in range(0, len(lines)):

        x = lines[i].split(' ')
        if x[1] == '#':
            ret += handleOneHash(lines[i][2:])
            ret += "\n"
        elif x[1] == "##":
            ret += handleTwoHash(lines[i][2:])
            ret += "\n"
        elif x[1] == "###":
            ret += handleThreeHash(lines[i][2:])
            ret += "\n"
        else:
            ret += lines[i][2:]
            ret += "\n"

    ret += "</blockquote>"
    print ret





inputFile = open("test.md")

# bq_start = False
# bq_lines = []
# for line in inputFile:
#     line = line.rstrip()
#     if bq_start == True and line[0] != '>':
#         bq_start = False
#     if line[0] == '>':
#         bq_start = True
#     if bq_start == True:
#         bq_lines.append(line)
# if len(bq_lines) > 0:
#     blockQuote(bq_lines)



for line in inputFile:
    line = line.rstrip()
    handleOneHash(line)
    handleTwoHash(line)
    handleThreeHash(line)
