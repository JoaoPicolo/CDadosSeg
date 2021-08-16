#!/usr/bin/python3

import sys
import os

import xml.etree.ElementTree as ET


def readIntoDict(entry_dir):
    files_dir = os.listdir(entry_dir)

    final_dict = dict({})
    for file_name in files_dir:
        root = ET.parse(str(entry_dir + "/" + file_name)).getroot()
        permissions = root.findall("uses-permission")

        final_perms = list([])
        for perm in permissions:
            for att in perm.attrib:
                permission = perm.attrib[att]
                if "permission" in permission:
                    parsed = permission.split('.')
                    final_perms.append(parsed[-1])
        
        name = file_name.split("AndroidManifest_")[1]
        name = name.split(".xml")[0]
        final_dict[name] = final_perms

    return final_dict


def printApkPermissions(xmls_dict):
    print("==================\n")
    print("Permissões por APK\n")
    print("==================\n")
    for key in xmls_dict:
        print(f'{key}: {xmls_dict[key]}\n')


def uniqueApkPermissons(xmls_dict):
    new_dict = dict({})

    for key in xmls_dict:
        permissions = set(xmls_dict[key])
        unique = permissions.difference(set({}))

        for key_scd in xmls_dict:
            if key_scd != key:
                unique = unique.difference(set(xmls_dict[key_scd]))

        new_dict[key] = list(unique)

    return new_dict


def printUniquePermissions(unique_dict):
    print("=========================\n")
    print("Permissões únicas por APK\n")
    print("=========================\n")
    for key in unique_dict:
        print(f'{key}: {unique_dict[key]}\n')


def sharedApkPermissions(xmls_dict):
    shared = list(xmls_dict.keys())
    shared = set(xmls_dict[shared[0]])

    for key in xmls_dict:
        shared = shared.intersection(set(xmls_dict[key]))

    return list(shared)


def printSharedPermissions(shared):
    print("==========================\n")
    print("Permissões comuns das APKs\n")
    print("==========================\n")
    print(shared)

def main(argv):
    entry_dir = argv[0]
    if not os.path.isdir(entry_dir):
        print("Por favor forneça um diretório contendo os Android Manifests")
        sys.exit(0)

    xmls_dict = readIntoDict(entry_dir)
    printApkPermissions(xmls_dict)

    unique_dict = uniqueApkPermissons(xmls_dict)
    printUniquePermissions(unique_dict)

    shared = sharedApkPermissions(xmls_dict)
    printSharedPermissions(shared)

if __name__ == "__main__":
    main(sys.argv[1:])