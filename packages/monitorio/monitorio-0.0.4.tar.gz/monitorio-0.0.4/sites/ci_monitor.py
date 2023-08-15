#!/usr/bin/env python3

""" Monitor Checkmk CI
local

fra / win / nexus / ci / tstbuild / review
 - diskspace

fra
 - docker
   - total cpu / ram
   - number of containers
   - per container
       - start / stop
       - cpu / ram
       - volumes
       - associated jenkins job
       -
   - number of images
   - number of volumes

jenkins
   - job tree
   - warning about certain job results

nexus

actions
 - rebuild
 - kill/delete containers/volumes/tags/images
 - open/close branches
"""

from monitorio.builder import Monitor, iterate, process_output, view

with Monitor("ci_dashboard"):

    @view
    async def local_resources():
        state = {}
        async for name, data in iterate(
            ps=process_output("ps", "1"),
            df=process_output("df", "2"),
        ):
            state[name] = data
            yield state
