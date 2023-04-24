#! /usr/bin/env python3
#
# bootstrap/show_directory.py

# rudiweb-examples
#
# Copyright 2023 J4M Solutions
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Show directory with support for bootstrap.
"""

import os
import os.path
from os.path import isdir, isfile


def main():
    try:
        env = os.environ
        docpath = env.get("DOCPATH")
        transpath = env.get("PATH_TRANSLATED")
        docdirname = os.path.dirname(docpath)
        docbasename = os.path.basename(docpath)
        if docpath.endswith("/index.html") and transpath.endswith("/index.html"):
            docpath = docpath[:-11]
            transpath = transpath[:-11]

        l = [
            # """<section class="bg-light text-dark">"""),
            """<section>""",
            """<div class="container">""",
            f"<div>Location: {docpath}</div>",
            # f"<div>Path: {transpath}</div>",
            """<table class="table table-hover table-striped">""",
            "<thead><tr><th>Name</th><th>Type</th><th>Size</th></tr></thead>",
            "<tbody>",
        ]
        names = [name for name in os.listdir(transpath) if name != docbasename]
        if names:
            for name in os.listdir(transpath):
                path = os.path.join(transpath, name)
                if isdir(path):
                    root = name
                    ext = ".directory"
                    size = 0
                    name = f"{name}/"
                else:
                    root, ext = os.path.splitext(name)
                    size = 0
                href = os.path.join(docdirname, name)
                l.append(
                    f"""<tr><td><a href="{href}">{root}</a></td><td>{ext[1:]}</td><td>{size}</td></tr>"""
                )
        else:
            l.append("""<tr><td colspan="3">No entries.</td></tr>""")
        l.extend(
            [
                "</tbody>",
                "</table>",
                "</div>",
                "</section>",
            ]
        )
        print("".join(l))
    except Exception as e:
        pass


if __name__ == "__main__":
    main()
