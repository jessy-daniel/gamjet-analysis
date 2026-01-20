import os
import argparse

parser = argparse.ArgumentParser(description="Move files")
parser.add_argument("-v", "--version", required=True)
parser.add_argument("-f", "--force", default=False, action="store_true")
parser.add_argument("-i", '--IOV_list', default="all")
args = parser.parse_args()

os.system(f"python3 addAllIOVs.py -v {args.version} {'-f' if args.force else ''}  -i {args.IOV_list}")


for file_name in ["GamHistosMix", "GamHistosRatio"]:
    with open(f"{file_name}.C") as file:
        filedata = file.read()

    # find line that starts with string version =
    for line in filedata.split("\n"):
        if line.startswith("string version"):
            line_new = f"string version = \"{args.version}\";"
            break
    # modify line
    filedata = filedata.replace(line, line_new)


    # find line that starts with string YEAR
    for line in filedata.split("\n"):
        if line.startswith("string YEAR"):
            line_new = f"string YEAR = \"{args.IOV_list}\";"
            break
    # modify line
    filedata = filedata.replace(line, line_new)

    # print(filedata[:1000])

    with open(f"{file_name}.C", "w") as file:
        file.write(filedata)

    os.system(f"root -q -l -b {file_name}.C+g")