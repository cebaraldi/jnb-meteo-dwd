
# Help
  
# < Return to selection

# request
# Estimated number of fields: 858000

# Python script
# MARS request
# For more information on how to retrieve data programmatically, in Python, please go to Access ECMWF Public Datasets.

#!/usr/bin/env python
from ecmwfapi import ECMWFDataServer

server = ECMWFDataServer()

server.retrieve({
    "class": "ti",
    "dataset": "tigge",
    "date": "2022-09-01/to/2022-09-30",
    "expver": "prod",
    "grid": "0.5/0.5",
    "levtype": "sfc",
    "origin": "kwbc",
    "param": "228002",
    "step": "0",
    "time": "00:00:00/12:00:00",
    "type": "cf",
    "target": "output"
})

server.retrieve({
    "class": "ti",
    "dataset": "tigge",
    "date": "2022-09-01/to/2022-09-30",
    "expver": "prod",
    "grid": "0.5/0.5",
    "levtype": "sfc",
    "origin": "cwao",
    "param": "134/136/151/165/166/167/168/235/228002/228139/228141/228164",
    "step": "0/6/12/18/24/30/36/42/48/54/60/66/72/78/84/90/96/102/108/114/120/126/132/138/144/150/156/162/168/174/180/186/192/198/204/210/216/222/228/234/240/246/252/258/264/270/276/282/288/294/300/306/312/318/324/330/336/342/348/354/360/366/372/378/384",
    "time": "00:00:00/12:00:00",
    "type": "cf",
    "target": "output"
})

server.retrieve({
    "class": "ti",
    "dataset": "tigge",
    "date": "2022-09-01/to/2022-09-30",
    "expver": "prod",
    "grid": "0.5/0.5",
    "levtype": "sfc",
    "origin": "kwbc",
    "param": "59/134/136/146/147/151/165/166/167/168/172/176/177/179/235/228001/228039/228139/228141/228144/228228",
    "step": "0/6/12/18/24/30/36/42/48/54/60/66/72/78/84/90/96/102/108/114/120/126/132/138/144/150/156/162/168/174/180/186/192/198/204/210/216/222/228/234/240/246/252/258/264/270/276/282/288/294/300/306/312/318/324/330/336/342/348/354/360/366/372/378/384",
    "time": "00:00:00/12:00:00",
    "type": "cf",
    "target": "output"
})

server.retrieve({
    "class": "ti",
    "dataset": "tigge",
    "date": "2022-09-01/to/2022-09-30",
    "expver": "prod",
    "grid": "0.5/0.5",
    "levtype": "sfc",
    "origin": "babj",
    "param": "59/134/136/146/147/151/165/166/167/168/172/176/177/235/228002/228141/228144/228164/228228",
    "step": "0/6/12/18/24/30/36/42/48/54/60/66/72/78/84/90/96/102/108/114/120/126/132/138/144/150/156/162/168/174/180/186/192/198/204/210/216/222/228/234/240/246/252/258/264/270/276/282/288/294/300/306/312/318/324/330/336/342/348/354/360",
    "time": "00:00:00/12:00:00",
    "type": "cf",
    "target": "output"
})

server.retrieve({
    "class": "ti",
    "dataset": "tigge",
    "date": "2022-09-01/to/2022-09-30",
    "expver": "prod",
    "grid": "0.5/0.5",
    "levtype": "sfc",
    "origin": "ecmf",
    "param": "59/134/136/146/147/151/165/166/167/168/172/176/177/179/189/235/228001/228002/228039/228139/228141/228144/228164/228228",
    "step": "0/6/12/18/24/30/36/42/48/54/60/66/72/78/84/90/96/102/108/114/120/126/132/138/144/150/156/162/168/174/180/186/192/198/204/210/216/222/228/234/240/246/252/258/264/270/276/282/288/294/300/306/312/318/324/330/336/342/348/354/360",
    "time": "00:00:00/12:00:00",
    "type": "cf",
    "target": "output"
})

server.retrieve({
    "class": "ti",
    "dataset": "tigge",
    "date": "2022-09-01/to/2022-09-30",
    "expver": "prod",
    "grid": "0.5/0.5",
    "levtype": "sfc",
    "origin": "egrr",
    "param": "59/134/136/146/147/151/165/166/167/168/172/176/177/179/235/228001/228002/228039/228139/228141/228144/228164/228228",
    "step": "0/6/12/18/24/30/36/42/48/54/60/66/72/78/84/90/96/102/108/114/120/126/132/138/144/150/156/162/168/174/180/186/192/198/204/210/216/222/228/234/240/246/252/258/264/270/276/282/288/294/300/306/312/318/324/330/336/342/348/354/360",
    "time": "00:00:00/12:00:00",
    "type": "cf",
    "target": "output"
})

server.retrieve({
    "class": "ti",
    "dataset": "tigge",
    "date": "2022-09-01/to/2022-09-30",
    "expver": "prod",
    "grid": "0.5/0.5",
    "levtype": "sfc",
    "origin": "rksl",
    "param": "134/146/147/151/165/166/167/168/176/177/179/235/228141/228164/228228",
    "step": "0/6/12/18/24/30/36/42/48/54/60/66/72/78/84/90/96/102/108/114/120/126/132/138/144/150/156/162/168/174/180/186/192/198/204/210/216/222/228/234/240/246/252/258/264/270/276/282/288",
    "time": "00:00:00/12:00:00",
    "type": "cf",
    "target": "output"
})

server.retrieve({
    "class": "ti",
    "dataset": "tigge",
    "date": "2022-09-01/to/2022-09-30",
    "expver": "prod",
    "grid": "0.5/0.5",
    "levtype": "sfc",
    "origin": "rjtd",
    "param": "134/136/146/147/151/165/166/167/168/172/176/177/179/235/228002/228039/228141/228164/228228",
    "step": "0/6/12/18/24/30/36/42/48/54/60/66/72/78/84/90/96/102/108/114/120/126/132/138/144/150/156/162/168/174/180/186/192/198/204/210/216/222/228/234/240/246/252/258/264",
    "time": "00:00:00/12:00:00",
    "type": "cf",
    "target": "output"
})

server.retrieve({
    "class": "ti",
    "dataset": "tigge",
    "date": "2022-09-01/to/2022-09-30",
    "expver": "prod",
    "grid": "0.5/0.5",
    "levtype": "sfc",
    "origin": "ammc/rksl",
    "param": "172/228002",
    "step": "0/6/12/18/24/30/36/42/48/54/60/66/72/78/84/90/96/102/108/114/120/126/132/138/144/150/156/162/168/174/180/186/192/198/204/210/216/222/228/234/240",
    "time": "00:00:00/12:00:00",
    "type": "cf",
    "target": "output"
})

server.retrieve({
    "class": "ti",
    "dataset": "tigge",
    "date": "2022-09-01/to/2022-09-30",
    "expver": "prod",
    "grid": "0.5/0.5",
    "levtype": "sfc",
    "origin": "dems",
    "param": "134/146/147/151/165/166/167/168/172/176/177/179/235/228002/228139/228141/228164/228228",
    "step": "0/6/12/18/24/30/36/42/48/54/60/66/72/78/84/90/96/102/108/114/120/126/132/138/144/150/156/162/168/174/180/186/192/198/204/210/216/222/228/234/240",
    "time": "00:00:00/12:00:00",
    "type": "cf",
    "target": "output"
})

server.retrieve({
    "class": "ti",
    "dataset": "tigge",
    "date": "2022-09-01/to/2022-09-30",
    "expver": "prod",
    "grid": "0.5/0.5",
    "levtype": "sfc",
    "origin": "vabb",
    "param": "134/146/147/151/165/166/167/168/172/177/179/235/228002/228139/228228",
    "step": "0/6/12/18/24/30/36/42/48/54/60/66/72/78/84/90/96/102/108/114/120/126/132/138/144/150/156/162/168/174/180/186/192/198/204/210/216/222/228/234/240",
    "time": "00:00:00/12:00:00",
    "type": "cf",
    "target": "output"
})

server.retrieve({
    "class": "ti",
    "dataset": "tigge",
    "date": "2022-09-01/to/2022-09-30",
    "expver": "prod",
    "grid": "0.5/0.5",
    "levtype": "sfc",
    "origin": "lfpw",
    "param": "59/134/151/165/166/167/168/172/235/228002/228139/228141/228164",
    "step": "0/6/12/18/24/30/36/42/48",
    "time": "00:00:00/12:00:00",
    "type": "cf",
    "target": "output"
})

server.retrieve({
    "class": "ti",
    "dataset": "tigge",
    "date": "2022-09-01/to/2022-09-30",
    "expver": "prod",
    "grid": "0.5/0.5",
    "levtype": "sfc",
    "origin": "cwao",
    "param": "121/122/228228",
    "step": "6/12/18/24/30/36/42/48/54/60/66/72/78/84/90/96/102/108/114/120/126/132/138/144/150/156/162/168/174/180/186/192/198/204/210/216/222/228/234/240/246/252/258/264/270/276/282/288/294/300/306/312/318/324/330/336/342/348/354/360/366/372/378/384",
    "time": "00:00:00/12:00:00",
    "type": "cf",
    "target": "output"
})

server.retrieve({
    "class": "ti",
    "dataset": "tigge",
    "date": "2022-09-01/to/2022-09-30",
    "expver": "prod",
    "grid": "0.5/0.5",
    "levtype": "sfc",
    "origin": "kwbc",
    "param": "121/122",
    "step": "6/12/18/24/30/36/42/48/54/60/66/72/78/84/90/96/102/108/114/120/126/132/138/144/150/156/162/168/174/180/186/192/198/204/210/216/222/228/234/240/246/252/258/264/270/276/282/288/294/300/306/312/318/324/330/336/342/348/354/360/366/372/378/384",
    "time": "00:00:00/12:00:00",
    "type": "cf",
    "target": "output"
})

server.retrieve({
    "class": "ti",
    "dataset": "tigge",
    "date": "2022-09-01/to/2022-09-30",
    "expver": "prod",
    "grid": "0.5/0.5",
    "levtype": "sfc",
    "origin": "babj",
    "param": "121/122/179",
    "step": "6/12/18/24/30/36/42/48/54/60/66/72/78/84/90/96/102/108/114/120/126/132/138/144/150/156/162/168/174/180/186/192/198/204/210/216/222/228/234/240/246/252/258/264/270/276/282/288/294/300/306/312/318/324/330/336/342/348/354/360",
    "time": "00:00:00/12:00:00",
    "type": "cf",
    "target": "output"
})

server.retrieve({
    "class": "ti",
    "dataset": "tigge",
    "date": "2022-09-01/to/2022-09-30",
    "expver": "prod",
    "grid": "0.5/0.5",
    "levtype": "sfc",
    "origin": "ecmf/egrr",
    "param": "121/122",
    "step": "6/12/18/24/30/36/42/48/54/60/66/72/78/84/90/96/102/108/114/120/126/132/138/144/150/156/162/168/174/180/186/192/198/204/210/216/222/228/234/240/246/252/258/264/270/276/282/288/294/300/306/312/318/324/330/336/342/348/354/360",
    "time": "00:00:00/12:00:00",
    "type": "cf",
    "target": "output"
})

server.retrieve({
    "class": "ti",
    "dataset": "tigge",
    "date": "2022-09-01/to/2022-09-30",
    "expver": "prod",
    "grid": "0.5/0.5",
    "levtype": "sfc",
    "origin": "rksl",
    "param": "121/122",
    "step": "6/12/18/24/30/36/42/48/54/60/66/72/78/84/90/96/102/108/114/120/126/132/138/144/150/156/162/168/174/180/186/192/198/204/210/216/222/228/234/240/246/252/258/264/270/276/282/288",
    "time": "00:00:00/12:00:00",
    "type": "cf",
    "target": "output"
})

server.retrieve({
    "class": "ti",
    "dataset": "tigge",
    "date": "2022-09-01/to/2022-09-30",
    "expver": "prod",
    "grid": "0.5/0.5",
    "levtype": "sfc",
    "origin": "rjtd",
    "param": "121/122",
    "step": "6/12/18/24/30/36/42/48/54/60/66/72/78/84/90/96/102/108/114/120/126/132/138/144/150/156/162/168/174/180/186/192/198/204/210/216/222/228/234/240/246/252/258/264",
    "time": "00:00:00/12:00:00",
    "type": "cf",
    "target": "output"
})

server.retrieve({
    "class": "ti",
    "dataset": "tigge",
    "date": "2022-09-01/to/2022-09-30",
    "expver": "prod",
    "grid": "0.5/0.5",
    "levtype": "sfc",
    "origin": "ammc",
    "param": "121/122/134/136/146/147/151/165/166/167/168/176/177/179/228139/228144/228164/228228",
    "step": "6/12/18/24/30/36/42/48/54/60/66/72/78/84/90/96/102/108/114/120/126/132/138/144/150/156/162/168/174/180/186/192/198/204/210/216/222/228/234/240",
    "time": "00:00:00/12:00:00",
    "type": "cf",
    "target": "output"
})

server.retrieve({
    "class": "ti",
    "dataset": "tigge",
    "date": "2022-09-01/to/2022-09-30",
    "expver": "prod",
    "grid": "0.5/0.5",
    "levtype": "sfc",
    "origin": "dems/vabb",
    "param": "121/122",
    "step": "6/12/18/24/30/36/42/48/54/60/66/72/78/84/90/96/102/108/114/120/126/132/138/144/150/156/162/168/174/180/186/192/198/204/210/216/222/228/234/240",
    "time": "00:00:00/12:00:00",
    "type": "cf",
    "target": "output"
})

server.retrieve({
    "class": "ti",
    "dataset": "tigge",
    "date": "2022-09-01/to/2022-09-30",
    "expver": "prod",
    "grid": "0.5/0.5",
    "levtype": "sfc",
    "origin": "lfpw",
    "param": "121/122/146/147/176/177/179/228144/228228",
    "step": "6/12/18/24/30/36/42/48",
    "time": "00:00:00/12:00:00",
    "type": "cf",
    "target": "output"
})

server.retrieve({
    "class": "ti",
    "dataset": "tigge",
    "date": "2022-09-01/to/2022-09-30",
    "expver": "prod",
    "grid": "0.5/0.5",
    "levtype": "sfc",
    "origin": "lfpw",
    "param": "121/122/146/147/176/177/179/228144/228228",
    "step": "6/12/18/24/30/36/42/48/54/60/66/72/78/84/90",
    "time": "06:00:00",
    "type": "cf",
    "target": "output"
})

server.retrieve({
    "class": "ti",
    "dataset": "tigge",
    "date": "2022-09-01/to/2022-09-30",
    "expver": "prod",
    "grid": "0.5/0.5",
    "levtype": "sfc",
    "origin": "lfpw",
    "param": "59/134/151/165/166/167/168/172/235/228002/228139/228141/228164",
    "step": "0/6/12/18/24/30/36/42/48/54/60/66/72/78/84/90",
    "time": "06:00:00",
    "type": "cf",
    "target": "output"
})

server.retrieve({
    "class": "ti",
    "dataset": "tigge",
    "date": "2022-09-01/to/2022-09-30",
    "expver": "prod",
    "grid": "0.5/0.5",
    "levtype": "sfc",
    "origin": "lfpw",
    "param": "136",
    "step": "0/6/12/18/24/30/36/42/48/54/60/66/72",
    "time": "06:00:00",
    "type": "cf",
    "target": "output"
})

server.retrieve({
    "class": "ti",
    "dataset": "tigge",
    "date": "2022-09-01/to/2022-09-30",
    "expver": "prod",
    "grid": "0.5/0.5",
    "levtype": "sfc",
    "origin": "ammc",
    "param": "121/122/134/146/147/151/165/166/167/168/176/177/179/228164/228228",
    "step": "6/12/18/24/30/36/42/48/54/60/66/72/78/84/90/96/102/108/114/120/126/132/138/144/150/156/162/168/174/180/186/192/198/204/210/216/222/228/234/240",
    "time": "06:00:00/18:00:00",
    "type": "cf",
    "target": "output"
})

server.retrieve({
    "class": "ti",
    "dataset": "tigge",
    "date": "2022-09-01/to/2022-09-30",
    "expver": "prod",
    "grid": "0.5/0.5",
    "levtype": "sfc",
    "origin": "ammc/egrr",
    "param": "172/228002",
    "step": "0",
    "time": "06:00:00/18:00:00",
    "type": "cf",
    "target": "output"
})

server.retrieve({
    "class": "ti",
    "dataset": "tigge",
    "date": "2022-09-01/to/2022-09-30",
    "expver": "prod",
    "grid": "0.5/0.5",
    "levtype": "sfc",
    "origin": "egrr",
    "param": "121/122",
    "step": "6/12/18/24/30/36/42/48/54/60/66/72/78/84/90/96/102/108/114/120/126/132/138/144/150/156/162/168/174",
    "time": "06:00:00/18:00:00",
    "type": "cf",
    "target": "output"
})

server.retrieve({
    "class": "ti",
    "dataset": "tigge",
    "date": "2022-09-01/to/2022-09-30",
    "expver": "prod",
    "grid": "0.5/0.5",
    "levtype": "sfc",
    "origin": "egrr",
    "param": "134/146/147/151/165/166/167/168/176/177/179/235/228141/228144/228164/228228",
    "step": "0/6/12/18/24/30/36/42/48/54/60/66/72/78/84/90/96/102/108/114/120/126/132/138/144/150/156/162/168/174",
    "time": "06:00:00/18:00:00",
    "type": "cf",
    "target": "output"
})

server.retrieve({
    "class": "ti",
    "dataset": "tigge",
    "date": "2022-09-01/to/2022-09-30",
    "expver": "prod",
    "grid": "0.5/0.5",
    "levtype": "sfc",
    "origin": "kwbc",
    "param": "121/122",
    "step": "6/12/18/24/30/36/42/48/54/60/66/72/78/84/90/96/102/108/114/120/126/132/138/144/150/156/162/168/174/180/186/192/198/204/210/216/222/228/234/240/246/252/258/264/270/276/282/288/294/300/306/312/318/324/330/336/342/348/354/360/366/372/378/384",
    "time": "06:00:00/18:00:00",
    "type": "cf",
    "target": "output"
})

server.retrieve({
    "class": "ti",
    "dataset": "tigge",
    "date": "2022-09-01/to/2022-09-30",
    "expver": "prod",
    "grid": "0.5/0.5",
    "levtype": "sfc",
    "origin": "kwbc",
    "param": "59/134/136/146/147/151/165/166/167/168/172/176/177/179/235/228001/228039/228139/228141/228144/228228",
    "step": "0/6/12/18/24/30/36/42/48/54/60/66/72/78/84/90/96/102/108/114/120/126/132/138/144/150/156/162/168/174/180/186/192/198/204/210/216/222/228/234/240/246/252/258/264/270/276/282/288/294/300/306/312/318/324/330/336/342/348/354/360/366/372/378/384",
    "time": "06:00:00/18:00:00",
    "type": "cf",
    "target": "output"
})

server.retrieve({
    "class": "ti",
    "dataset": "tigge",
    "date": "2022-09-01/to/2022-09-30",
    "expver": "prod",
    "grid": "0.5/0.5",
    "levtype": "sfc",
    "origin": "kwbc",
    "param": "228002",
    "step": "0",
    "time": "06:00:00/18:00:00",
    "type": "cf",
    "target": "output"
})

server.retrieve({
    "class": "ti",
    "dataset": "tigge",
    "date": "2022-09-01/to/2022-09-30",
    "expver": "prod",
    "grid": "0.5/0.5",
    "levtype": "sfc",
    "origin": "lfpw",
    "param": "121/122/146/147/176/177/179/228144/228228",
    "step": "6/12/18/24/30/36/42/48/54/60/66/72/78/84/90/96/102/108",
    "time": "18:00:00",
    "type": "cf",
    "target": "output"
})

server.retrieve({
    "class": "ti",
    "dataset": "tigge",
    "date": "2022-09-01/to/2022-09-30",
    "expver": "prod",
    "grid": "0.5/0.5",
    "levtype": "sfc",
    "origin": "lfpw",
    "param": "59/134/136/151/165/166/167/168/172/235/228002/228139/228141/228164",
    "step": "0/6/12/18/24/30/36/42/48/54/60/66/72/78/84/90/96/102/108",
    "time": "18:00:00",
    "type": "cf",
    "target": "output"
})
# © European Centre for Medium-Range Weather Forecasts

# AccessibilityPrivacyTerms of useContact us 