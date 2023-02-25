# MIT License

# Copyright (c) 2023 MohitLabs

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import numpy as np
from flatlib.datetime import Datetime
from flatlib.geopos import GeoPos
from flatlib.chart import Chart
from flatlib import const

def fetch_sentiment():
    current_date = Datetime("2023/02/21", "16:45", "+00:00")
    current_location = GeoPos(28.834968, 78.751423)

    chart = Chart(current_date, current_location)
    house1 = chart.get(const.HOUSE1)
    house2 = chart.get(const.HOUSE2)
    house3 = chart.get(const.HOUSE3)
    house4 = chart.get(const.HOUSE4)
    house5 = chart.get(const.HOUSE5)
    house6 = chart.get(const.HOUSE6)
    house7 = chart.get(const.HOUSE7)
    house8 = chart.get(const.HOUSE8)
    house9 = chart.get(const.HOUSE9)
    house10 = chart.get(const.HOUSE10)
    house11 = chart.get(const.HOUSE11)
    house12 = chart.get(const.HOUSE12)
    print(house1)
    print(house2)
    print(house3)
    print(house4)
    print(house5)
    print(house6)
    print(house7)
    print(house8)
    print(house9)
    print(house10)
    print(house11)
    print(house12)
